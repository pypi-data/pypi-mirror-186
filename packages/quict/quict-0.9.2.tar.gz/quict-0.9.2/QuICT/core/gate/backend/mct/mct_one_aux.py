#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/11/12 11:37
# @Author  : Han Yu
# @File    : MCT_one_aux.py

from QuICT.core import *
from QuICT.core.gate import *
from .mct_linear_dirty_aux import MCTLinearHalfDirtyAux


class MCTOneAux(object):
    def execute(self, n):
        """ Decomposition of n-qubit Toffoli gates with one ancillary qubit and linear circuit complexity

        He Y, Luo M X, Zhang E, et al.
        Decompositions of n-qubit Toffoli gates with linear circuit complexity[J].
        International Journal of Theoretical Physics, 2017, 56(7): 2350-2361.

        Args:
            n(int): the number of used qubit, which is (n + 2) for n-qubit Toffoli gates

        Returns:
            CompositeGate: the result of Decomposition
        """
        n = n - 1
        gates = CompositeGate()
        qubit_list = list(range(n + 1))
        with gates:
            if n == 3:
                CCX & qubit_list[:3]
                return gates
            elif n == 2:
                CX & qubit_list[:2]
                return gates
            k = n // 2 + n % 2

            MCT_half_dirty = MCTLinearHalfDirtyAux()
            half_dirty_gates = MCT_half_dirty.execute(k, n + 1)

            qubit_remain = qubit_list[k:k + n // 2] + qubit_list[:k] + [qubit_list[-1]]
            if n // 2 < 1:
                raise Exception("there must be at least one control bit")
            controls_remain = [qubit_remain[i] for i in range(n // 2)]
            auxs_remain = [qubit_remain[i] for i in range(n // 2, n)]
            gates_remain = MCT_half_dirty.assign_qubits(n + 1, n // 2, controls_remain, auxs_remain, n)

            half_dirty_gates | gates
            H & qubit_list[-2]
            S & qubit_list[-1]
            gates_remain | gates
            S_dagger & qubit_list[-1]
            half_dirty_gates | gates
            S & qubit_list[-1]
            gates_remain | gates
            H & qubit_list[-2]
            S_dagger & qubit_list[-1]

        return gates
