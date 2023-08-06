#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/2/24 上午10:37
# @Author  : Kaiqi Li
# @File    : cpu_calculator
import os
import subprocess
import numpy as np

try:
    from QuICT.ops.backend import linalg
except ImportError:
    backend_file_path = os.path.dirname(__file__) + "/../backend/linear_alg_cpu.py"
    res = subprocess.call(["python3", backend_file_path])
    from QuICT.ops.backend import linalg


def MatrixTensorI(A, n, m):
    """ tensor I^n and A and I^m

    Args:
        A(np.array<np.complex>): the matrix A
        n(int): the index of indentity
        m(int): the index of indentity

    Returns:
        np.array<np.complex>: the tensor result I^n ⊗ A ⊗ I^m
    """
    # Parameter normalized
    n, m = np.int32(n), np.int32(m)
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if A.dtype == np.complex64:
        return linalg.matrixtensorf(A, n, m)
    elif A.dtype == np.complex128:
        return linalg.matrixtensord(A, n, m)
    else:
        raise TypeError(f"The matrix A should be complex64 or complex128, not {A.dtype}.")


def MatrixPermutation(A: np.ndarray, mapping: np.ndarray, changeInput: bool = False) -> np.ndarray:
    """ permute A with mapping, inplace

    Args:
        A(np.array<np.complex>): the matrix A
        mapping(np.ndarray<int>): the qubit mapping
        changeInput(bool): whether changes in A
    """
    # Parameter normalized
    assert isinstance(changeInput, bool)
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if not isinstance(mapping, np.ndarray):
        mapping = np.array(mapping, dtype=np.int32)

    if mapping.dtype != np.int32:
        mapping = mapping.astype(np.int32)

    if A.dtype == np.complex64:
        ops = linalg.matrixpermf
    elif A.dtype == np.complex128:
        ops = linalg.matrixpermd
    else:
        raise TypeError(f"The matrix A should be complex64 or complex128, not {A.dtype}.")

    if changeInput:
        ops(A, mapping, changeInput)
    else:
        return ops(A, mapping, changeInput)


def VectorPermutation(A: np.ndarray, mapping: np.ndarray, changeInput: bool = False):
    """ permutaion A with mapping, changeInput

    Args:
        A(np.array<np.complex>): the matrix A
        mapping(np.ndarray<int>): the qubit mapping
        changeInput(bool): whether changes in A
    Returns:
        np.array<np.complex>: the result of Permutation
    """
    # Parameter normalized
    assert isinstance(changeInput, bool)
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if not isinstance(mapping, np.ndarray):
        mapping = np.array(mapping, dtype=np.int32)

    if mapping.dtype != np.int32:
        mapping = mapping.astype(np.int32)

    if A.dtype == np.complex64:
        ops = linalg.vectorpermf
    elif A.dtype == np.complex128:
        ops = linalg.vectorpermd
    else:
        raise TypeError(f"The matrix A should be complex64 or complex128, not {A.dtype}.")

    if changeInput:
        ops(A, mapping, changeInput)
    else:
        return ops(A, mapping, changeInput)


def tensor(A, B):
    """ tensor A and B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: the tensor result A ⊗ B
    """
    # Parameter normalized
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if not isinstance(B, np.ndarray):
        B = np.array(B)

    if A.dtype == np.complex64 and B.dtype == np.complex64:
        return linalg.tensorf(A, B)
    elif A.dtype == np.complex128 and B.dtype == np.complex128:
        return linalg.tensord(A, B)
    else:
        raise TypeError(f"The matrix should be complex64 or complex128, not {A.dtype} and {B.dtype}.")


def dot(A, B):
    """ dot matrix A and matrix B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: A * B
    """
    # Parameter normalized
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if not isinstance(B, np.ndarray):
        B = np.array(B)

    assert A.dtype == B.dtype and A.shape[1] == B.shape[0]
    if A.dtype == np.complex64:
        if B.ndim == 1:
            return linalg.vdotmf(A, B)
        else:
            return linalg.dotf(A, B)
    elif A.dtype == np.complex128:
        if B.ndim == 1:
            return linalg.vdotmd(A, B)
        else:
            return linalg.dotd(A, B)
    else:
        raise TypeError(f"The matrix should be complex64 or complex128, not {A.dtype} and {B.dtype}.")


def multiply(A, B):
    """ multiply matrix A and matrix B

    Args:
        A(np.array<np.complex>): the matrix A
        B(np.array<np.complex>): the matrix B

    Returns:
        np.array<np.complex>: A x B
    """
    # Parameter normalized
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if not isinstance(B, np.ndarray):
        B = np.array(B)

    if A.dtype == np.complex64 and B.dtype == np.complex64:
        return linalg.multiplyf(A, B)
    elif A.dtype == np.complex128 and B.dtype == np.complex128:
        return linalg.multiplyd(A, B)
    else:
        raise TypeError(f"The matrix should be complex64 or complex128, not {A.dtype} and {B.dtype}.")


def matrix_dot_vector(
    vec: np.ndarray,
    vec_bit: int,
    mat: np.ndarray,
    mat_bit: int,
    mat_args: np.ndarray
):
    """ Dot the quantum gate's matrix and qubits'state vector, depending on the target qubits of gate.

    Args:
        mat (np.ndarray): The 2D numpy array, represent the quantum gate's matrix
        mat_bit (np.int32): The quantum gate's qubit number
        vec (np.ndarray): The state vector of qubits
        vec_bit (np.int32): The number of qubits
        mat_args (np.ndarray): The target qubits of quantum gate

    Raises:
        TypeError: matrix and vector should be complex and with same precision

    Returns:
        np.ndarray: updated state vector
    """
    # Parameter normalized
    mat_bit, vec_bit = np.int32(mat_bit), np.int32(vec_bit)
    if not isinstance(mat, np.ndarray):
        mat = np.array(mat)

    if not isinstance(vec, np.ndarray):
        vec = np.array(vec)

    if not isinstance(mat_args, np.ndarray):
        mat_args = np.array(mat_args, np.int32)
    elif mat_args.dtype != np.int32:
        mat_args = mat_args.astype(np.int32)

    if mat_bit == vec_bit:
        return dot(mat, vec)

    if mat.dtype == np.complex64 and vec.dtype == np.complex64:
        return linalg.matdotvecf(mat, mat_bit, vec, vec_bit, mat_args)
    elif mat.dtype == np.complex128 and vec.dtype == np.complex128:
        return linalg.matdotvecd(mat, mat_bit, vec, vec_bit, mat_args)
    else:
        raise TypeError(f"The matrix should be complex64 or complex128, not {mat.dtype} and {vec.dtype}.")


def measure_gate_apply(
    index: int,
    vec: np.array
):
    """ Measured the state vector for target qubit

    Args:
        index (int): The index of target qubit
        vec (np.array): The state vector of qubits

    Raises:
        TypeError: The vector should be complex.

    Returns:
        _type_: The updated state vector
    """
    # Parameter normalized
    index = np.int32(index)
    if not isinstance(vec, np.ndarray):
        vec = np.array(vec)

    if vec.dtype == np.complex64:
        return linalg.measuref(index, vec)
    elif vec.dtype == np.complex128:
        return linalg.measured(index, vec)
    else:
        raise TypeError(f"The vector should be complex64 or complex128, not {vec.dtype}.")
