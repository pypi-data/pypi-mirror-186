#!/usr/bin/env python
# -*- coding:utf8 -*-

from typing import *
import numpy as np


class Merged:
    """
    Merged points in heap

    Attributes:
        deg(int) : degree of x
        nodes(List[int]) : node indices in a bipartite
    """

    def __init__(self, deg: int, nodes: List[int]):
        """
        Get a merged point

        Args:
            deg(int) : degree of x
            nodes(List[int]) : node indices in a bipartite
        """
        self.deg = deg
        self.nodes = nodes

    def __add__(self, other: "Merged") -> "Merged":
        """
        combine two merged points to a larger merged

        Args:
            other(Merged): Another Merged node.
        """
        d = self.deg + other.deg
        x = self.nodes + other.nodes
        return Merged(d, x)

    def __lt__(self, other):
        return self.deg < other.deg


def f2_matmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Multiply 2 matrices in F_2.

    Args:
        a (np.ndarray): Input boolean matrix a.
        b (np.ndarray): Input boolean matrix b.

    Returns:
        np.ndarray: Production of ab over F_2.
    """
    a_ = np.array(a, dtype=int)
    b_ = np.array(b, dtype=int)
    c_ = a_ @ b_
    c_ %= 2
    c = np.array(c_, dtype=bool)
    return c


def f2_half_gaussian_elimination(mat_: np.ndarray) -> np.ndarray:
    """
    Gaussian elimination to convert a matrix into triangular form over F_2.
    Args:
        mat_ (np.ndarray): Input boolean matrix.

    Returns:
        np.ndarray: Eliminated triangular matrix.
    """
    mat: np.ndarray = mat_.copy()
    row_pivot = 0
    col_pivot = 0
    m = mat.shape[0]
    n = mat.shape[1]
    while row_pivot < m and col_pivot < n:
        if not mat[row_pivot, col_pivot]:
            for k in range(row_pivot + 1, m):
                if mat[k, col_pivot]:
                    mat[[k, row_pivot], :] = mat[[row_pivot, k], :]
                    break
        if mat[row_pivot, col_pivot]:
            for k in range(row_pivot + 1, m):
                if mat[k, col_pivot]:
                    mat[k, :] ^= mat[row_pivot, :]
            row_pivot += 1
            col_pivot += 1
        else:
            col_pivot += 1
    return mat


def f2_rank(mat_: np.ndarray) -> int:
    """
    Rank of a matrix over F_2.
    Args:
        mat_ (np.ndarray): Input boolean matrix.

    Returns:
        int: Rank of mat_ over F_2.
    """
    mat = f2_half_gaussian_elimination(mat_)
    rk = 0
    for i in range(mat.shape[0]):
        if np.any(mat[i, :]):
            rk += 1
    return rk


def f2_inverse(mat_: np.ndarray) -> np.ndarray:
    """
    Matrix inverse over F_2.
    Args:
        mat_ (np.ndarray): Input boolean matrix.

    Returns:
        np.ndarray: The inverse boolean matrix of mat_ over F_2.
    """
    n = mat_.shape[0]
    aug = np.empty(shape=(n, 2 * n), dtype=bool)
    aug[:, :n] = mat_
    aug[:, n:] = np.eye(n, dtype=bool)

    # gaussian elimination
    for i in range(n):
        if not aug[i, i]:
            for k in range(i + 1, n):
                if aug[k, i]:
                    aug[[k, i], :] = aug[[i, k], :]
                    break
        if not aug[i, i]:
            raise Exception("Matrix is not invertible!")
        for k in range(n):
            if i != k and aug[k, i]:
                aug[k, :] ^= aug[i, :]
    ret = aug[:, n:].copy()
    return ret
