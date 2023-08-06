#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/5/20 上午10:37
# @Author  : Kaiqi Li
# @File    : cpu_calculator
import random
from numba import njit, prange
import numpy as np

from QuICT.ops.utils import mapping_augment


@njit(parallel=True, nogil=True)
def MatrixTensorI(A, n, m):
    """ tensor I^n and A and I^m

    Args:
        A(np.array<np.complex>): the matrix A
        n(int): the index of indentity
        m(int): the index of indentity

    Returns:
        np.array<np.complex>: the tensor result I^n ⊗ A ⊗ I^m
    """
    i_m = np.identity(m)
    row_a, col_a = A.shape
    MatrixTensor = np.zeros((n * m * row_a, n * m * col_a), dtype=A.dtype)

    for i in prange(row_a):
        for j in prange(col_a):
            temp_M = A[i, j] * i_m
            for k in range(n):
                start_row_idx = k * m * row_a + i * m
                start_col_idx = k * m * col_a + j * m
                MatrixTensor[start_row_idx:start_row_idx + m, start_col_idx:start_col_idx + m] = temp_M

    return MatrixTensor


@njit(parallel=True, nogil=True)
def MatrixPermutation(A: np.ndarray, mapping: np.ndarray, changeInput: bool = False) -> np.ndarray:
    """ permute A with mapping, inplace

    Args:
        A(np.array<np.complex>): the matrix A
        mapping(np.ndarray<int>): the qubit mapping
        changeInput(bool): whether changes in A
    """
    if not A.shape[0] == (1 << mapping.shape[0]):
        raise IndexError("Indices do not match!")

    idx_mapping = mapping_augment(mapping)

    # Do NOT perform parallel operations over row permutations!
    # They are just too spare in memory. Elements in the same column
    # are distributed with a gap as matrix row length.
    perm_mat = A[idx_mapping, :]
    for i in prange(idx_mapping.shape[0]):
        perm_mat[i] = perm_mat[i][idx_mapping]

    if changeInput:
        A[:, :] = perm_mat

    return perm_mat


@njit()
def VectorPermutation(A: np.ndarray, mapping: np.ndarray, changeInput: bool = False):
    """ permutaion A with mapping, changeInput

    Args:
        A(np.array<np.complex>): the matrix A
        mapping(np.ndarray<int>): the qubit mapping
        changeInput(bool): whether changes in A
    Returns:
        np.array<np.complex>: the result of Permutation
    """
    if not A.shape[0] == 1 << mapping.shape[0]:
        raise IndexError("Indices do not match!")

    switched_idx = mapping_augment(mapping)

    if changeInput:
        A[:] = A[switched_idx]

    return A[switched_idx]


@njit(parallel=True, nogil=True)
def tensor(A: np.ndarray, B: np.ndarray):
    """ tensor A and B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: the tensor result A ⊗ B
    """
    row_a, col_a = A.shape
    row_b, col_b = B.shape
    tensor_data = np.empty((row_a * row_b, col_a * col_b), dtype=A.dtype)

    for r in prange(row_a):
        for c in prange(col_a):
            tensor_data[r * row_b:(r + 1) * row_b, c * col_b:(c + 1) * col_b] = A[r, c] * B

    return tensor_data


@njit()
def dot(A: np.ndarray, B: np.ndarray):
    """ dot matrix A and matrix B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: A * B
    """
    return np.dot(A, B)


@njit()
def multiply(A: np.ndarray, B: np.ndarray):
    """ multiply matrix A and matrix B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: A x B
    """
    return np.multiply(A, B)


@njit()
def matrix_dot_vector(
    vec: np.ndarray,
    vec_bit: int,
    mat: np.ndarray,
    mat_bit: int,
    mat_args: np.ndarray
):
    """ Dot the quantum gate's matrix and qubits'state vector, depending on the target qubits of gate.

    Args:
        vec (np.ndarray): The state vector of qubits
        vec_bit (np.int32): The number of qubits
        mat (np.ndarray): The 2D numpy array, represent the quantum gate's matrix
        mat_bit (np.int32): The quantum gate's qubit number
        mat_args (np.ndarray): The target qubits of quantum gate

    Raises:
        TypeError: matrix and vector should be complex and with same precision

    Returns:
        np.ndarray: updated state vector
    """
    # Deal with special case when matrix's qubit == vector's qubit
    if mat_bit == vec_bit:
        return np.dot(mat, vec)

    repeat = 1 << (vec_bit - mat_bit)
    arg_len = 1 << mat_bit
    sorted_args = mat_args.copy()
    sorted_args = np.sort(sorted_args)
    aux = np.zeros_like(vec)
    for i in range(repeat):
        for sarg_idx in range(mat_bit):
            less = i & ((1 << sorted_args[sarg_idx]) - 1)
            i = i >> sorted_args[sarg_idx] << (sorted_args[sarg_idx] + 1) + less

        indexes = np.array([i] * arg_len, dtype=np.int32)
        for i in range(1, arg_len, 1):
            for j in range(mat_bit):
                if i & (1 << j):
                    indexes[i] += 1 << mat_args[j]

        aux[indexes] = dot(mat, vec[indexes])

    return aux


@njit()
def measure_gate_apply(
    index: int,
    vec: np.array
):
    """ Measured the state vector for target qubit

    Args:
        index (int): The index of target qubit
        vec (np.array): The state vector of qubits

    Raises:
        TypeError: The state vector should be np.ndarray.

    Returns:
        bool: The measured result 0 or 1.
    """
    target_index = 1 << index
    vec_idx_0 = [idx for idx in range(len(vec)) if not idx & target_index]
    vec_idx_0 = np.array(vec_idx_0, dtype=np.int32)
    vec_idx_1 = [idx for idx in range(len(vec)) if idx & target_index]
    vec_idx_1 = np.array(vec_idx_1, dtype=np.int32)
    prob = np.sum(np.square(np.abs(vec[vec_idx_0])))

    _1 = random.random() > prob
    if _1:
        alpha = np.float64(1 / np.sqrt(1 - prob))
        vec[vec_idx_0] = np.complex128(0)
        vec[vec_idx_1] = vec[vec_idx_1] * alpha
    else:
        alpha = np.float64(1 / np.sqrt(prob))
        vec[vec_idx_0] = vec[vec_idx_0] * alpha
        vec[vec_idx_1] = np.complex128(0)

    return _1
