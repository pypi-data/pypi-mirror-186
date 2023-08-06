#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/3/20 4:44 下午
# @Author  : Han Yu    Dang Haoran    Cai Chao
# @File    : two_qubit_gate_rules.py

import numpy as np

from QuICT.core.gate import *

"""
the file describe transform rules between two kinds of 2-qubit gates.
"""
"""
transform CX gate into others
"""


def cx2cy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S & targs[1]
        CY & targs
        S_dagger & targs[1]
    return gates


def cx2cz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[1]
        CZ & targs
        H & targs[1]
    return gates


def cx2ch_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
    return gates


def cx2crz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Rz(np.pi / 2) & targs[0]
        H & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
    return gates


def cx2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[1]
        FSim(0, np.pi) & targs
        H & targs[1]
    return gates


def cx2rxx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
    return gates


def cx2ryy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(3 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[1]
        Ryy(np.pi / 2) & targs
        Rx(np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


def cx2rzz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        H & targs[0]
        H & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


"""
transform CY gate into others
"""


def cy2cx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S_dagger & targs[1]
        CX & [targs[0], targs[1]]
        S & targs[1]
    return gates


def cy2cz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S_dagger & targs[1]
        H & targs[1]
        CZ & targs
        H & targs[1]
        S & targs[1]
    return gates


def cy2ch_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        T_dagger & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T & targs[1]
    return gates


def cy2crz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Rz(np.pi / 2) & targs[0]
        S_dagger & targs[1]
        H & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
        S & targs[1]
    return gates


def cy2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S_dagger & targs[1]
        H & targs[1]
        FSim(0, np.pi) & targs
        H & targs[1]
        S & targs[1]
    return gates


def cy2rxx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        S_dagger & targs[1]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        S & targs[1]
    return gates


def cy2ryy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(3 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Ryy(np.pi / 2) & targs
        Rx(np.pi) & targs[1]
        H & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


def cy2rzz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        H & targs[0]
        Rx(np.pi / 2) & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
        S & targs[1]
    return gates


"""
transform CZ gate into others
"""


def cz2cx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[1]
        CX & [targs[0], targs[1]]
        H & targs[1]
    return gates


def cz2cy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[1]
        S & targs[1]
        CY & targs
        S_dagger & targs[1]
        H & targs[1]
    return gates


def cz2ch_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
        CH & targs
        S & targs[1]
        Rx(np.pi / 4) & targs[1]
    return gates


def cz2crz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Rz(np.pi / 2) & targs[0]
        CRz(np.pi) & targs
    return gates


def cz2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        FSim(0, np.pi) & targs
    return gates


def cz2rxx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 4) & targs[0]
        H & targs[1]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        H & targs[1]
    return gates


def cz2ryy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Rz(-np.pi / 2) & targs[1]
        Rx(-np.pi / 2) & targs[1]
        Ryy(np.pi / 2) & targs
        Rx(np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


def cz2rzz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 4) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        H & targs[0]
        Rz(-np.pi / 2) & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


"""
transform CRz gate into others
"""


def crz2cx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        """decomposition1:"""
        Rz(theta / 2) & targs[1]
        CX & targs
        Rz(-theta / 2) & targs[1]
        CX & targs
        """decomposition2:
        U1(theta / 2) & targs[1]
        CX & targs
        U1(-theta / 2) & targs[1]
        CX & targs
        """
    return gates


def crz2cy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Rz((theta + np.pi) / 2) & targs[1]
        CY & targs
        Rz(-theta / 2) & targs[1]
        CY & targs
        S_dagger & targs[1]
    return gates


def crz2cz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rz(theta / 2) & targs[1]
        H & targs[1]
        CZ & targs
        Rx(-theta / 2) & targs[1]
        CZ & targs
        H & targs[1]
    return gates


def crz2ch_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 8) & targs[0]
        Rz(theta / 2 + np.pi / 4) & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Ry(theta / 2) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
    return gates


def crz2fsim_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rz(theta / 2) & targs[1]
        H & targs[1]
        FSim(0, np.pi) & targs
        Rx(-theta / 2) & targs[1]
        FSim(0, np.pi) & targs
        H & targs[1]
    return gates


def crz2rxx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(3 * np.pi / 2) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        U1(theta / 2) & targs[1]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        U1(-theta / 2) & targs[1]
        Rx(-np.pi / 2) & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
    return gates


def crz2ryy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi) & targs[0]
        Rz(theta / 2 + np.pi / 2) & targs[1]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Ryy(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        Rx(np.pi - theta / 2) & targs[1]
        H & targs[1]
        Ryy(np.pi / 2) & targs
        Rx(np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


def crz2rzz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rz(theta / 2 + np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[1]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        H & targs[0]
        Rzz(np.pi / 2) & targs
        Rz(-np.pi / 2) & targs[0]
        Rx(-theta / 2) & targs[1]
        Rz(-np.pi / 2) & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
    return gates


"""
transform CH gate into others
"""


def ch2cx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
        CX & targs
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
    return gates


def ch2cy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(-np.pi / 2) & targs[1]
        Rz(np.pi / 4) & targs[1]
        CY & targs
        Rz(-np.pi / 4) & targs[1]
        Rx(np.pi / 2) & targs[1]
    return gates


def ch2cz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S & targs[1]
        Rx(np.pi / 4) & targs[1]
        CZ & targs
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
    return gates


def ch2crz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 4) & targs[0]
        Rz(np.pi / 2) & targs[0]
        S & targs[1]
        Rx(np.pi / 4) & targs[1]
        CRz(np.pi) & targs
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
    return gates


def ch2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S & targs[1]
        Rx(np.pi / 4) & targs[1]
        FSim(0, np.pi) & targs
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
    return gates


def ch2rxx_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(13 * np.pi / 8) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi) & targs[1]
        Ry(-np.pi / 4) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
    return gates


def ch2ryy_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rz(np.pi / 4) & targs[1]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Ryy(np.pi / 2) & targs
        Rx(np.pi / 2) & targs[0]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
        Rx(np.pi / 4) & targs[1]
        S_dagger & targs[1]
    return gates


def ch2rzz_rule(gate):
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(3 * np.pi / 2) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        H & targs[0]
        Ry(np.pi / 4) & targs[1]
        Rx(-np.pi) & targs[1]
        H & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
    return gates


"""
transform Rxx gate into others
"""


def rxx2cx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        H & targs[1]
        CX & targs
        Rz(theta) & targs[1]
        CX & targs
        H & targs[1]
        H & targs[0]
    return gates


def rxx2cy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        H & targs[1]
        S & targs[1]
        CY & targs
        Rz(theta) & targs[1]
        CY & targs
        S_dagger & targs[1]
        H & targs[1]
        H & targs[0]
    return gates


def rxx2cz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        CZ & targs
        Rx(theta) & targs[1]
        CZ & targs
        H & targs[0]
    return gates


def rxx2ch_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        Rx(-np.pi / 4) & targs[1]
        S_dagger & targs[1]
        CH & targs
        Ry(-theta) & targs[1]
        CH & targs
        S & targs[1]
        Rx(np.pi / 4) & targs[1]
        H & targs[0]
    return gates


def rxx2crz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 2) & targs[0]
        H & targs[0]
        Rz(np.pi) & targs[0]
        CRz(np.pi) & targs
        Rx(theta) & targs[1]
        CRz(np.pi) & targs
        H & targs[0]
    return gates


