import numpy as np
import random

from QuICT.core.circuit.circuit import Circuit
from QuICT.core.gate import BasicGate, UnitaryGate, Unitary, CompositeGate
from QuICT.core.noise import NoiseModel
from QuICT.core.operator import NoiseGate
from QuICT.core.utils import GateType, matrix_product_to_circuit
import QuICT.ops.linalg.cpu_calculator as CPUCalculator
from QuICT.tools.exception.core import TypeError, ValueError
from QuICT.tools.exception.simulation import SimulationMatrixError, SampleBeforeRunError


class DensityMatrixSimulation:
    """ The Density Matrix Simulator

    Args:
        device (str, optional): The device type, one of [CPU, GPU]. Defaults to "CPU".
        precision (str, optional): The precision for the density matrix, one of [single, double]. Defaults to "double".
        accumulated_mode (bool): If True, calculated density matrix with Kraus Operators in NoiseGate.
            if True, p = \\sum Ki p Ki^T.conj(). Default to be False.
            [Important: set accumulated_mode for True if you need sample result, otherwise, using False for
            fast simulate time.]
    """
    def __init__(
        self,
        device: str = "CPU",
        precision: str = "double",
        accumulated_mode: bool = False
    ):
        self._device = device
        self._precision = np.complex128 if precision == "double" else np.complex64
        self._accumulated_mode = accumulated_mode
        self._density_matrix = None

        if device == "CPU":
            self._computer = CPUCalculator
            self._array_helper = np
        elif device == "GPU":
            import QuICT.ops.linalg.gpu_calculator as GPUCalculator
            import cupy as cp

            self._computer = GPUCalculator
            self._array_helper = cp
        else:
            raise ValueError("DensityMatrixSimulation.device", "[CPU, GPU]", device)

    def initial_circuit(self, circuit: Circuit, noise_model: NoiseModel):
        """ Initial the qubits, quantum gates and state vector by given quantum circuit. """
        self._origin_circuit = circuit
        self._circuit = circuit if noise_model is None else noise_model.transpile(circuit, self._accumulated_mode)
        self._noise_model = noise_model
        self._qubits = int(circuit.width())

        if self._precision != circuit._precision:
            circuit.convert_precision()

    def initial_density_matrix(self, qubits: int):
        """ Initial density matrix by given qubits number.

        Args:
            qubits (int): the number of qubits.
        """
        self._density_matrix = self._array_helper.zeros((1 << qubits, 1 << qubits), dtype=self._precision)
        if self._device == "CPU":
            self._density_matrix[0, 0] = self._precision(1)
        else:
            self._density_matrix.put((0, 0), self._precision(1))

    def check_matrix(self, matrix):
        """ Density Matrix Validation. """
        if not np.allclose(matrix.T.conjugate(), matrix):
            raise SimulationMatrixError("The conjugate transpose of density matrix do not equal to itself.")

        if not isinstance(matrix, np.ndarray):
            matrix = matrix.get()

        eigenvalues = np.linalg.eig(matrix)[0]
        for ev in eigenvalues:
            if ev < 0 and not np.isclose(ev, 0, rtol=1e-4):
                raise SimulationMatrixError("The eigenvalues of density matrix should be non-negative")

        if not np.isclose(matrix.trace(), 1, rtol=1e-4):
            raise SimulationMatrixError("The sum of trace of density matrix should be 1.")

        return True

    def run(
        self,
        circuit: Circuit,
        density_matrix: np.ndarray = None,
        noise_model: NoiseModel = None,
        use_previous: bool = False
    ) -> np.ndarray:
        """ Simulating the given circuit through density matrix simulator.

        Args:
            circuit (Circuit): The quantum circuit.
            density_matrix (np.ndarray): The initial density matrix.
            noise_model (NoiseModel, optional): The NoiseModel contains NoiseErrors. Defaults to None.
            use_previous (bool, optional): Using the previous state vector. Defaults to False.

        Returns:
            np.ndarray: the density matrix after simulating
        """
        self.initial_circuit(circuit, noise_model)
        # Initial density matrix
        if density_matrix is not None:
            self.check_matrix(density_matrix)
            self._density_matrix = self._array_helper.array(density_matrix, dtype=self._precision)
        elif (self._density_matrix is None or not use_previous):
            self.initial_density_matrix(self._qubits)

        self._run(self._circuit)

        # Check Readout Error in the NoiseModel
        if noise_model is not None:
            noise_model.apply_readout_error(circuit.qubits)

        return self._density_matrix

    def _run(self, noised_circuit):
        # Start simulator
        cgate = CompositeGate()
        cgate._max_qubit = self._qubits
        for gate in noised_circuit.gates:
            # Store continuous BasicGates into cgate
            if isinstance(gate, BasicGate) and gate.type != GateType.measure:
                gate | cgate
                continue

            if cgate.size() > 0:
                self.apply_gates(cgate)
                cgate.clean()
                cgate._max_qubit = self._qubits

            if gate.type == GateType.measure:
                self.apply_measure(gate.targ)
            elif isinstance(gate, NoiseGate):
                self.apply_noise(gate, self._qubits)
            else:
                raise TypeError("DensityMatrixSimulation.run.circuit", "[BasicGate, NoiseGate]", type(gate))

        if cgate.size() > 0:
            self.apply_gates(cgate)

    def apply_gates(self, cgate: CompositeGate):
        """ Simulating Circuit with BasicGates

        dm = M*dm(M.conj)^T

        Args:
            cgate (CompositeGate): The CompositeGate.
        """
        cgate_matrix = cgate.matrix(self._device)
        self._density_matrix = self._computer.dot(
            self._computer.dot(cgate_matrix, self._density_matrix),
            cgate_matrix.conj().T
        )

    def apply_noise(self, noise_gate: NoiseGate, qubits: int):
        """ Simulating NoiseGate.

        dm = /sum K*dm*(K.conj)^T

        Args:
            noise_gate (NoiseGate): The NoiseGate
            qubits (int): The number of qubits in the circuit.
        """
        gate_args = noise_gate.targs
        noised_matrix = self._array_helper.zeros_like(self._density_matrix)
        for kraus_matrix in noise_gate.noise_matrix:
            umat = matrix_product_to_circuit(kraus_matrix, gate_args, qubits, gpu_output=self._device == "GPU")

            noised_matrix += self._computer.dot(
                self._computer.dot(umat, self._density_matrix),
                umat.conj().T
            )

        self._density_matrix = noised_matrix.copy()

    def apply_measure(self, index: int):
        """ Simulating the MeasureGate.

        Args:
            index (int): The index of measured qubit.
        """
        P0 = self._array_helper.array([[1, 0], [0, 0]], dtype=self._precision)
        mea_0 = matrix_product_to_circuit(P0, index, self._qubits, gpu_output=self._device == "GPU")
        prob_0 = self._array_helper.matmul(mea_0, self._density_matrix).trace()
        _1 = random.random() > prob_0
        if not _1:
            U = self._array_helper.matmul(
                mea_0,
                self._array_helper.eye(1 << self._qubits, dtype=self._precision) / self._array_helper.sqrt(prob_0)
            )
            self._density_matrix = self._computer.dot(self._computer.dot(U, self._density_matrix), U.conj().T)
        else:
            P1 = self._array_helper.array([[0, 0], [0, 1]], dtype=self._precision)
            mea_1 = matrix_product_to_circuit(P1, index, self._qubits, gpu_output=self._device == "GPU")

            U = self._array_helper.matmul(
                mea_1,
                self._array_helper.eye(1 << self._qubits, dtype=self._precision) / self._array_helper.sqrt(1 - prob_0)
            )
            self._density_matrix = self._computer.dot(self._computer.dot(U, self._density_matrix), U.conj().T)

        self._circuit.qubits[index].measured = int(_1)

    def sample(self, shots: int) -> list:
        assert (self._density_matrix is not None), \
            SampleBeforeRunError("DensityMatrixSimulation sample without run any circuit.")
        if self._accumulated_mode or self._noise_model is None:
            original_dm = self._density_matrix.copy()

        state_list = [0] * self._density_matrix.shape[0]
        lastcall_per_qubit = self._circuit.get_lastcall_for_each_qubits()
        measured_idx = [
            i for i in range(self._qubits)
            if lastcall_per_qubit[i] != GateType.measure
        ]

        for _ in range(shots):
            for m_id in measured_idx:
                self.apply_measure(m_id)

            if self._noise_model is not None:
                self._noise_model.apply_readout_error(self._circuit.qubits)

            state_list[int(self._circuit.qubits)] += 1
            if self._accumulated_mode or self._noise_model is None:
                self._density_matrix = original_dm.copy()
            else:
                self.initial_density_matrix(self._qubits)
                noised_circuit = self._noise_model.transpile(self._origin_circuit, self._accumulated_mode) \
                    if self._noise_model is not None else self._circuit

                self._run(noised_circuit)

        return state_list
