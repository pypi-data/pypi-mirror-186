from typing import *
from collections import namedtuple
import numpy as np

from .gate_type import MatrixType
import QuICT.ops.linalg.cpu_calculator as CPUCalculator

from QuICT.tools.exception.core import TypeError


def get_gates_order_by_depth(gates: list) -> list:
    """ Order the gates of circuit by its depth layer

    Returns:
        List[List[BasicGate]]: The list of gates which at same layers in circuit.
    """
    gate_by_depth = [[gates[0]]]          # List[list], gates for each depth level.
    # List[set], gates' qubits for each depth level.
    gate_args_by_depth = [set(gates[0].cargs + gates[0].targs)]
    for gate in gates[1:]:
        gate_arg = set(gate.cargs + gate.targs)
        for i in range(len(gate_args_by_depth) - 1, -1, -1):
            if gate_arg & gate_args_by_depth[i]:
                if i == len(gate_args_by_depth) - 1:
                    gate_by_depth.append([gate])
                    gate_args_by_depth.append(gate_arg)
                else:
                    gate_by_depth[i + 1].append(gate)
                    gate_args_by_depth[i + 1] = gate_arg | gate_args_by_depth[i + 1]
                break
            else:
                if i == 0:
                    gate_by_depth[i].append(gate)
                    gate_args_by_depth[i] = gate_arg | gate_args_by_depth[i]

    return gate_by_depth


class MatrixGroup:
    def __init__(self, matrix, args, blocked_args: set = set([])):
        self.args = set(args)
        self.value = [(matrix, args)]
        self.block_args = blocked_args

    def append(self, matrix, args):
        self.args = self.args | set(args)
        self.value.append((matrix, args))

    def intersect(self, args: list):
        intersect_qubits = list(set(args) & self.args)
        blocked_qubits = list(set(args) & self.block_args)

        return intersect_qubits, blocked_qubits


