"""
Decomposition of uniformly-Ry gate, which is specially designed for
the optimization of unitary transform
"""

from typing import *
import numpy as np

from QuICT.core.gate import CompositeGate, CX, CZ, Ry


class UniformlyRyRevision(object):
    def __init__(self, is_cz_left: bool = False):
        self.is_cz_left = is_cz_left

    def execute(self, angle_list):
        """ uniformlyRyGate

        http://cn.arxiv.org/abs/quant-ph/0504100v1 Fig4 a)
        This part is mainly copied from ../uniformly_gate/uniformly_rotation.py
        Here we demand a CZ gate at the edge of the decomposition, therefore the
        recursion process is slightly revised.

        If qubit_num > 2, synthesized gates would have 2 cz gates at rightmost place.
        If qubit_num == 2, there would be only 1 cz gate.

        Args:
            angle_list(list<float>): the angles of Ry Gates

        Returns:
            CompositeGate: the synthesis gate list
        """
        angle_list = list(angle_list)
        n = int(np.round(np.log2(len(angle_list)))) + 1
        if 1 << (n - 1) != len(angle_list):
            raise Exception("the number of parameters unmatched.")
        return self.uniformly_rotation_cz(0, n, angle_list, self.is_cz_left)

    def uniformly_rotation_cz(
        self,
        low: int,
        high: int,
        angles: List[float],
        is_cz_left: bool = False
    ) -> CompositeGate:
        """
        synthesis uniformlyRy gate, bits range [low, high)

        Args:
            low(int): the left range low
            high(int): the right range high
            angles(list<float>): the list of angle y
            mapping(list<int>): the qubit order of gate
            is_cz_left(bool): is cx/cz left decomposition
        Returns:
            gateSet: the synthesis gate list
        """
        return self.inner_uniformly_rotation_cz(low, high, angles, True, is_cz_left)

    def inner_uniformly_rotation_cz(
        self,
        low: int,
        high: int,
        angles: List[float],
        is_first_level: bool,
        is_cz_left: bool = False
    ) -> CompositeGate:
        if low + 1 == high:
            gates = CompositeGate()
            with gates:
                Ry(angles[0].real) & low
            return gates
        length = len(angles) // 2
        Rxp = []
        Rxn = []
        for i in range(length):
            Rxp.append((angles[i] + angles[i + length]) / 2)
            Rxn.append((angles[i] - angles[i + length]) / 2)
        if is_first_level:
            if is_cz_left:
                gates = CompositeGate()
                with gates:
                    CZ & [low, high - 1]
                    # if high - low == 2, no CZ is needed here
                    if high - low > 2:
                        CZ & [low, low + 1]
                gates.extend(self.inner_uniformly_rotation_cz(low + 1, high, Rxn, False, False))
                with gates:
                    # CZ & [low, high - 1]
                    Ry(np.pi / 2) & high - 1
                    CX & [low, high - 1]
                    Ry(-np.pi / 2) & high - 1
                    # The extra CZ derived from CCPhase can also be moved to the edge
                gates.extend(self.inner_uniformly_rotation_cz(low + 1, high, Rxp, False, True))
            else:
                gates = self.inner_uniformly_rotation_cz(low + 1, high, Rxp, False, False)
                with gates:
                    # CZ & [low, high - 1]
                    Ry(np.pi / 2) & high - 1
                    CX & [low, high - 1]
                    Ry(-np.pi / 2) & high - 1
                    # The extra CZ derived from CCPhase can also be moved to the edge
                gates.extend(self.inner_uniformly_rotation_cz(low + 1, high, Rxn, False, True))
                with gates:
                    CZ & [low, high - 1]
                    # if high - low == 2, no CZ is needed here
                    if high - low > 2:
                        CZ & [low, low + 1]
        elif is_cz_left:
            gates = self.inner_uniformly_rotation_cz(low + 1, high, Rxn, False, False)
            with gates:
                CX & [low, high - 1]
            gates.extend(self.inner_uniformly_rotation_cz(low + 1, high, Rxp, False, True))
        else:
            gates = self.inner_uniformly_rotation_cz(low + 1, high, Rxp, False, False)
            with gates:
                CX & [low, high - 1]
            gates.extend(self.inner_uniformly_rotation_cz(low + 1, high, Rxn, False, True))
        return gates
