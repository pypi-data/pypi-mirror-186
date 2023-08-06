import copy
import math
import numpy as np
from typing import Union, List

from QuICT.ops.linalg.cpu_calculator import dot, tensor
from QuICT.tools.exception.core import ValueError, TypeError
from .utils import NoiseChannel


class ReadoutError:
    """ The Readout error class

    Example:
        p(n|m) describe the probability of getting the noise outcome n with the truly measured result m. \n
        The ReadoutError for 1 qubit: \n
            P = [[p(0|0), p(1|0)], = [[0.8, 0.2], \n
                 [p(0|1), p(1|1)]]    [0.3, 0.7]]

        The ReadoutError for 2 qubit:
            P = [[p(00|00), p(01|00), p(10|00), p(11|00)], \n
                 [p(00|01), p(01|01), p(10|01), p(11|01)], \n
                 [p(00|10), p(01|10), p(10|10), p(11|10)], \n
                 [p(00|11), p(01|11), p(10|11), p(11|11)]] \n

    Important:
        The sum of each rows in the prob should equal to 1.

    Args:
        prob (List, np.ndarray): The probability of outcome assignment
    """
    @property
    def qubits(self) -> int:
        return self._qubits

    @property
    def prob(self) -> np.ndarray:
        return self._prob

    @property
    def type(self) -> str:
        return self._type

    def __init__(self, prob: Union[List, np.ndarray]):
        self._prob = self._probability_check(prob)
        self._qubits = int(np.log2(self._prob.shape[0]))
        self._type = NoiseChannel.readout

    def __str__(self):
        ro_str = f"{self.type.value} with {self.qubits} qubits.\n"
        for i, probs in enumerate(self.prob):
            ro_str += f"P[{i}]: {probs}\n"

        return ro_str

    def _probability_check(self, prob):
        if not isinstance(prob, (list, np.ndarray)):
            raise TypeError("ReadoutError.prob", "list or np.ndarray.", f"{type(prob)}")

        prob = np.array(prob)
        row, col = prob.shape
        if row != col:
            raise ValueError("ReadoutError.prob.shape", "row == col", f"{row} and {col}")

        n = int(np.log2(row))
        if 2 ** n != row:
            raise ValueError("ReadoutError.prob.shape", "2 ** n", f"{row}")

        for p in prob:
            if not isinstance(prob, (list, np.ndarray)):
                raise TypeError("ReadoutError.prob", "list or np.ndarray.", f"{type(prob)}")

            sum_p = [i for i in p if i >= 0 and i <= 1]
            if not math.isclose(sum(sum_p), 1, rel_tol=1e-6) or len(sum_p) != len(p):
                raise ValueError("ReadoutError.prob", "same to 1 for each row", f"{sum(sum_p)}")

        return prob

    def expand(self, extend_qubits: int, change_itself: bool = False):
        """ Expand noise with size of extend_qubits. """
        extra_identity = np.identity(2 ** extend_qubits)
        expand_prob = tensor(self.prob, extra_identity)

        if change_itself:
            self._prob = expand_prob
            self._qubits += extend_qubits
        else:
            return ReadoutError(expand_prob)

    def compose(self, other):
        """ dot(self.prob, other.prob) """
        assert isinstance(other, ReadoutError)

        left_prob, right_prob = self.prob, other.prob
        if self.qubits > other.qubits:
            right_prob = other.expand(self.qubits - other.qubits).prob
        elif self.qubits < other.qubits:
            left_prob = self.expand(other.qubits - self.qubits).prob

        compose_prob = dot(left_prob, right_prob)
        return ReadoutError(compose_prob)

    def tensor(self, other):
        """ tensor(self.prob, other.prob) """
        assert isinstance(other, ReadoutError)

        tensor_prob = tensor(self.prob, other.prob)
        return ReadoutError(tensor_prob)

    def power(self, n: int):
        """ (self.prob)^n """
        assert isinstance(n, int)

        based_prob = copy.deepcopy(self.prob)
        for _ in range(1, n):
            based_prob = dot(based_prob, self.prob)

        return ReadoutError(based_prob)

    def is_identity(self) -> bool:
        """ Whether self.prob is identity matrix. """
        id_matrix = np.identity(2 ** self._qubits)
        if np.allclose(self._prob, id_matrix, rtol=1e-6):
            return True

        return False

    def apply_to_qubits(self, measured_result: int):
        prob = np.random.random()
        related_prob_error = self._prob[measured_result]
        for idx, error_prob in enumerate(related_prob_error):
            if prob <= error_prob:
                return idx

            prob -= error_prob
