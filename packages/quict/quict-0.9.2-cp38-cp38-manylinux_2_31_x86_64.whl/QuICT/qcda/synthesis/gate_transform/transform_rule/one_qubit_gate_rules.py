#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/3/20 4:42 下午
# @Author  : Han Yu
# @File    : SU2_rules.py

"""
the file describe transform rules that decompose SU(2) into instruction set.
"""

import numpy as np
from numpy import arccos, linalg

from QuICT.core.gate import *


def _arccos(value):
    """ calculate arccos(value)

    Args:
        value: the cos value

    Returns:
        float: the corresponding angle
    """
    if value < -1:
        value = -1
    elif value > 1:
        value = 1
    return arccos(value)


def _check2pi(theta, eps=1e-15):
    """ check whether theta is a multiple of 2π

    Args:
        theta(float): the angle to be checked
        eps(float): tolerate error

    Returns:
        bool: whether theta is a multiple of 2π
    """
    multiple = np.round(theta / (2 * np.pi))
    return abs(2 * np.pi * multiple - theta) < eps


def zyz_rule(gate):
    """ decomposition the unitary gate with 2 * 2 unitary into Rz Ry Rz sequence

    Args:
        gate(Unitary): the gate to be decomposed

    Returns:
        compositeGate: a list of compositeGate
    """
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-13

    det = linalg.det(unitary)
    beta_plus_delta = 0
    beta_dec_delta = 0
    if abs(det - 1) > eps:
        unitary[:] /= np.sqrt(det)

    if abs(unitary[0, 0]) > abs(unitary[0, 1]) > eps:
        gamma = _arccos((2 * (unitary[0, 0] * unitary[1, 1]).real - 1))
    else:
        gamma = _arccos((2 * (unitary[0, 1] * unitary[1, 0]).real + 1))
    if abs(unitary[0, 0]) > eps:
        beta_plus_delta = -np.angle(unitary[0, 0] / np.cos(gamma / 2)) * 2
    if abs(unitary[0, 1]) > eps:
        beta_dec_delta = np.angle(unitary[1, 0] / np.sin(gamma / 2)) * 2

    beta = (beta_plus_delta + beta_dec_delta) / 2
    delta = beta_plus_delta - beta
    gates = CompositeGate()
    with gates:
        if not _check2pi(delta):
            Rz(delta) & targ
        if not _check2pi(gamma):
            Ry(gamma) & targ
        if not _check2pi(beta):
            Rz(beta) & targ
    return gates


def xyx_rule(gate):
    """ decomposition the unitary gate with 2 * 2 unitary into Rx Ry Rx sequence

    Args:
        gate(Unitary): the gate to be decomposed

    Returns:
        compositeGate: a list of compositeGate
    """
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-13
    unitary = np.array([
        [0.5 * (unitary[0, 0] + unitary[0, 1] + unitary[1, 0] + unitary[1, 1]),
         0.5 * (unitary[0, 0] - unitary[0, 1] + unitary[1, 0] - unitary[1, 1])],
        [0.5 * (unitary[0, 0] + unitary[0, 1] - unitary[1, 0] - unitary[1, 1]),
         0.5 * (unitary[0, 0] - unitary[0, 1] - unitary[1, 0] + unitary[1, 1])]
    ], dtype=np.complex128)
    det = linalg.det(unitary)
    beta_plus_delta = 0
    beta_dec_delta = 0
    if abs(det - 1) > eps:
        unitary[:] /= np.sqrt(det)

    if abs(unitary[0, 0]) > abs(unitary[0, 1]) > eps:
        gamma = _arccos((2 * (unitary[0, 0] * unitary[1, 1]).real - 1))
    else:
        gamma = _arccos((2 * (unitary[0, 1] * unitary[1, 0]).real + 1))
    if abs(unitary[0, 0]) > eps:
        beta_plus_delta = -np.angle(unitary[0, 0] / np.cos(gamma / 2)) * 2
    if abs(unitary[0, 1]) > eps:
        beta_dec_delta = np.angle(unitary[1, 0] / np.sin(gamma / 2)) * 2

    beta = (beta_plus_delta + beta_dec_delta) / 2
    delta = beta_plus_delta - beta
    gates = CompositeGate()
    with gates:
        if not _check2pi(delta):
            Rx(delta) & targ
        if not _check2pi(gamma):
            Ry(-gamma) & targ
        if not _check2pi(beta):
            Rx(beta) & targ
    return gates


