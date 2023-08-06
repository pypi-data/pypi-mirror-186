"""
Another version of decomposition of SU(4) with Cartan KAK Decomposition,
which is specially designed for the optimization of unitary transform.
"""

import numpy as np

from QuICT.core.gate import CompositeGate, CX, Rx, Rz, Unitary
from .cartan_kak_decomposition import CartanKAKDecomposition

# Magic basis
B = (1.0 / np.sqrt(2)) * np.array([[1, 1j, 0, 0],
                                   [0, 0, 1j, 1],
                                   [0, 0, 1j, -1],
                                   [1, -1j, 0, 0]], dtype=complex)


class CartanKAKDiagonalDecomposition(object):
    def __init__(self, eps=1e-15):
        """
        Args:
            eps(float, optional): Eps of decomposition process
        """
        self.eps = eps

    def execute(self, matrix):
        """
        Decompose a matrix U in SU(4) with Cartan KAK Decomposition. Unlike the
        original version, now the result circuit has a two-qubit gate whose
        matrix is diagonal at the edge, which is useful in the optimization.
        The process is taken from [2] Proposition V.2 and Theorem VI.3,
        while the Cartan KAK Decomposition process is refined from [1].

        Args:
            matrix(np.array): 4*4 unitary matrix to be decomposed

        Returns:
            CompositeGate: Decomposed gates.

        Reference:
            [1] https://arxiv.org/abs/0806.4015
            [2] https://arxiv.org/abs/quant-ph/0308033
        """
        sy2 = np.array([[0, 0, 0, -1],
                        [0, 0, 1, 0],
                        [0, 1, 0, 0],
                        [-1, 0, 0, 0]], dtype=complex)

        # Proposition V.2
        U = matrix.copy()
        U /= np.linalg.det(U) ** 0.25
        gUTT = U.T.dot(sy2).dot(U).dot(sy2).T
        denominator = (gUTT[0, 0] - gUTT[1, 1] - gUTT[2, 2] + gUTT[3, 3]).real
        if np.isclose(denominator, 0):
            psi = np.pi / 2
        else:
            numerator = (gUTT[0, 0] + gUTT[1, 1] + gUTT[2, 2] + gUTT[3, 3]).imag
            psi = np.arctan(numerator / denominator)

        gates_Delta = CompositeGate()
        with gates_Delta:
            CX & [0, 1]
            Rz(psi) & 1
            CX & [0, 1]
        Delta = gates_Delta.matrix()
        U = U.dot(Delta)

        # Refined Cartan KAK Decomposition for U (because we have known Ud here!)
        # Some preparation derived from Cartan involution
        Up = B.T.conj().dot(U).dot(B)
        M2 = Up.T.dot(Up)
        M2.real[abs(M2.real) < self.eps] = 0.0
        M2.imag[abs(M2.imag) < self.eps] = 0.0

        # Since M2 is a symmetric unitary matrix, we can diagonalize its real and
        # imaginary part simultaneously. That is, ∃ P in SO(4), s.t. M2 = P.D.P^T,
        # where D is diagonal with unit-magnitude elements.
        D, P = CartanKAKDecomposition.diagonalize_unitary_symmetric(M2)
        d = np.angle(D) / 2

        # A special case occurs when there are pairs of -1 in D
        if np.any(np.isclose(D, -1)):
            if np.count_nonzero(np.isclose(D, -1)) == 2:
                d[np.where(np.isclose(D, -1))] = np.pi / 2, -np.pi / 2
            elif np.count_nonzero(np.isclose(D, -1)) == 4:
                d[:] = np.pi / 2, np.pi / 2, -np.pi / 2, -np.pi / 2
            else:
                raise ValueError('Odd number of -1 in D')

        # Refinement time, by some mathematics we know that d here must be a rearragement
        # of d_Ud. However, the diagonalization process does not guarantee that they are
        # correctly sorted.
        order = np.argsort(d)[::-1]
        d[:] = d[order]
        P[:, :] = P[:, order]
        a = (d[0] + d[2]) / 2
        b = (d[1] + d[2]) / 2
        c = (d[0] + d[1]) / 2
        assert np.isclose(b, 0)

        # P could be in O(4) instead of SO(4).
        if np.linalg.det(P) < 0:
            P[:, -1] = -P[:, -1]

        # Now is the time to calculate KL and KR
        KL = B.dot(Up).dot(P).dot(np.diag(np.exp(-1j * d))).dot(B.T.conj())
        KR = B.dot(P.T).dot(B.T.conj())
        KL.real[abs(KL.real) < self.eps] = 0.0
        KL.imag[abs(KL.imag) < self.eps] = 0.0
        KR.real[abs(KR.real) < self.eps] = 0.0
        KR.imag[abs(KR.imag) < self.eps] = 0.0
        KL0, KL1 = CartanKAKDecomposition.tensor_decompose(KL)
        KR0, KR1 = CartanKAKDecomposition.tensor_decompose(KR)

        # Finally we could combine everything together
        gates = CompositeGate()
        with gates:
            Unitary(Delta.conj()) & [0, 1]
            Unitary(KR0) & 0
            Unitary(KR1) & 1
            CX & [0, 1]
            Rx(-2 * a) & 0
            Rz(-2 * c) & 1
            CX & [0, 1]
            Unitary(KL0) & 0
            Unitary(KL1) & 1

        return gates
