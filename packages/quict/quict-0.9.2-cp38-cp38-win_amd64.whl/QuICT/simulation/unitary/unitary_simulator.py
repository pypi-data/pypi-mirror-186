from typing import *
import numpy as np

from QuICT.core import Circuit
import QuICT.ops.linalg.cpu_calculator as CPUCalculator
from QuICT.tools.exception.core import ValueError
from QuICT.tools.exception.simulation import (
    UnitaryMatrixUnmatchedError, StateVectorUnmatchedError, SampleBeforeRunError
)


class UnitarySimulator():
    """ Algorithms to calculate the unitary matrix of a quantum circuit, and simulate.

    Args:
        device (str, optional): The device type, one of [CPU, GPU]. Defaults to "CPU".
        precision (str, optional): The precision for the unitary matrix, one of [single, double]. Defaults to "double".
    """
    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, vec):
        self._vector = self._array_helper.array(vec)

    def __init__(
        self,
        device: str = "CPU",
        precision: str = "double"
    ):
        self._device = device
        self._precision = np.complex128 if precision == "double" else np.complex64
        self._vector = None
        self._circuit = None

        if device == "CPU":
            self._computer = CPUCalculator
            self._array_helper = np
        elif device == "GPU":
            import cupy as cp
            import QuICT.ops.linalg.gpu_calculator as GPUCalculator

            self._computer = GPUCalculator
            self._array_helper = cp
        else:
            raise ValueError("UnitarySimulation.device", "[CPU, GPU]", device)

    def initial_vector_state(self):
        """ Initial the state vector for simulation through UnitarySimulator,
        must after initial_circuit
        """
        self._vector = self._array_helper.zeros(1 << self._qubits_num, dtype=self._precision)
        if self._device == "CPU":
            self._vector[0] = self._precision(1)
        else:
            self._vector.put(0, self._precision(1))

    def run(
        self,
        circuit: Union[np.ndarray, Circuit],
        state_vector: np.ndarray = None,
        use_previous: bool = False
    ) -> np.ndarray:
        """ Simulation by given unitary matrix or circuit

        Args:
            circuit (Union[np.ndarray, Circuit]): The unitary matrix or the circuit for simulation
            state_vector (ndarray): The initial state vector.
            use_previous (bool, optional): whether using previous state vector. Defaults to False.

        Returns:
            np.ndarray: The state vector after simulation
        """
        # Step 1: Generate the unitary matrix of the given circuit
        if isinstance(circuit, Circuit):
            if self._precision != circuit._precision:
                circuit.convert_precision()

            self._qubits_num = circuit.width()
            self._unitary_matrix = circuit.matrix(self._device)
            assert 2 ** self._qubits_num == self._unitary_matrix.shape[0], \
                UnitaryMatrixUnmatchedError("The unitary matrix should has the same qubits with the circuit.")
        else:
            row, col = circuit.shape
            self._qubits_num = int(np.log2(row))
            assert row == col and 2 ** self._qubits_num == col, \
                UnitaryMatrixUnmatchedError("The unitary matrix should be square.")
            self._unitary_matrix = self._array_helper.array(circuit, dtype=self._precision)

        # Step 2: Prepare the state vector
        if state_vector is not None:
            assert 2 ** self._qubits_num == state_vector.size, \
                StateVectorUnmatchedError("The state vector should has the same qubits with the circuit.")
            self.vector = self._array_helper.array(state_vector, dtype=self._precision)
        elif not use_previous or self._vector is None:
            self.initial_vector_state()

        # Step 3: Simulation with the unitary matrix and qubit's state vector
        if not self._is_identity():
            self._vector = self._computer.dot(
                self._unitary_matrix,
                self._vector
            )

        return self._vector

    def _is_identity(self):
        identity_matrix = self._array_helper.identity(1 << self._qubits_num, dtype=self._precision)
        return self._array_helper.allclose(self._unitary_matrix, identity_matrix)

    def sample(self, shots: int):
        """_summary_

        Args:
            shots (int): _description_

        Returns:
            _type_: _description_
        """
        assert (self._vector is not None), \
            SampleBeforeRunError("UnitarySimulation sample without run any circuit.")

        original_sv = self._vector.copy()
        counts = [0] * (1 << self._qubits_num)
        for _ in range(shots):
            measured_result = 0
            for i in range(self._qubits_num):
                measured_result <<= 1
                measured_result += self._measure(i)

            counts[measured_result] += 1
            self._vector = original_sv.copy()

        return counts

    def _measure(self, index):
        if self._device == "CPU":
            result = self._computer.measure_gate_apply(
                index,
                self._vector
            )
        else:
            from QuICT.ops.gate_kernel import apply_measuregate, measured_prob_calculate
            prob = measured_prob_calculate(
                index,
                self._vector,
                self._qubits_num
            )
            result = apply_measuregate(
                index,
                self._vector,
                self._qubits_num,
                prob=prob.get()
            )

        return int(result)
