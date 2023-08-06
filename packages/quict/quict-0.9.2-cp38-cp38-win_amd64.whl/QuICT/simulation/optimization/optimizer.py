from collections import defaultdict
import numpy as np

from QuICT.core.gate import Unitary
from QuICT.ops.linalg.cpu_calculator import multiply, dot, tensor, MatrixPermutation


class Optimizer:
    """ The quantum circuit optimizer, used to optimize the quantum circuit
    before simulation. Currently, it only working with the 1-, 2-qubits quantum
    gates.

    The rules:
        1. For the consecutive 1-qubit gates, it will be combined into a new 1-qubit Unitary
        gate.
        2. Merge the 1-qubit gates into the connected 2-qubits gate, if they have same qubit.
        3. If any 2-qubits gate has same target and control qubit indexes, and no other gates
        between them, merge its into a new 2-qubits Unitary gate.
    """
    def __init__(self):
        self._opt_gates = []    # The gates list after optimizer
        self._gates_by_qubit = defaultdict(list)    # Temporarily store the 1-qubit gates by qubits
        self._two_qubits_opt_gates_idxes_dict = {}  # Record the qubit indexes of the 2-qubits gates
        self._based_tensor_matrix = np.identity(2, dtype=np.complex128)

    def optimize(self, gates: list) -> list:
        """ Depending on the optimized rules, generate the optimized gates by the given quantum gates.

        Args:
            gates (list[Gate]): The list of gates before optimization

        Returns:
            list: The list of the optimized gates
        """
        self._cache_clear()

        for gate in gates:
            # The qubit indexes of the gate
            qubit_idxes = gate.cargs + gate.targs

            if gate.is_special():   # Do not optimized any special quantum gates
                self._1qubit_gates_clean(qubit_idxes)
                self._opt_gates.append(gate)
                continue

            if len(qubit_idxes) == 1:       # 1-qubit gate
                self._gates_by_qubit[gate.targ].append(gate)
            elif len(qubit_idxes) == 2:     # 2-qubits gate
                self.two_qubits_gates_combined(
                    gate
                )

                for idx in qubit_idxes:
                    del self._gates_by_qubit[idx]
            else:   # TODO: not support the gates with more than 2 qubits
                self._1qubit_gates_clean(qubit_idxes)
                self._opt_gates.append(gate)
                continue

        # Merge the rest 1-qubit gates into a Unitary gate.
        for qubit, gates in self._gates_by_qubit.items():
            if gates:
                self.single_gates_combined(qubit)

        return self._opt_gates

    def _cache_clear(self):
        """ Initial the Optimizer """
        self._opt_gates = []
        self._gates_by_qubit = defaultdict(list)
        self._two_qubits_opt_gates_idxes_dict = {}

    def _is_diagonal_matrix(self, matrix):
        return np.allclose(np.diag(np.diag(matrix)), matrix)

    def _1qubit_gates_clean(self, args):
        for arg in args:
            if self._gates_by_qubit[arg]:
                self.single_gates_combined(arg)
                del self._gates_by_qubit[arg]

    def _gate_combined(self, qubit_idxes: list):
        assert len(qubit_idxes) == 2
        cidx_matrix = self.single_gates_combined(qubit_idxes[0], matrix_only=True)
        tidx_matrix = self.single_gates_combined(qubit_idxes[1], matrix_only=True)

        return tensor(cidx_matrix, tidx_matrix)

    def single_gates_combined(self, qubit, matrix_only: bool = False):
        """ The optimized algorithm for 1-qubit gates with same qubit.

        Args:
            gates ([Gate]): The 1-qubit gates in the same qubit.
            matrix_only (bool, optional): return the Unitary gate or matrix. Defaults to False.

        Returns:
            (UnitaryGate, np.array): the new Unitary gate or the gate matrix
        """
        gates = self._gates_by_qubit[qubit]
        if not gates:
            return self._based_tensor_matrix

        if len(gates) == 1 and not matrix_only:
            self._opt_gates.append(gates[0])
            return

        based_matrix = gates[0].matrix
        for gate in gates[1:]:
            if self._is_diagonal_matrix(based_matrix) and gate.is_diagonal():  # Using multiply for diagonal gates
                based_matrix = multiply(gate.matrix, based_matrix)
            else:   # Using dot for non-diagonal gates
                based_matrix = dot(gate.matrix, based_matrix)

        if matrix_only:
            return based_matrix

        # Add the optimized quantum gate
        opt_gate = Unitary(based_matrix)
        opt_gate.targs = qubit
        self._opt_gates.append(opt_gate)

    def two_qubits_gates_combined(self, two_qubit_gate):
        """ The optimized algorithm for 2-qubits gates and related 1-qubit gates.

        Args:
            two_qubit_gate (Gate): The 2-qubits quantum gate
            cidx_gates (gates, None): The 1-qubit quantum gates in the control index
            tidx_gates (gates, None): The 1-qubit quantum gates in the target index
            gate_idx_bit (int): The bit-represent for the indexes of the 2-qubits quantum gate
        """
        qubit_idxes = two_qubit_gate.cargs + two_qubit_gate.targs
        gate_idx_bit = np.sum([1 << qidx for qidx in qubit_idxes])
        reverse = qubit_idxes[0] > qubit_idxes[1]

        # Combined the gate matrix of the control and target indexes into the 2-qubits gate matrix
        single_gates_combined_matrix = self._gate_combined(qubit_idxes)
        if self._is_diagonal_matrix(single_gates_combined_matrix) and two_qubit_gate.is_diagonal():
            opt_gate_matrix = multiply(two_qubit_gate.matrix, single_gates_combined_matrix)
        else:
            opt_gate_matrix = dot(two_qubit_gate.matrix, single_gates_combined_matrix)

        if reverse:
            MatrixPermutation(opt_gate_matrix, np.array([1, 0]), changeInput=True)

        # Combined the two-qubits gates
        if gate_idx_bit in self._two_qubits_opt_gates_idxes_dict.keys():
            pre_gate = self._opt_gates[self._two_qubits_opt_gates_idxes_dict[gate_idx_bit]]
            if pre_gate.is_diagonal() and self._is_diagonal_matrix(opt_gate_matrix):
                pre_gate.matrix = multiply(opt_gate_matrix, pre_gate.matrix)
            else:
                pre_gate.matrix = dot(opt_gate_matrix, pre_gate.matrix)
        else:
            overwritten_idx = \
                [idx_bit for idx_bit in self._two_qubits_opt_gates_idxes_dict.keys() if idx_bit & gate_idx_bit]
            for idx in overwritten_idx:
                del self._two_qubits_opt_gates_idxes_dict[idx]

            opt_gate = Unitary(opt_gate_matrix)
            opt_gate.targs = qubit_idxes

            self._two_qubits_opt_gates_idxes_dict[gate_idx_bit] = len(self._opt_gates)
            self._opt_gates.append(opt_gate)
