from typing import Union
import numpy as np


CGATE_LIST = []


def matrix_product_to_circuit(
    gate_matrix: np.ndarray,
    gate_args: Union[int, list],
    max_q: int,
    min_q: int = 0,
    gpu_output: bool = False
):
    """ Expand gate matrix with the number of qubits

    Args:
        gate_matrix (np.ndarray): The gate's matrix.
        gate_args Union[int, list]: The gate's qubit indexes.
        max_q (int): The qubits' number
        min_q (int, optional): The minimum qubit's number. Defaults to 0.
        gpu_output(bool, optional): Generate matrix in GPU or not. Default to False.

    Returns:
        np.array: the expanded gate's 2-D matrix
    """
    if isinstance(gate_args, int):
        gate_args = [gate_args]

    n = 1 << (max_q - min_q)
    xor = n - 1
    new_values = np.zeros((n, n), dtype=gate_matrix.dtype)
    assert gate_matrix.shape == (1 << len(gate_args), 1 << len(gate_args))
    for arg in gate_args:
        assert arg >= 0 and arg < max_q and isinstance(arg, int)

    datas = np.zeros(n, dtype=int)
    for i in range(n):
        nowi = 0
        for t_idx, targ in enumerate(gate_args):
            assert targ >= min_q and targ < max_q
            k = (max_q - min_q) - 1 - (targ - min_q)
            if (1 << k) & i != 0:
                nowi += (1 << (len(gate_args) - 1 - t_idx))

        datas[i] = nowi

    for i in gate_args:
        xor = xor ^ (1 << (max_q - 1 - i))

    for i in range(n):
        nowi = datas[i]
        for j in range(n):
            if (i & xor) == (j & xor):
                nowj = datas[j]
                new_values[i][j] = gate_matrix[nowi][nowj]

    if gpu_output:
        import cupy as cp

        new_values = cp.array(new_values)

    return new_values


def perm_decomposition(permutation: list):
    n = len(permutation)
    assert len(set(permutation)) == n and set(permutation) == set(range(n))

    sorted_idx, swap_pairs = [], []
    idx = 0
    while idx < n:
        if idx in sorted_idx:
            idx += 1
            continue

        target = permutation[idx]
        if target != idx:
            swap_pairs.append([idx, target])
            sorted_idx.append(target)
            permutation[idx], permutation[target] = permutation[target], permutation[idx]
        else:
            idx += 1

    return swap_pairs
