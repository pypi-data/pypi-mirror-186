import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.core.gate.backend import MCTOneAux
from QuICT.tools import Logger
from QuICT.tools.exception.core import *

logger = Logger("Grover")

ALPHA = 1.5


def degree_counterclockwise(v1: np.ndarray, v2: np.ndarray):
    """from v1 to v2
    """
    d = np.real(np.arccos(sum(v1 * v2) / np.sqrt(sum(v1 * v1) * sum(v2 * v2))))
    if d > 0.5 * np.pi:
        d = np.pi - d
    return d


class Grover:
    """ simple grover

    Quantum Computation and Quantum Information - Michael A. Nielsen & Isaac L. Chuang
    """

    def __init__(self, simulator) -> None:
        self.simulator = simulator

    def _grover_operator(self, n, n_ancilla, oracle, is_bit_flip=False):
        cgate = CompositeGate()
        index_q = list(range(n))
        ancilla_q = list(range(n, n + n_ancilla))
        # Grover iteration
        if is_bit_flip:
            X | cgate(ancilla_q[0])
            H | cgate(ancilla_q[0])
        oracle | cgate(index_q + ancilla_q)
        if is_bit_flip:
            H | cgate(ancilla_q[0])
            X | cgate(ancilla_q[0])
        for idx in index_q:
            H | cgate(idx)
        # control phase shift
        for idx in index_q:
            X | cgate(idx)
        H | cgate(index_q[n - 1])
        MCTOneAux().execute(n + 1) | cgate(index_q + ancilla_q[:1])
        H | cgate(index_q[n - 1])
        for idx in index_q:
            X | cgate(idx)
        # control phase shift end
        for idx in index_q:
            H | cgate(idx)
        return cgate

    def circuit(
        self,
        n,
        n_ancilla,
        oracle,
        n_solution=1,
        measure=True,
        is_bit_flip=False,
        iteration_number_forced=False,
    ):
        """ grover search for f with custom oracle

        Args:
            n(int): the length of input of f
            n_ancilla(int): length of oracle working space. assume clean
            oracle(CompositeGate): the oracle that flip phase of target state.
                [0:n] is index qreg,
                [n:n+k] is ancilla
            n_solution(int): number of solution
            measure(bool): measure included or not
            iteration_number_forced(bool): if True, n_solution is used as iteration count

        Returns:
            int: the a satisfies that f(a) = 1
        """
        assert n_ancilla > 0, "at least 1 ancilla, which is shared by MCT part"
        circuit = Circuit(n + n_ancilla)
        index_q = list(range(n))
        if iteration_number_forced:
            T = n_solution
        else:
            N = 2 ** n
            theta = np.arcsin(np.sqrt(n_solution / N))
            T = int(np.round((np.pi / 2 - theta) / (2 * theta)))

        grover_operator = self._grover_operator(n, n_ancilla, oracle, is_bit_flip)

        # create equal superposition state in index_q
        for idx in index_q:
            H | circuit(idx)
        # rotation
        for i in range(T):
            grover_operator | circuit
        for idx in index_q:
            if measure:
                Measure | circuit(idx)
        logger.info(
            f"circuit width          = {circuit.width():4}\n"
            + f"oracle  calls          = {T:4}\n"
            + f"other circuit size     = {circuit.size() - oracle.size()*T:4}\n"
        )
        return circuit

    def run(
        self,
        n,
        n_ancilla,
        oracle,
        n_solution=1,
        measure=True,
        is_bit_flip=False,
        check_solution=None,
    ):
        simulator = self.simulator
        index_q = list(range(n))
        # unkonwn solution number
        if n_solution is None:
            assert check_solution is not None
            n_solution_guess = 1 << n
            while n_solution_guess > 0:
                logger.info(f"trial with {n_solution_guess} solutions...")
                circ = self.circuit(
                    n, n_ancilla, oracle, n_solution_guess, True, is_bit_flip
                )
                simulator.run(circ)
                solution = int(circ[index_q])
                if check_solution(solution):
                    return solution
                n_solution_guess = int(n_solution_guess / ALPHA)
            logger.info("FAILED!")
            return None
        # no solution
        elif n_solution == 0:
            return 0
        # standard Grover's algorithm
        else:
            circ = self.circuit(n, n_ancilla, oracle, n_solution, measure, is_bit_flip)
            simulator.run(circ)
            return int(circ[index_q])
