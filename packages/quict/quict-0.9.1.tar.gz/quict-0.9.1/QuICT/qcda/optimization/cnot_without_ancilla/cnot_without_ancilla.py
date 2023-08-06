from typing import *

import numpy as np

from QuICT.core import *
from QuICT.core.gate import build_gate, BasicGate, CompositeGate, GateType
from QuICT.qcda.utility import OutputAligner
from .utility import *
from .graph import *
from .edge_coloring import EdgeColoring
from .block_ldu_decompose import BlockLDUDecompose


class CnotWithoutAncilla(object):
    @OutputAligner()
    def execute(
            self,
            circuit_segment: Union[Circuit, CompositeGate]
    ) -> CompositeGate:
        if isinstance(circuit_segment, Circuit):
            gates = circuit_segment.gates
            n = len(circuit_segment.qubits)
        elif isinstance(circuit_segment, CompositeGate):
            gates = circuit_segment
            n = circuit_segment.circuit_width()
        else:
            raise Exception("Only accept Circuit/CompositeGate!")

        mat = np.eye(n, dtype=bool)
        for gate in gates:
            gate: BasicGate
            c = gate.carg
            t = gate.targ
            mat[t, :] ^= mat[c, :]

        composite_gate = CompositeGate()

        parallel_elimination = self.matrix_run(mat)
        parallel_elimination.reverse()
        for level in parallel_elimination:
            for c, t in level:
                _cx = build_gate(GateType.cx, [c, t])
                composite_gate.append(_cx)
        return composite_gate

    @classmethod
    def matrix_run(cls, mat: np.ndarray) \
            -> List[List[Tuple[int, int]]]:
        """
        Get parallel row elimination of a boolean invertible matrix.

        Args:
            mat (np.ndarray): A boolean invertible matrix

        Returns:
            List[List[Tuple[int,int]]]: Parallel row elimination. In each depth level there are
            non-overlapping row eliminations.
        """
        if len(mat.shape) != 2 or mat.shape[0] != mat.shape[1]:
            raise Exception("Must use a square matrix!")
        if mat.dtype != bool:
            raise Exception("Must use a boolean matrix!")

        return cls.__matrix_run(mat)

    @classmethod
    def small_matrix_run(cls, mat: np.ndarray) \
            -> List[List[Tuple[int, int]]]:
        n = mat.shape[0]
        if n == 1:
            return [[]]
        elif n == 2:
            # Enumerate
            if np.allclose(
                    mat,
                    np.array([
                        [1, 0],
                        [0, 1]
                    ], dtype=bool)
            ):  # :(
                return [[]]
            elif np.allclose(
                    mat,
                    np.array([
                        [1, 0],
                        [1, 1]
                    ], dtype=bool)
            ):  # :P
                return [[(0, 1)]]
            elif np.allclose(
                    mat,
                    np.array([
                        [0, 1],
                        [1, 0]
                    ], dtype=bool)
            ):  # :b
                return [[(0, 1)], [(1, 0)], [(0, 1)]]
            elif np.allclose(
                    mat,
                    np.array([
                        [0, 1],
                        [1, 1]
                    ], dtype=bool)
            ):  # :D
                return [[(1, 0)], [(0, 1)]]
            elif np.allclose(
                    mat,
                    np.array([
                        [1, 1],
                        [0, 1]
                    ], dtype=bool)
            ):  # :X
                return [[(1, 0)]]
            elif np.allclose(
                    mat,
                    np.array([
                        [1, 1],
                        [1, 0]
                    ], dtype=bool)
            ):  # :O
                return [[(0, 1)], [(1, 0)]]
        else:
            raise Exception("Must use matrix size <= 2.")

    @classmethod
    def __matrix_run(cls, mat: np.ndarray) \
            -> List[List[Tuple[int, int]]]:
        """
        Get parallel row elimination of a boolean invertible matrix.
        No shape & data type checks for inner methods.

        Args:
            mat (np.ndarray): A boolean invertible matrix

        Returns:
            List[List[Tuple[int,int]]]: Parallel row elimination. In each depth level there are
            non-overlapping row eliminations.
        """

        n = mat.shape[0]

        if n <= 2:
            return cls.small_matrix_run(mat)

        l_, d_, u_, remapping = BlockLDUDecompose.run(mat)

        # Implement remapping using swap operations(3-depth CNOT).

        """
        Notes:
        P @ M == L @ D @ U, where P == P^{-1}.
        So, M == P @ L @ D @ U. We sequentially eliminate P, L, D, U.
        If we reverse the eliminations' order to get a row transform sequence,
        changing an I into M, then that is exactly what we need for CNOT circuit.

        """

        parallel_elimination: List[List[Tuple[int, int]]] = []

        r_p_e = cls.remapping_run(remapping)
        parallel_elimination.extend(r_p_e)

        l_p_e = cls.triangular_matrix_run(l_, is_lower_triangular=True)
        if l_p_e != [[]]:
            parallel_elimination.extend(l_p_e)

        d_p_e = cls.block_diagonal_matrix_run(d_)
        if d_p_e != [[]]:
            parallel_elimination.extend(d_p_e)

        u_p_e = cls.triangular_matrix_run(u_, is_lower_triangular=False)
        if u_p_e != [[]]:
            parallel_elimination.extend(u_p_e)

        return parallel_elimination

    @classmethod
    def triangular_matrix_run(cls, mat: np.ndarray, is_lower_triangular: bool) \
            -> List[List[Tuple[int, int]]]:
        """
        Get parallel row elimination of a triangular matrix by bipartite edge coloring.


        Args:
            mat (np.ndarray): A triangular boolean matrix with block identity diagonal entries.
            is_lower_triangular (bool): Is the input triangular matrix has all its non-zero
                entries in lower part. If this parameter is false, all non-zero entries should
                be located in upper part.

        Returns:
            List[List[Tuple[int,int]]]: Parallel row elimination. In each depth level there are
            non-overlapping row eliminations.
        """
        n = mat.shape[0]
        s_size = n // 2
        t_size = n - s_size

        # Always use the identity sub matrix as the `left` in bipartite
        if is_lower_triangular:
            left = [i for i in range(s_size)]
            right = [i + s_size for i in range(t_size)]
        else:
            left = [i for i in range(t_size)]
            right = [i + t_size for i in range(s_size)]

        # Construct bipartite
        bipartite = Bipartite(left, right)
        # Add edges
        if is_lower_triangular:
            for j in range(s_size):
                for i in range(s_size, n):
                    if mat[i, j]:
                        bipartite.add_edge(j, i)
                        bipartite.add_edge(i, j)
        else:
            for j in range(s_size, n):
                for i in range(s_size):
                    if mat[i, j]:
                        bipartite.add_edge(j - s_size, i + t_size)
                        bipartite.add_edge(i + t_size, j - s_size)

        colored_bipartite = EdgeColoring.get_edge_coloring(bipartite)
        max_deg = colored_bipartite.get_max_degree()
        parallel_elimination: List[List[Tuple[int, int]]] = [[] for _ in range(max_deg)]

        # Iterate over left vertices to check edges with the same color
        for node in colored_bipartite.left:
            eid = colored_bipartite.head[node]
            while eid != -1:
                edge = colored_bipartite.edges[eid]
                color_index = edge.color
                if is_lower_triangular:
                    c = edge.start
                    t = edge.end
                else:
                    c = edge.start + s_size
                    t = edge.end - t_size
                row_elimination = (c, t)
                parallel_elimination[color_index].append(row_elimination)
                eid = edge.next

        return parallel_elimination

    @classmethod
    def block_diagonal_matrix_run(cls, mat: np.ndarray) \
            -> List[List[Tuple[int, int]]]:
        """
        Get parallel row elimination of a block diagonal matrix by bipartite edge coloring.


        Args:
            mat (np.ndarray): A block diagonal boolean matrix.

        Returns:
            List[List[Tuple[int,int]]]: Parallel row elimination. In each depth level there are
            non-overlapping row eliminations.
        """
        n = mat.shape[0]
        s_size = n // 2

        u1 = mat[:s_size, :s_size]
        u2 = mat[s_size:, s_size:]

        u1_parallel_elimination = cls.__matrix_run(u1)
        u2_parallel_elimination = cls.__matrix_run(u2)

        u1_p_l = len(u1_parallel_elimination)
        u2_p_l = len(u2_parallel_elimination)
        for lv in u2_parallel_elimination:
            for idx, r in enumerate(lv):
                lv[idx] = (r[0] + s_size, r[1] + s_size)
        p_l = max(u1_p_l, u2_p_l)

        parallel_elimination: List[List[Tuple[int, int]]] = [[] for _ in range(p_l)]

        for i in range(p_l):
            if i < u1_p_l:
                parallel_elimination[i].extend(u1_parallel_elimination[i])
            if i < u2_p_l:
                parallel_elimination[i].extend(u2_parallel_elimination[i])

        return parallel_elimination

    @classmethod
    def remapping_run(cls, remapping: List[int]) -> List[List[Tuple[int, int]]]:
        s_size = len(remapping) // 2

        parallel_elimination: List[List[Tuple[int, int]]] = [[], [], []]

        for i in range(s_size):
            if remapping[i] >= s_size:
                x = remapping[i]
                y = i
                parallel_elimination[0].append((x, y))
                parallel_elimination[1].append((y, x))
                parallel_elimination[2].append((x, y))

        return parallel_elimination
