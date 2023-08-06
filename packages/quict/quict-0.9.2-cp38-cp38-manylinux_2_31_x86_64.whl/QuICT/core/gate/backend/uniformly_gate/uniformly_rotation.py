#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/12/27 10:45 下午
# @Author  : Han Yu
# @File    : uniformRotation.py

from typing import *
import numpy as np

from QuICT.core.gate import GateType, build_gate, CompositeGate, CX


class UniformlyRotation(object):
    """
    Implements the uniformly Ry or Rz gate

    Reference:
        https://arxiv.org/abs/quant-ph/0504100 Fig4 a)
    """
    def __init__(self, gate_type=None):
        """
        Args:
            gate_type(GateType): the type of uniformly gate, Ry or Rz
        """
        assert gate_type in [GateType.ry, GateType.rz], ValueError('Invalid gate_type')
        self.gate_type = gate_type

    def execute(self, angle_list):
        """
        Args:
            angle_list(list<float>): the angles of Ry or Rz gates

        Returns:
            CompositeGate: CompositeGate that implements the uniformly gate
        """
        angle_list = list(angle_list)
        n = int(np.log2(len(angle_list))) + 1
        if 1 << (n - 1) != len(angle_list):
            raise Exception("the number of parameters unmatched.")
        return self.uniformly_rotation(0, n, angle_list, self.gate_type)

    def uniformly_rotation(
        self,
        low: int,
        high: int,
        angles: List[float],
        gate_type: int,
        is_left_cnot: bool = False
    ) -> CompositeGate:
        """
        synthesis uniformlyRotation gate, bits range [low, high)

        Args:
            low(int): the left range low
            high(int): the right range high
            angles(list<float>): the list of angle y
            gate_type(int): the gateType (Rz or Ry)
            is_left_cnot(bool): is cnot left decomposition
        Returns:
            gateSet: the synthesis gate list
        """
        return self.inner_uniformly_rotation(low, high, angles, gate_type, True, is_left_cnot)

    def inner_uniformly_rotation(
        self,
        low: int,
        high: int,
        angles: List[float],
        gate_type: int,
        is_first_level: bool,
        is_left_cnot: bool = False
    ) -> CompositeGate:
        if low + 1 == high:
            rot = build_gate(gate_type, low, [angles[0].real])
            gates = CompositeGate()
            gates.append(rot)
            return gates
        length = len(angles) // 2
        Rxp = []
        Rxn = []
        for i in range(length):
            Rxp.append((angles[i] + angles[i + length]) / 2)
            Rxn.append((angles[i] - angles[i + length]) / 2)
        if is_first_level:
            if is_left_cnot:
                gates = CompositeGate()
                CX & [low, high - 1] | gates
                gates.extend(self.inner_uniformly_rotation(low + 1, high, Rxn, gate_type, False, False))
                CX & [low, high - 1] | gates
                gates.extend(self.inner_uniformly_rotation(low + 1, high, Rxp, gate_type, False, True))
            else:
                gates = self.inner_uniformly_rotation(low + 1, high, Rxp, gate_type, False, False)
                CX & [low, high - 1] | gates
                gates.extend(self.inner_uniformly_rotation(low + 1, high, Rxn, gate_type, False, True))
                CX & [low, high - 1] | gates
        elif is_left_cnot:
            gates = self.inner_uniformly_rotation(low + 1, high, Rxn, gate_type, False, False)
            CX & [low, high - 1] | gates
            gates.extend(self.inner_uniformly_rotation(low + 1, high, Rxp, gate_type, False, True))
        else:
            gates = self.inner_uniformly_rotation(low + 1, high, Rxp, gate_type, False, False)
            CX & [low, high - 1] | gates
            gates.extend(self.inner_uniformly_rotation(low + 1, high, Rxn, gate_type, False, True))
        return gates
