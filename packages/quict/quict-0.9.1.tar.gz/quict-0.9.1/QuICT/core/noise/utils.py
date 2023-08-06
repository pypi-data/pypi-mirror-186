from enum import Enum
import numpy as np

from QuICT.ops.linalg.cpu_calculator import dot


def is_kraus_ops(kraus: list) -> bool:
    row, col = kraus[0].shape
    n = int(np.log2(row))
    if not row == col or not row == 2 ** n:
        return False

    for kmat in kraus:
        if not kmat.shape == (row, col):
            return False

    kk = sum(dot(np.transpose(k).conjugate(), (k)) for k in kraus)
    if not np.allclose(kk, np.identity(row, dtype=kraus[0].dtype), rtol=1e-4):
        return False

    return True


class NoiseChannel(Enum):
    unitary = "Unitary Channel"
    pauil = "Pauli Channel"
    depolarizing = "Depolarizing Channel"
    damping = "Damping Channel"
    readout = "Readout Channel"