class CircuitMatrix:
    def __init__(self, device: str = "CPU"):
        self._device = device
        if device == "CPU":
            self._computer = CPUCalculator
            self._array_helper = np
        else:
            import cupy as cp
            import QuICT.ops.linalg.gpu_calculator as GPUCalculator

            self._computer = GPUCalculator
            self._array_helper = cp

    def get_unitary_matrix(self, gates: list, qubits_num: int, mini_arg: int = 0) -> np.ndarray:
        # Order gates by depth
        gates_order_by_depth = get_gates_order_by_depth(gates)

        # Get MatrixGroups by its qubit args and depth
        matrix_groups = [[]]          # List[List[MatrixGroup]]
        for layer_gates in gates_order_by_depth:
            for gate in layer_gates:
                if gate.controls + gate.targets >= 3:
                    raise TypeError(
                        "CircuitMatrix.get_unitary_matrix.gates", "1 or 2-qubits gates", gate.controls + gate.targets
                    )

                if gate.matrix_type == MatrixType.special:
                    continue

                args = gate.cargs + gate.targs
                matrix = gate.matrix if self._device == "CPU" else self._array_helper.array(gate.matrix)
                if len(args) == 2 and args[0] > args[1]:
                    args.sort()
                    matrix = self._computer.MatrixPermutation(matrix, self._array_helper.array([1, 0]))

                is_intersect, is_blocked_layer = self._find_related_MatrixGroup(matrix_groups, args)
                if not is_intersect:
                    new_mg = MatrixGroup(matrix, args)
                    matrix_groups[is_blocked_layer].append(new_mg)
                else:
                    if len(is_intersect) == 2:
                        related_mg0, related_mg1 = is_intersect[0], is_intersect[1]
                        if related_mg0.position == related_mg1.position:
                            matrix_groups[related_mg0.layer][related_mg0.position].append(matrix, args)
                        else:
                            blocked_args = matrix_groups[related_mg0.layer][related_mg0.position].args | \
                                matrix_groups[related_mg1.layer][related_mg1.position].args
                            new_mg = MatrixGroup(matrix, args, blocked_args)
                            if related_mg0.layer == len(matrix_groups) - 1:
                                matrix_groups.append([new_mg])
                            else:
                                matrix_groups[related_mg0.layer + 1].append(new_mg)
                    else:
                        intersect_info = is_intersect[0]
                        matrix_groups[intersect_info.layer][intersect_info.position].append(matrix, args)

        # Combined the matries in each MatrixGroup
        combined_matries = []
        for layer in matrix_groups:
            for mg in layer:
                combined_matries.append(self._combined_gates(mg.value))

        # Combined all matries from the combined MatrixGroup
        circuit_matrix, circuit_matrix_args = self._combined_gates(combined_matries)
        # Permutation the circuit matrix with currect qubits' order
        args_baseline = list(range(mini_arg, qubits_num, 1))
        if circuit_matrix_args != args_baseline:
            circuit_matrix = self._tensor_unitary(circuit_matrix, circuit_matrix_args, args_baseline)

        return circuit_matrix

    def _find_related_MatrixGroup(self, matrix_groups: list, args: list):
        intersect_info = namedtuple('IntersectInfo', ['arg', 'layer', 'position'])
        is_blocked = 0
        is_intersect = []
        for lidx in range(len(matrix_groups) - 1, -1, -1):
            layer = matrix_groups[lidx]
            for midx, mg in enumerate(layer):
                iq, bq = mg.intersect(args)
                if len(iq) > 0:
                    for idx in iq:
                        inter_info = intersect_info(idx, lidx, midx)
                        is_intersect.append(inter_info)

                if len(bq) > 0:
                    is_blocked = lidx

            if len(is_intersect) > 0:
                return is_intersect, False

            if is_blocked:
                break

        return is_intersect, is_blocked

    def merge_gates(self, u1, u1_args, u2, u2_args):
        u1_args_set, u2_args_set = set(u1_args), set(u2_args)
        insection_args = u1_args_set & u2_args_set
        if len(insection_args) == 0:
            return self._computer.tensor(u1, u2), u1_args + u2_args

        if u1_args_set == u2_args_set:
            args_idx = [u1_args.index(u2_arg) for u2_arg in u2_args]
            u2 = self._computer.MatrixPermutation(
                u2,
                self._array_helper.array(args_idx)
            )

        union_args = u1_args + [i for i in u2_args if i not in u1_args] if len(u1_args) >= len(u2_args) else \
            u2_args + [i for i in u1_args if i not in u2_args]
        if len(union_args) != len(u1_args_set):
            u1 = self._tensor_unitary(u1, u1_args, union_args)

        if len(union_args) != len(u2_args_set):
            u2 = self._tensor_unitary(u2, u2_args, union_args)

        return self._computer.dot(u2, u1), union_args

    def _tensor_unitary(self, unitary, unitary_args, extend_args):
        uargs_idx = [extend_args.index(uarg) for uarg in unitary_args]
        mono_diff = np.diff(uargs_idx)
        if np.allclose(abs(mono_diff), 1):
            if np.allclose(mono_diff, -1):
                unitary = self._computer.MatrixPermutation(
                    unitary,
                    self._array_helper.arange(len(unitary_args) - 1, -1, -1)
                )

            return self._computer.MatrixTensorI(
                unitary,
                1 << (min(uargs_idx) - 0),
                1 << (len(extend_args) - 1 - max(uargs_idx))
            )

        tensor_matrix = self._computer.MatrixTensorI(
            unitary,
            1,
            1 << (len(extend_args) - len(unitary_args))
        )
        tmatrix_args = unitary_args + [earg for earg in extend_args if earg not in unitary_args]
        permutation_index = [extend_args.index(tm_arg) for tm_arg in tmatrix_args]

        return self._computer.MatrixPermutation(tensor_matrix, self._array_helper.array(permutation_index))

    def _combined_gates(self, gates):
        args_num = [len(args) for _, args in gates]
        while len(args_num) > 1:
            left, right = self._find_mini_args_num(args_num)
            lg, rg = gates[left], gates[right]
            combined_matrix, combined_matrix_args = self.merge_gates(
                lg[0], lg[1],
                rg[0], rg[1]
            )
            gates[left] = (combined_matrix, combined_matrix_args)
            del gates[right]

            args_num[left] += args_num[right]
            del args_num[right]

        return gates[0]

    def _find_mini_args_num(self, nums: list):
        mini_num = sum(nums) * 2
        left, right = -1, -1
        for i in range(1, len(nums), 1):
            if nums[i] + nums[i - 1] < mini_num:
                left = i - 1
                right = i
                mini_num = nums[i] + nums[i - 1]

        return left, right
