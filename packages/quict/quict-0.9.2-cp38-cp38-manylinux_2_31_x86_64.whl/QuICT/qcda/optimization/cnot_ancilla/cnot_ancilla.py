#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/11/5 8:55
# @Author  : Han Yu
# @File    : cnot_ancillae.py

from math import log2, ceil, floor, sqrt
from typing import Union

import numpy as np

from QuICT.core import *
from QuICT.core.gate import CX, CompositeGate, GateType
from QuICT.qcda.utility import OutputAligner
from QuICT.tools.exception.core import ValueError, CircuitAppendError


class CnotAncilla(object):
    """ Optimization the circuit by (3s+1)n ancillary qubits

    Optimal Space-Depth Trade-Off of CNOT Circuits in Quantum Logic Synthesis
    Theorem 7
    parallelize any n-qubit CNOT circuit into O(n/slogn) depth with (3s+1) ancillas,
    where 1 <= s <= O(n/log^2n). time complex is \tilde{O}(n^w), which is time for get inverse of a matrix.
    https://arxiv.org/pdf/1907.05087.pdf
    """
    def __init__(self, size=1):
        """
        Args:
            size(int): the 's' in the Theorem, where (3s+1) ancillas would be used
        """
        self.size = size

    @OutputAligner()
    def execute(self, circuit: Union[Circuit, CompositeGate]):
        """
        Args:
            circuit(CompositeGate/Circuit): circuit to be optimize

        Returns:
            CompositeGate/Circuit: the optimized circuit
        """
        # transform the CNOT circuit into a matrix with 0 and 1
        self.width = circuit.width()
        if self.width < 4:
            raise ValueError("CnotAncilla.circuit.width", ">= 4", self.width)
        matrix = np.identity(self.width, dtype=bool)
        for gate in circuit.gates:
            if gate.type != GateType.cx:
                raise CircuitAppendError(f"the input circuit should be a CNOT circuit, but it contains {str(gate)}")
            matrix[gate.targs] = np.bitwise_xor(matrix[gate.cargs], matrix[gate.targs])

        # apply Theorem 7 to build new circuit
        self.CNOT = []
        # x, z and c mean three part in the circuit in the theorem 7
        x: list = [j for j in range(self.width)]
        z: list = [j + self.width for j in range(self.width)]
        c: list = [j + 2 * self.width for j in range(3 * self.size * self.width)]
        inv_matrix = self.inverse_matrix_f2(matrix, self.width)
        # do C_1 operate
        self.lemma_4(matrix, x, c, z)
        # do C_2 operate
        self.lemma_4(inv_matrix, z, c, x)

        new_circuit = Circuit(circuit.width() * (2 + 3 * self.size))
        for cnot in self.CNOT:
            CX | new_circuit([cnot[0], cnot[1]])
        return new_circuit

    def lemma_4(self, M, x, c, z):
        """ apply Lemma4 to make (x, z, 0) -> (x, z xor Mx, 0)

        time complex: \tilde{O}(n^2)
        depth : O(n/slogn)

        Args:
            M(np.matrix): a matrix in F_2
            x(list<int>): the indexes of first register, length is n
            c(list<int>): the indexes of ancillary register, length is n
            z(list<int>): the indexes of second register, length is 3 * s * n
        """
        # divide the part into size slog^2n and apply Lemma 5
        # we ensure the log2n be even and 2 (sqrt(n) - 1) log2n <= n
        log2n = floor(log2(self.width))
        while log2n % 2 == 1 or 2 * (round(pow(2, log2n / 2)) - 1) * log2n > self.width:
            log2n -= 1
        t = round(log2n * log2n)
        for i in range(ceil(self.width / (self.size * t))):
            self.generate_y_part(M[:, i * self.size * t:], x[i * t * self.size:], c, i, t, z)

    def generate_y_part(self, Y_part, x, c, index, length, z):
        """ :: apply Corollary 3 to make (x, z, 0) -> (x, (T_part)z, 0)

        time complex: \tilde{O}(sn)
        depth : O(logn)

        Args:
            Y_part(np.matrix): n * n, matrix in F_2. We only use the part
                            Y_part[: , :slog^2n]
            x(list<int>): the indexes of first register, we only use x[:slog^2n]
            c(list<int>): the indexes of ancillary register, length is 3 * s * n
            index(int): the index of the Y part
            length(int): the reality value for log^2n
            z(list<int>): the indexes of second register, length is n
        """
        # operate R_a in Corollary 3
        init_len = len(self.CNOT)
        for i in range(self.size):
            if index * length * self.size + i * length < self.width:
                self.generate_y_base(Y_part[:, i * length:], c[i * 3 * self.width:], length, x[i * length:])
        end_len = len(self.CNOT)
        # operate Add in Corollary 3
        for i in range(self.size):
            for j in range(self.width):
                self.CNOT.append((c[i * 3 * self.width + j], z[j]))
        # operate R_a^{-1} in Corollary 3
        self.inverse_gates(init_len, end_len)

    def generate_y_base(self, Y_part, c, length, x):
        """ Apply Lemma 6 to copy part of Y_part in ancillary register

        We generator Y_part[:, :log^2n]
        to c[:n] with the help of c[n :  3 * n]
        time complex: \tilde{O}(n)
        depth : O(logn)

        Args:
            Y_part(np.matrix): Y_part
            c(list<int>): indexes of ancillary register,
            length: the value of log^2n
            x(list<int>): indexes of first register, length is log^2n

        """
        # ancillary qubits in Lemma 6
        ancillary = c[self.width: 3 * self.width]
        # goal qubits in Lemma 6
        ystart = c[:self.width]
        d2logn = int(floor(round(sqrt(length)) / 2))
        sqrtn = int(pow(2, d2logn))
        # real length
        length = min(length, np.shape(Y_part)[1])

        Step1_start = len(self.CNOT)
        for j in range(ceil(length / d2logn)):
            # Step 1 Construct Pj's (Lemma 5)
            cols = min(d2logn, length - j * d2logn)
            r_sqrtn = int(pow(2, cols))
            self.construct_pj(ancillary[sqrtn + sqrtn * d2logn * j // 2:], x[j * d2logn:],
                              ancillary[j * (sqrtn - 1):], r_sqrtn, cols)
        Step1_end = len(self.CNOT)

        pointer = self.width
        for k in range(ceil(length / d2logn)):
            # Step 2 Copy rows in Pj's
            Step2_start = len(self.CNOT)
            cols = min(d2logn, length - k * d2logn)
            r_sqrtn = int(pow(2, cols))
            sl = [0] * (r_sqrtn - 1)
            sl_origin = [[] * 0 for _ in range(r_sqrtn - 1)]
            for u in range(self.width):
                l = 0
                for i in range(cols):
                    if Y_part[u, d2logn * k + i]:
                        l += 1 << i
                if l == 0:
                    continue
                sl[l - 1] += 1
            for i in range(1, r_sqrtn):
                if sl[i - 1] > 0:
                    total = ceil(sl[i - 1] / (4 * d2logn)) - 1
                    number_a = 1
                    now = k * (sqrtn - 1) + i - 1
                    sl_origin[i - 1].append((4 * d2logn, now))
                    while total > 0:
                        for _ in range(number_a):
                            self.CNOT.append((ancillary[now], ancillary[pointer]))
                            sl_origin[i - 1].append((4 * d2logn, pointer))
                            pointer += 1
                            total -= 1
                            if total == 0:
                                break
                            self.CNOT.append((ancillary[now], ancillary[pointer]))
                            sl_origin[i - 1].append((4 * d2logn, pointer))
                            pointer += 1
                            total -= 1
                            if total == 0:
                                break
                            if now == k * (sqrtn - 1) + i - 1:
                                now = pointer - 2
                            else:
                                now += 1
            Step2_end = len(self.CNOT)
            # Step 3
            for u in range(self.width):
                l = 0
                for i in range(cols):
                    if Y_part[u, d2logn * k + i]:
                        l += 1 << i
                if l == 0:
                    continue
                l -= 1
                assert len(sl_origin[l]) > 0
                if sl_origin[l][0][0] == 0:
                    sl_origin[l] = sl_origin[l][1:]
                assert len(sl_origin[l]) > 0
                sl_origin[l][0] = (sl_origin[l][0][0] - 1, sl_origin[l][0][1])
                self.CNOT.append((ancillary[sl_origin[l][0][1]], ystart[u]))
            # Step 4.1 restore of Step2
            self.inverse_gates(Step2_start, Step2_end)
        # Step 4.2 restore of Step1
        self.inverse_gates(Step1_start, Step1_end)

    def construct_pj(self, c, x, z, sqrtn, d2logn):
        """
        Apply Lemma 5 to make (x, z, 0) -> (x, (Pj)z, 0)$$
        Pj is the sqrt(n) * logn/2 matrix go through F_2^{logn / 2}

        Args:
            c(list<int>): the indexes of ancillae, length is sqrt(n) * log2n / 2
            x(list<int>): the indexes of first register, length is log2n / 2
            z(list<int>): the indexes of second register, length is log2n / 2
            sqrtn(int)  : the value of sqrt(n)
            d2logn(int) : the value of logn / 2
        """
        t = []
        total = 0
        first = 0

        start = len(self.CNOT)
        for j in range(d2logn):
            tj = 0
            for i in range(1, sqrtn):
                if i & (1 << j):
                    tj += 1
            total += tj
            t.append(total - 1)
            if tj > 0:
                tj -= 1
                self.CNOT.append((x[j], c[first]))
                now = first
                first += 1
                number_a = 1
                while tj > 0:
                    for i in range(number_a):
                        self.CNOT.append((c[now + i], c[first]))
                        first += 1
                        tj -= 1
                        if tj == 0:
                            break
                        self.CNOT.append((c[now + i], c[first]))
                        first += 1
                        tj -= 1
                        if tj == 0:
                            break
        end = len(self.CNOT)
        for j in range(d2logn):
            for i in range(1, sqrtn):
                if i & (1 << j):
                    self.CNOT.append((c[t[j]], z[i - 1]))
                    t[j] -= 1
        self.inverse_gates(start, end)

    def inverse_gates(self, start, end):
        """ apply the inverse of gate list in CNOT[start:end] on the circuit

        Args:
            start(int): the start index of interval
            end(int): the end index of interval
        """

        for i in range(end - 1, start - 1, -1):
            self.CNOT.append((self.CNOT[i][0], self.CNOT[i][1]))

    @staticmethod
    def inverse_matrix_f2(mat, n):
        """ get the inverse matrix of mat in F_2

        Args:
            mat(np.ndarray): the matrix in F_2
            n(int): the size of the matrix

        Returns:
            np.ndarray: the inverse of mat in F_2
        """
        b = np.zeros(2 * n * n, dtype=bool).reshape(n, 2 * n)
        for i in range(n):
            for j in range(n):
                b[i][j] = mat[i][j]
                b[i][j + n] = False
            b[i][i + n] = True
        for i in range(n):
            if not b[i][i]:
                flag = False
                for j in range(i + 1, n):
                    if b[j][i]:
                        flag = True
                        for t in range(2 * n):
                            b[j][t], b[i][t] = b[i][t], b[j][t]
                if not flag:
                    return False
            for j in range(i + 1, n):
                if b[j][i]:
                    for t in range(2 * n):
                        b[j][t] = b[j][t] ^ b[i][t]
        for i in range(n):
            for j in range(n):
                b[i][j] = b[i][j + n]
        return b[:, :n]