def rxx2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    theta = gate.pargs[0]
    gates = CompositeGate()
    with gates:
        H & targs[0]
        FSim(0, np.pi) & targs
        Rx(theta) & targs[1]
        FSim(0, np.pi) & targs
        H & targs[0]
    return gates


def rxx2ryy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        Rx(-np.pi / 2) & targs[0]
        H & targs[1]
        Rx(-np.pi / 2) & targs[1]
        Ryy(theta) & targs
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[0]
    return gates


def rxx2rzz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[0]
        H & targs[1]
        Rzz(theta) & targs
        H & targs[1]
        H & targs[0]
    return gates


"""
transform Ryy gate into others
"""


def ryy2cx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        CX & targs
        Rz(theta) & targs[1]
        CX & targs
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
    return gates


def ryy2cy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        S & targs[1]
        CY & targs
        Rz(theta) & targs[1]
        CY & targs
        S_dagger & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
    return gates


def ryy2cz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        CZ & targs
        Rx(theta) & targs[1]
        CZ & targs
        H & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
    return gates


def ryy2ch_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Ry(np.pi / 4) & targs[1]
        Rx(np.pi) & targs[1]
        CH & targs
        Ry(-theta) & targs[1]
        CH & targs
        Rx(-np.pi) & targs[1]
        Ry(-np.pi / 4) & targs[1]
        Rx(-np.pi / 2) & targs[0]
    return gates


