#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/11/12 6:33
# @Author  : Han Yu
# @File    : MCT_Linear_Simulation.py

from QuICT.core import *
from QuICT.core.gate import *


class MCTLinearHalfDirtyAux(object):
    def execute(self, m: int, n: int):
        """ A linear simulation for Toffoli gate

        https://arxiv.org/abs/quant-ph/9503016 Lemma 7.2

        Implement a m-bit toffoli gate in a qureg with n qubit with linear complexity.

        If n ≥ 5 and m ∈ {3, . . . , ⌈n/2⌉} then (m+1)-Toffoli gate can be simulated
        by a network consisting of 4(m - 2) toffoli gates

        Args:
            m(int): the number of control qubits of the toffoli
            n(int): the number of qubits in the qureg

        Returns:
            CompositeGate: the result of Decomposition
        """
        if m > (n // 2) + (1 if n % 2 == 1 else 0):
            raise Exception("control bit cannot above ceil(n/2)")
        if m < 1:
            raise Exception("there must be at least one control bit")

        controls = [i for i in range(m)]
        auxs = [i for i in range(m, n - 1)]
        target = n - 1

        return self.assign_qubits(n, m, controls, auxs, target)

    @staticmethod
    def assign_qubits(n: int, m: int, controls: list, auxs: list, target: int):
        """
        Args:
            n(int): the number of qubits in the qureg
            m(int): the number of control qubits of the toffoli
            controls(list): list of control qubits
            auxs(list): list of ancillas
            target(int): target qubit

        Returns:
            CompositeGate: the result of Decomposition
        """
        gates = CompositeGate()
        with gates:
            qubit_list = controls + auxs + [target]
            if m == 1:
                CX & [qubit_list[0], qubit_list[n - 1]]
            elif m == 2:
                CCX & [qubit_list[0], qubit_list[1], qubit_list[n - 1]]
            else:
                for i in range(m, 2, -1):
                    CCX & [qubit_list[i - 1], qubit_list[n - 1 - (m - i + 1)], qubit_list[n - 1 - (m - i)]]
                CCX & [qubit_list[0], qubit_list[1], qubit_list[n - m + 1]]
                for i in range(3, m + 1):
                    CCX & [qubit_list[i - 1], qubit_list[n - 1 - (m - i + 1)], qubit_list[n - 1 - (m - i)]]

                for i in range(m - 1, 2, -1):
                    CCX & [qubit_list[i - 1], qubit_list[n - 1 - (m - i + 1)], qubit_list[n - 1 - (m - i)]]
                CCX & [qubit_list[0], qubit_list[1], qubit_list[n - m + 1]]
                for i in range(3, m):
                    CCX & [qubit_list[i - 1], qubit_list[n - 1 - (m - i + 1)], qubit_list[n - 1 - (m - i)]]

        return gates


class MCTLinearOneDirtyAux(object):
    def execute(self, n):
        """ A linear simulation for Toffoli gate

        https://arxiv.org/abs/quant-ph/9503016 Corollary 7.4

        Implement an n-bit toffoli gate in a qureg with n + 2 qubits with linear complexity.

        On an n-bit circuit, an (n-2)-bit toffoli gate can be simulated by
        8(n-5) CCX gates, with 1 bit dirty ancilla.

        Args:
            n(int): the number of used qubit, which is (n + 2) for n-qubit Toffoli gates

        Returns:
            CompositeGate: the result of Decomposition
        """
        if n < 3:
            raise Exception("there must be at least one control bit")

        controls = list(range(n - 2))
        target = n - 2
        aux = n - 1     # this is a dirty ancilla

        gates = CompositeGate()
        with gates:
            n = len(controls) + 2
            if n == 5:
                CCX & [controls[0], controls[1], aux]
                CCX & [controls[2], aux, target]
                CCX & [controls[0], controls[1], aux]
                CCX & [controls[2], aux, target]
                return gates
            if n == 4:
                CCX & [controls[0], controls[1], target]
                return gates
            if n == 3:
                CX & [controls[0], target]
                return gates
            # n > 5
            m = n // 2
            MCT_half_dirty = MCTLinearHalfDirtyAux()
            gates_first = MCT_half_dirty.assign_qubits(n, m, controls[0:m], controls[m:n - 2] + [target], aux)
            gates_last = MCT_half_dirty.assign_qubits(n, n - m - 1, controls[m:n - 2] + [aux], controls[0:m], target)
            if n - m == 3:  # n == 6
                gates_first | gates
                CCX & [controls[m], aux, target]
                gates_first | gates
                CCX & [controls[m], aux, target]
            else:
                gates_first | gates
                gates_last | gates
                gates_first | gates
                gates_last | gates

        return gates
