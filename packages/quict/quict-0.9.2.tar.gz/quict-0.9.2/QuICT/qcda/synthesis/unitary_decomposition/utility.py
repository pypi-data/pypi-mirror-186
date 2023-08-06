from typing import *
import numpy as np

from QuICT.core import *
from QuICT.core.gate import *


def add_factor_shift_into_phase(gates: CompositeGate, shift: complex) -> CompositeGate:
    phase = np.angle(shift)
    phase_gate = GPhase(phase) & 0
    gates.append(phase_gate)
    return gates


def quantum_shannon_decompose(
        u1: np.ndarray,
        u2: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Decompose a block diagonal even-size unitary matrix.
    block_diag(u1,u2) == block_diag(v, v) @ block_diag(d, d_dagger) @ block_diag(w, w)

    Args:
        u1 (np.ndarray): upper-left block
        u2 (np.ndarray): right-bottom block

    Returns:
        Tuple[np.ndarray,np.ndarray,np.ndarray]
    """
    s = u1 @ u2.conj().T

    eig_values, v = np.linalg.eig(s)
    v_dagger = v.conj().T
    d = np.sqrt(np.diag(eig_values))
    w = d @ v_dagger @ u2

    return v, d, w


def shift_ratio(mat1: np.ndarray, mat2: np.ndarray) -> complex:
    return mat1.dot(np.linalg.inv(mat2))[0, 0]
