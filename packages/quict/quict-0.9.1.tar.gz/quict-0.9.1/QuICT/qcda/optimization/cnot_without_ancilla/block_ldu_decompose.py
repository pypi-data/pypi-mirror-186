from typing import *
import numpy as np

from .utility import *


class BlockLDUDecompose:
    @classmethod
    def remapping_select(cls, mat_: np.ndarray) \
            -> List[int]:
        """
        Select some rows out of a square matrix to get a full-ranked sub-matrix.

        Args:
            mat_(np.ndarray): Boolean matrix to be decomposed

        Returns:
            List[int]: Row reordering args. The remapping ensures that if selected rows
                are in the upper part before selecting, their locations won't be changed.
        """
        mat = mat_.copy()
        n = mat.shape[0]
        s_size = n // 2
        selected = []
        unselected = []
        rk = 0
        for i in range(n):
            selected.append(i)
            sub_mat = mat[selected, :s_size]
            slct_rk = f2_rank(sub_mat)
            if slct_rk == len(selected):
                rk += 1
                if rk == s_size:
                    for j in range(i + 1, n):
                        unselected.append(j)
                    break
            else:
                unselected.append(selected.pop())

        selected_part2 = []
        swap_flag = [True for _ in range(s_size)]
        for i in range(s_size):
            if selected[i] < s_size:
                swap_flag[selected[i]] = False
            else:
                selected_part2.append(selected[i])

        remapping = [i for i in range(n)]

        cur_part2_ptr = 0
        for i in range(s_size):
            if swap_flag[i]:
                x = i
                y = selected_part2[cur_part2_ptr]
                remapping[x], remapping[y] = remapping[y], remapping[x]
                cur_part2_ptr += 1

        return remapping

    @classmethod
    def run(cls, mat_: np.ndarray) \
            -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[int]]:
        """
        Block LDU decomposition of a boolean matrix.

        Args:
            mat_(np.ndarray): Boolean matrix to be decomposed

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, List[int]]: Decomposed L, D, U and row remapping.
        """

        n = mat_.shape[0]
        if n <= 1:
            raise Exception("LDU decomposition is designed for matrix whose size >= 2.")

        remapping = cls.remapping_select(mat_)
        mat: np.ndarray = mat_.copy()[remapping]

        s_size = n // 2
        t_size = n - s_size

        a = mat[:s_size, :s_size]
        b = mat[:s_size, s_size:]
        c = mat[s_size:, :s_size]
        d = mat[s_size:, s_size:]

        ai = f2_inverse(a)
        c_ai = f2_matmul(c, ai)
        c_ai_b = f2_matmul(c_ai, b)
        ai_b = f2_matmul(ai, b)

        lower = np.zeros(shape=(n, n), dtype=bool)
        diagonal = np.zeros(shape=(n, n), dtype=bool)
        upper = np.zeros(shape=(n, n), dtype=bool)

        # lower
        lower[:s_size, :s_size] = np.eye(s_size, dtype=bool)
        lower[s_size:, s_size:] = np.eye(t_size, dtype=bool)
        lower[s_size:, :s_size] = c_ai

        # diagonal
        diagonal[:s_size, :s_size] = a
        diagonal[s_size:, s_size:] = d ^ c_ai_b

        # upper
        upper[:s_size, :s_size] = np.eye(s_size, dtype=bool)
        upper[s_size:, s_size:] = np.eye(t_size, dtype=bool)
        upper[:s_size, s_size:] = ai_b

        return lower, diagonal, upper, remapping
