#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/12/28 12:29 上午
# @Author  : Han Yu
# @File    : uniformly_unitary.py

import numpy as np

from .uniformly_rotation import UniformlyRotation
from QuICT.core.gate import build_gate, GateType, CompositeGate, H, Rz, CX


class UniformlyUnitary(object):
    """
    Implements the uniformly unitary gate

    Reference:
        https://arxiv.org/abs/quant-ph/0504100 Fig4 b)
    """
    def execute(self, matrices):
        """
        Args:
            matrices(list<numpy.array>): the matrices of unitary gates

        Returns:
            CompositeGate: CompositeGate that implements the uniformly gate
        """
        matrices = list(matrices)
        n = int(np.log2(len(matrices))) + 1
        if 1 << (n - 1) != len(matrices):
            raise Exception("the number of parameters unmatched.")
        return self.uniformly_unitary(0, n, matrices)

    def uniformly_unitary(self, low, high, unitary):
        """ synthesis uniformlyUnitary gate, bits range [low, high)

        Args:
            low(int): the left range low
            high(int): the right range high
            unitary(list<int>): the list of unitaries
        Returns:
            the synthesis result
        """
        if low + 1 == high:
            rot = self.unitary_to_u3gate(unitary[0], low)
            gates = CompositeGate()
            gates.append(rot)
            return gates
        length = len(unitary) // 2
        Rxv = []
        Rxu = []
        angle_list = [0] * 2 * length
        for i in range(length):
            v, u, angles = self.get_parameters_from_unitaries(unitary[i], unitary[i + length])
            Rxu.append(u)
            Rxv.append(v)
            dual_position = 0
            for j in range(high - low - 2):
                if (1 << j) & i:
                    dual_position += 1 << (high - low - 2 - j - 1)
            angle_list[dual_position] = angles[0]
            angle_list[dual_position + length] = angles[1]
        gates = self.uniformly_unitary(low + 1, high, Rxv)
        CX & [low, high - 1] | gates
        gates.extend(self.uniformly_unitary(low + 1, high, Rxu))
        URz = UniformlyRotation(GateType.rz)
        urz = URz.execute(angle_list)
        urz & list(range(high - 1, low - 1, -1))
        gates.extend(urz)
        return gates

    def unitary_to_u3gate(self, unitary, target):
        """ gates from a one-qubit unitary

        Args:
            unitary(np.ndarray): the unitary to be transformed
            target(int): the qubit gate acts on
        Returns:
            U3Gate: gate from the unitary
        """
        unitary = np.array(unitary).reshape(2, 2)
        z = np.exp(1j * np.angle(unitary[0, 0]))
        unitary = unitary / z

        theta = np.arccos(unitary[0, 0])
        sint = np.sin(theta)
        if abs(sint) >= 1e-6:
            lamda = np.angle(unitary[0, 1] / -sint)
            phi = np.angle(unitary[1, 0] / sint)
        else:
            lamda = 0
            phi = np.angle(unitary[1, 1] / np.cos(theta))
        gate = build_gate(GateType.u3, target, [theta * 2, phi, lamda])
        assert np.allclose(gate.matrix, unitary)
        return gate

    def u2_phase_angle(self, mat):
        """ express U(2) with SU(2) and phase

        exp(i * phi / 2) SU(2) = U(2)

        Args:
            mat(np.ndarray): U2 matrix

        Returns:
            float: phase angle
        """
        if abs(mat[0, 0]) < 1e-10:
            absX = -mat[1, 0] * mat[0, 1]
            phase = np.angle(absX) / 2
            mat /= np.exp(1j * phase)
        else:
            absX = mat[0, 0] * mat[1, 1]
            phase = np.angle(absX) / 2
            mat /= np.exp(1j * phase)

        return 2 * phase

    def get_parameters_from_unitaries(self, u1, u2):
        """ decomposition uniformly controlled one qubit unitaries

        (0><0) ⊗ u1 + (1><1) ⊗ u2

        Args:
            u1(np.ndarray): unitary with 0
            u2(np.ndarray): unitary with 1

        Returns:
            np.ndarray: v in the decomposition
            np.ndarray: u in the decomposition
            list<float>: angle list of Rz
        """
        a = np.array(u1).reshape(2, 2)
        b = np.array(u2).reshape(2, 2)

        mat = a.dot(b.T.conj())
        phi = self.u2_phase_angle(mat)
        x1 = np.angle(mat[0, 0])

        r11_angle = 1j / 2 * (-np.pi / 2 - phi / 2 - x1)
        r22_angle = 1j / 2 * (np.pi / 2 - phi / 2 + x1)
        r = np.diag([np.exp(r11_angle), np.exp(r22_angle)])

        rXr = r.dot(mat).dot(r) * np.exp(1j * phi / 2)
        lamda, hU = np.linalg.eig(rXr)
        if abs(abs(lamda[0] - 1j)) >= 1e-10:
            hU[:, [0, 1]] = hU[:, [1, 0]]

        u = hU.reshape(2, 2)
        d = np.diag([np.exp(1j * np.pi / 4), np.exp(-1j * np.pi / 4)])
        v = d.T.conj().dot(u.T.conj()).dot(r).dot(a)
        v = H.matrix.dot(v)
        v *= np.exp(-1j * np.pi / 4)
        u = u.dot(Rz(-np.pi / 2).matrix).dot(H.matrix)

        return v, u, [-np.pi - 1.0 * (x1 + phi / 2), 1.0 * (x1 - phi / 2)]