def ryy2crz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        Rz(np.pi) & targs[0]
        CRz(np.pi) & targs
        Rx(theta) & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
    return gates


def ryy2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    theta = gate.pargs[0]
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        FSim(0, np.pi) & targs
        Rx(theta) & targs[1]
        FSim(0, np.pi) & targs
        H & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
    return gates


def ryy2rxx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        """Decomposition1:"""
        GPhase(7 * np.pi / 2) & targs[0]
        Rz(-np.pi / 2) & targs[0]
        Rxx(np.pi / 2) & targs
        Rz(theta) & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        """Decomposition2:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[0]
        H & targs[1]
        Rxx(theta) & targs
        H & targs[1]
        H & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rx(-np.pi / 2) & targs[0]
        """
    return gates


def ryy2rzz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        Rzz(theta) & targs
        Rx(-np.pi / 2) & targs[1]
        Rx(-np.pi / 2) & targs[0]
    return gates


"""
transform Rzz gate into others
"""


def rzz2cx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        CX & targs
        Rz(theta) & targs[1]
        CX & targs
    return gates


def rzz2cy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        S & targs[1]
        CY & targs
        Rz(theta) & targs[1]
        CY & targs
        S_dagger & targs[1]
    return gates


def rzz2cz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        H & targs[1]
        CZ & targs
        Rx(theta) & targs[1]
        CZ & targs
        H & targs[1]
    return gates


def rzz2ch_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Ry(-theta) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
    return gates


def rzz2crz_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(np.pi / 2) & targs[0]
        H & targs[1]
        Rz(np.pi) & targs[0]
        CRz(np.pi) & targs
        Rx(theta) & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
    return gates


def rzz2fsim_rule(gate):
    targs = gate.cargs + gate.targs
    theta = gate.pargs[0]
    gates = CompositeGate()
    with gates:
        H & targs[1]
        FSim(0, np.pi) & targs
        Rx(theta) & targs[1]
        FSim(0, np.pi) & targs
        H & targs[1]
    return gates