def ibmq_rule(gate):
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-13

    det = linalg.det(unitary)
    beta_plus_delta = 0
    beta_dec_delta = 0
    if abs(det - 1) > eps:
        unitary[:] /= np.sqrt(det)

    if abs(unitary[0, 0]) > abs(unitary[0, 1]) > eps:
        gamma = _arccos((2 * (unitary[0, 0] * unitary[1, 1]).real - 1))
    else:
        gamma = _arccos((2 * (unitary[0, 1] * unitary[1, 0]).real + 1))
    if abs(unitary[0, 0]) > eps:
        beta_plus_delta = -np.angle(unitary[0, 0] / np.cos(gamma / 2)) * 2
    if abs(unitary[0, 1]) > eps:
        beta_dec_delta = np.angle(unitary[1, 0] / np.sin(gamma / 2)) * 2

    beta = (beta_plus_delta + beta_dec_delta) / 2
    delta = beta_plus_delta - beta
    gates = CompositeGate()
    with gates:
        if not _check2pi(delta):
            Rz(delta) & targ
        if not _check2pi(gamma):
            SX & targ
            Rz(gamma) & targ
            SX & targ
            X & targ
        if not _check2pi(beta):
            Rz(beta) & targ
    return gates


def zxz_rule(gate):
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-13

    det = linalg.det(unitary)
    beta_plus_delta = 0
    beta_dec_delta = 0
    if abs(det - 1) > eps:
        unitary[:] /= np.sqrt(det)

    beta_plus_delta = 2 * np.angle(unitary[1, 1])
    beta_dec_delta = 2 * np.angle(unitary[1, 0]) + np.pi
    gamma = 2 * _arccos(np.abs(unitary[0, 0]))
    beta = (beta_plus_delta + beta_dec_delta) / 2
    delta = beta_plus_delta - beta

    gates = CompositeGate()
    with gates:
        if not _check2pi(delta):
            Rz(delta) & targ
        if not _check2pi(gamma):
            Rx(gamma) & targ
        if not _check2pi(beta):
            Rz(beta) & targ
    return gates


def hrz_rule(gate):
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-13

    det = linalg.det(unitary)
    beta_plus_delta = 0
    beta_dec_delta = 0
    if abs(det - 1) > eps:
        unitary[:] /= np.sqrt(det)

    beta_plus_delta = 2 * np.angle(unitary[1, 1])
    beta_dec_delta = 2 * np.angle(unitary[1, 0]) + np.pi
    gamma = 2 * _arccos(np.abs(unitary[0, 0]))
    beta = (beta_plus_delta + beta_dec_delta) / 2
    delta = beta_plus_delta - beta

    gates = CompositeGate()
    with gates:
        if not _check2pi(delta):
            Rz(delta) & targ
        if not _check2pi(gamma):
            H & targ
            Rz(gamma) & targ
            H & targ
        if not _check2pi(beta):
            Rz(beta) & targ
    return gates


def u3_rule(gate):
    unitary = gate.matrix
    targ = gate.targ
    eps = 1e-6

    # u3[0, 0] is real
    z = np.exp(1j * np.angle(unitary[0, 0]))
    unitary = unitary / z

    theta = np.arccos(unitary[0, 0])
    sint = np.sin(theta)
    if abs(sint) >= eps:
        lamda = np.angle(unitary[0, 1] / -sint)
        phi = np.angle(unitary[1, 0] / sint)
    else:
        lamda = 0
        phi = np.angle(unitary[1, 1] / np.cos(theta))

    if _check2pi(theta, eps):
        theta = 0
    if _check2pi(lamda, eps):
        lamda = 0
    if _check2pi(phi, eps):
        phi = 0
    g = build_gate(GateType.u3, targ, [theta * 2, phi, lamda])
    gates = CompositeGate(gates=[g])
    return gates
