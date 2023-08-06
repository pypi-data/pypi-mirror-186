import copy

import numpy as np
import torch

from QuICT.algorithm.quantum_machine_learning.utils import Ansatz
from QuICT.algorithm.quantum_machine_learning.utils.gate_tensor import *
from QuICT.core import Circuit
from QuICT.core.gate import *


class Hamiltonian:
    """The Hamiltonian class."""

    @property
    def pauli_str(self):
        """The coefficient of each term in the Hamiltonian, i.e. [0.4, 0.6]."""
        return self._pauli_str

    @property
    def coefficients(self):
        """The coefficient of each term in the Hamiltonian, i.e. [0.4, 0.6]."""
        return self._coefficients

    @property
    def pauli_gates(self):
        """The Pauli gate of each term in the Hamiltonian, i.e. ["YXZ", ""]."""
        return self._pauli_gates

    @property
    def qubit_indexes(self):
        """The target bit of the Pauli gate of each term in the Hamiltonian, i.e. [[012], []]."""
        return self._qubit_indexes

    def __init__(self, pauli_str: list):
        """Instantiate the Hamiltonian class with a Pauli string.

        Args:
            pauli_str (list): A list of Hamiltonian information.

            Some Examples are like this:

            [[0.4, 'Y0', 'X1', 'Z2', 'I5'], [0.6]]
            [[1, 'X0', 'I5'], [-3, 'Y3'], [0.01, 'Z5', 'Y0]]

            *Important*: Coefficients are required. And each Pauli Gate should act on different qubit.
        """
        self._pauli_str = pauli_str
        self._remove_I()
        self._coefficients = []
        self._pauli_gates = []
        self._qubit_indexes = []
        self._pauli_str_validation()

    def __getitem__(self, indexes):
        pauli_str = []
        if isinstance(indexes, int):
            indexes = [indexes]
        for idx in indexes:
            pauli_str.append(self._pauli_str[idx])
        return Hamiltonian(pauli_str)

    def __add__(self, other):
        """Concatenate two Pauli Strings."""
        return Hamiltonian(self._pauli_str + other._pauli_str)

    def __sub__(self, other):
        """Concatenate two Pauli strings after the coefficients of the subtrahend term become the opposite."""
        return self.__add__(other.__mul__(-1))

    def __mul__(self, other: float):
        """Multiply all coefficients of the Pauli string by a float."""
        new_pauli_str = copy.deepcopy(self.pauli_str)
        for pauli_operator in new_pauli_str:
            pauli_operator[0] *= other
        return Hamiltonian(new_pauli_str)

    def _remove_I(self):
        new_pauli_str = []
        for pauli_operator in self._pauli_str:
            assert isinstance(pauli_operator[0], float)
            for pauli_gate in pauli_operator[1:][::-1]:
                if "I" in pauli_gate:
                    pauli_operator.remove(pauli_gate)
            new_pauli_str.append(pauli_operator)

        self._pauli_str = new_pauli_str

    def get_hamiton_matrix(self, n_qubits):
        """Construct a matrix form of the Hamiltonian.

        Args:
            n_qubits (int): The number of qubits.

        Returns:
            np.array: The Hamiltonian matrix.
        """
        hamiton_matrix = np.zeros((1 << n_qubits, 1 << n_qubits), dtype=np.complex128)
        hamiton_circuits = self.construct_hamiton_circuit(n_qubits)
        for coeff, circuit in zip(self._coefficients, hamiton_circuits):
            hamiton_matrix += coeff * circuit.matrix()

        return hamiton_matrix

    def construct_hamiton_circuit(self, n_qubits):
        """Construct a circuit form of the Hamiltonian.

        Args:
            n_qubits (int): The number of qubits.

        Returns:
            list<Circuit>: A list of circuits corresponding to the Hamiltonian.
        """
        hamiton_circuits = []
        gate_dict = {"X": X, "Y": Y, "Z": Z}
        for qubit_index, pauli_gate in zip(self._qubit_indexes, self._pauli_gates):
            circuit = Circuit(n_qubits)
            for qid, gate in zip(qubit_index, pauli_gate):
                assert gate in gate_dict.keys(), "Invalid Pauli gate."
                gate_dict[gate] | circuit(qid)
            hamiton_circuits.append(circuit)
        return hamiton_circuits

    def construct_hamiton_ansatz(self, n_qubits, device=torch.device("cuda:0")):
        """Construct an ansatz form of the Hamiltonian.

        Args:
            n_qubits (int): The number of qubits.

        Returns:
            list<Ansatz>: A list of ansatz corresponding to the Hamiltonian.
        """
        hamiton_ansatz = []
        gate_dict = {"X": X_tensor, "Y": Y_tensor, "Z": Z_tensor}
        for qubit_index, pauli_gate in zip(self._qubit_indexes, self._pauli_gates):
            ansatz = Ansatz(n_qubits, device=device)
            for qid, gate in zip(qubit_index, pauli_gate):
                assert gate in gate_dict.keys(), "Invalid Pauli gate."
                ansatz.add_gate(gate_dict[gate], qid)
            hamiton_ansatz.append(ansatz)
        return hamiton_ansatz

    def _pauli_str_validation(self):
        """Validate the Pauli string."""
        for pauli_operator in self._pauli_str:
            self._pauli_operator_validation(pauli_operator)

    def _pauli_operator_validation(self, pauli_operator):
        """Validate the Pauli operator."""
        assert isinstance(pauli_operator[0], int) or isinstance(
            pauli_operator[0], float
        ), "A Pauli operator must contain a coefficient, which must be integer or float."

        indexes = []
        pauli_gates = ""
        for pauli_gate in pauli_operator[1:]:
            pauli_gate = pauli_gate.upper()
            assert (
                pauli_gate[0] in ["X", "Y", "Z", "I"] and pauli_gate[1:].isdigit()
            ), "The Pauli gate should be in the format of Pauli gate + qubit index. e.g. Z0, I5, Y3."
            pauli_gates += pauli_gate[0]
            indexes.append(int(pauli_gate[1:]))
        assert len(indexes) == len(
            set(indexes)
        ), "Each Pauli Gate should act on different qubit."

        self._coefficients.append(float(pauli_operator[0]))
        self._qubit_indexes.append(indexes)
        self._pauli_gates.append(pauli_gates)