def rzz2rxx_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(7 * np.pi / 2) & targs[0]
        Ry(np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Rz(theta) & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
    return gates


def rzz2ryy_rule(gate):
    theta = gate.pargs[0]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Ryy(theta) & targs
        Rx(np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[0]
    return gates


"""
transform Fsim gate into others
"""


def fsim2cx_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4) & targs[0]
        CX & targs
        H & targs[0]
        CX & [targs[1], targs[0]]
        Rz(-theta) & targs[0]
        CX & [targs[1], targs[0]]
        Rz(theta) & targs[0]
        H & targs[0]
        CX & targs
        U1(-fai / 2) & targs[1]
        CX & targs
        U1(fai / 2) & targs[1]
        CX & targs
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2cy_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4 - np.pi / 4) & targs[0]
        S & targs[1]
        CY & targs
        H & targs[0]
        S & targs[0]
        CY & [targs[1], targs[0]]
        Rz(-theta) & targs[0]
        CY & [targs[1], targs[0]]
        Rz(theta - np.pi / 2) & targs[0]
        H & targs[0]
        CY & targs
        U1(-fai / 2) & targs[1]
        CY & targs
        U1(fai / 2) & targs[1]
        CY & targs
        S_dagger & targs[1]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2cz_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4) & targs[0]
        H & targs[1]
        CZ & targs
        H & targs[1]
        CZ & [targs[1], targs[0]]
        Rx(-theta) & targs[0]
        CZ & [targs[1], targs[0]]
        Rx(theta) & targs[0]
        H & targs[1]
        CZ & targs
        Rx(-fai / 2) & targs[1]
        CZ & targs
        Rx(fai / 2) & targs[1]
        CZ & targs
        H & targs[1]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2ch_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4) & targs[0]
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
        Rx(-np.pi / 4) & targs[0]
        S_dagger & targs[0]
        CH & [targs[1], targs[0]]
        Ry(theta) & targs[0]
        CH & [targs[1], targs[0]]
        S & targs[0]
        Rx(theta + np.pi / 4) & targs[0]
        T & targs[1]
        Rx(np.pi / 2) & targs[1]
        CH & targs
        Ry(fai / 2) & targs[1]
        CH & targs
        Ry(-fai / 2) & targs[1]
        CH & targs
        Rx(-np.pi / 2) & targs[1]
        T_dagger & targs[1]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2crz_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4 - np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        H & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
        Rz(np.pi / 2) & targs[1]
        CRz(np.pi) & [targs[1], targs[0]]
        Rz(np.pi / 2) & targs[1]
        Rx(-theta) & targs[0]
        CRz(np.pi) & [targs[1], targs[0]]
        Rx(theta) & targs[0]
        Rz(np.pi / 2) & targs[0]
        H & targs[1]
        CRz(np.pi) & targs
        Rz(np.pi / 2) & targs[0]
        Rx(-fai / 2) & targs[1]
        CRz(np.pi) & targs
        Rz(np.pi / 2) & targs[0]
        Rx(fai / 2) & targs[1]
        CRz(np.pi) & targs
        H & targs[1]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2rxx_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 2 - np.pi / 2) & targs[0]
        Rxx(theta) & targs
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[0]
        H & targs[1]
        Rxx(theta) & targs
        H & targs[0]
        Rx(-np.pi) & targs[0]
        Rz(-np.pi / 2) & targs[0]
        H & targs[1]
        Rx(-np.pi) & targs[1]
        Ry(-fai / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        U1(fai / 2) & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Rxx(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2ryy_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 4 + np.pi / 2) & targs[0]
        H & targs[0]
        H & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Rx(-np.pi / 2) & targs[1]
        Ryy(theta) & targs
        Rx(np.pi / 2) & targs[1]
        Rx(np.pi / 2) & targs[0]
        H & targs[1]
        H & targs[0]
        Ryy(theta) & targs
        Rz(np.pi / 2 + -fai / 2) & targs[1]
        Ry(np.pi / 2) & targs[0]
        Rz(np.pi / 2) & targs[0]
        Ryy(np.pi / 2) & targs
        Ry(-np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        Rz(np.pi / 2 + fai / 2) & targs[1]
        Ryy(np.pi / 2) & targs
        Rx(np.pi / 2) & targs[1]
        H & targs[1]
        Rx(-np.pi / 2) & targs[0]
        Ry(-np.pi) & targs[0]
        Rz(-fai / 2) & targs[0]
    return gates


def fsim2rzz_rule(gate):
    theta = gate.pargs[0]
    fai = gate.pargs[1]
    targs = gate.cargs + gate.targs
    gates = CompositeGate()
    with gates:
        GPhase(-fai / 2 - np.pi / 2) & targs[0]
        H & targs[0]
        H & targs[1]
        Rzz(theta) & targs
        H & targs[1]
        H & targs[0]
        Rx(np.pi / 2) & targs[0]
        Rx(np.pi / 2) & targs[1]
        Rzz(theta) & targs
        Rx(-np.pi) & targs[0]
        Rz(-np.pi / 2) & targs[0]
        H & targs[0]
        Rx(-np.pi) & targs[1]
        Ry(-fai / 2) & targs[1]
        H & targs[1]
        Rzz(np.pi / 2) & targs
        Rz(-np.pi / 2) & targs[0]
        H & targs[1]
        U1(fai / 2) & targs[1]
        Rx(-np.pi / 2) & targs[1]
        H & targs[1]
        Rzz(np.pi / 2) & targs
        H & targs[1]
        H & targs[0]
        Ry(-np.pi / 2) & targs[0]
        Rz(-fai / 2) & targs[0]
    return gates
