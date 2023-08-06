from typing import *
import numpy as np

from QuICT.core import *
from QuICT.core.gate import *
from QuICT.core.gate.backend import UniformlyRotation
from .utility import *


class ControlledUnitaryDecomposition(object):
    def __init__(self, include_phase_gate: bool = True, recursive_basis: int = 2):
        """
        Args:
            include_phase_gate(bool): Whether to include a phase gate to keep synthesized gate matrix the same
                as input. If set False, the output gates might have a matrix which has a factor shift to input:
                np.allclose(<matrix_of_return_gates> * factor, <input_matrix>).
            recursive_basis(int): Terminate recursion at which level. It could be set as 1 or 2, which would stop
                recursion when matrix is 2 or 4, respectively. When set as 2, the final step is done by KAK
                decomposition.
                Correctness of this algorithm is never influenced by recursive_basis.
        """
        self.include_phase_gate = include_phase_gate
        self.recursive_basis = recursive_basis

    def execute(self, u1: np.ndarray, u2: np.ndarray):
        """
        Transform a controlled-unitary matrix into CX gates and single qubit gates.
        A controlled-unitary is a block-diagonal unitary. Parameter u1 and u2 are
        the block diagonals.

        Args:
            u1(np.ndarray): Upper-left block diagonal.
            u2(np.ndarray): bottom-right block diagonal.
            include_phase_gate(bool): Whether to include a phase gate to keep synthesized gate matrix the same
                as input. If set False, the output gates might have a matrix which has a factor shift to input:
                np.allclose(<matrix_of_return_gates> * factor, <input_matrix>).
            mapping(List[int]): The order of input qubits. Mapping is a list of their labels from top to bottom.
            recursive_basis(int): Terminate recursion at which level. It could be set as 1 or 2, which would stop
                recursion when matrix is 2 or 4, respectively. When set as 2, the final step is done by KAK
                decomposition.
                Correctness of this algorithm is never influenced by recursive_basis.

        Returns:
            Union[Tuple[CompositeGate,None], Tuple[CompositeGate,complex]]: If inlclude_phase_gate==False,
                this function returns synthesized gates and a shift factor. Otherwise a tuple like (<gates>, None)
                is returned.
        """
        gates, shift = self.inner_cutrans_build_gate(u1, u2, self.recursive_basis)
        if self.include_phase_gate:
            gates = add_factor_shift_into_phase(gates, shift)
            return gates, None
        else:
            return gates, shift

    def _i_tensor_unitary(
        self,
        u: np.ndarray,
        recursive_basis: int,
        keep_left_diagonal: bool = False,
    ) -> Tuple[CompositeGate, complex]:
        """
        Transform (I_{2x2} tensor U) into gates. The 1st bit
        is under the identity transform.

        Args:
            u (np.ndarray): A unitary matrix.

        Returns:
            Tuple[CompositeGate, complex]: Synthesized gates and a phase factor.
        """

        gates: CompositeGate
        shift: complex
        # Dynamically import to avoid circulation.
        from .unitary_decomposition import UnitaryDecomposition
        UD = UnitaryDecomposition()
        gates, shift = UD.inner_utrans_build_gate(
            mat=u,
            recursive_basis=recursive_basis,
            keep_left_diagonal=keep_left_diagonal,
        )
        for gate in gates:
            for idx, _ in enumerate(gate.cargs):
                gate.cargs[idx] += 1
            for idx, _ in enumerate(gate.targs):
                gate.targs[idx] += 1

        return gates, shift

    def inner_cutrans_build_gate(
        self,
        u1: np.ndarray,
        u2: np.ndarray,
        recursive_basis: int = 2,
        keep_left_diagonal: bool = False,
    ) -> Tuple[CompositeGate, complex]:
        """
        Build gates from parameterized model without mapping

        Returns:
            Tuple[CompositeGate, complex]: Synthesized gates and factor shift.
        """
        qubit_num = 1 + int(round(np.log2(u1.shape[0])))
        v, d, w = quantum_shannon_decompose(u1, u2)
        shift: complex = 1.0

        # diag(u1, u2) == diag(v, v) @ diag(d, d_dagger) @ diag(w, w)
        # diag(v, v)
        v_gates, _shift = self._i_tensor_unitary(v, recursive_basis, keep_left_diagonal=True)
        shift *= _shift

        # diag(d, d_dagger)
        angle_list = []
        for i in range(d.shape[0]):
            s = d[i, i]
            theta = -2 * np.log(s) / 1j
            angle_list.append(theta)

        URz = UniformlyRotation(GateType.rz)
        reversed_rz = URz.execute(angle_list)
        reversed_rz & [(i + 1) % qubit_num for i in range(qubit_num)]

        # diag(w, w)
        if recursive_basis == 2:
            forwarded_d_gate: BasicGate = v_gates.gates.pop(0)
            forwarded_mat = forwarded_d_gate.matrix
            for i in range(0, w.shape[0], 4):
                for k in range(4):
                    w[i + k, :] *= forwarded_mat[k, k]

        w_gates, _shift = self._i_tensor_unitary(w, recursive_basis, keep_left_diagonal=keep_left_diagonal)
        shift *= _shift

        gates = CompositeGate()
        gates.extend(w_gates)
        gates.extend(reversed_rz)
        gates.extend(v_gates)

        return gates, shift
