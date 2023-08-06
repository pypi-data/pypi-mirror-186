#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/2/23 10:14 上午
# @Author  : Han Yu
# @File    : search_with_prior_knowledge.py

import numpy as np
from scipy.optimize import minimize

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.core.gate.backend import MCTOneAux
from QuICT.qcda.synthesis.quantum_state_preparation import QuantumStatePreparation

P_GLOBAL = []
T_GLOBAL = 1


def fun(x):
    return -np.dot(P_GLOBAL, np.sin((2 * T_GLOBAL + 1) * np.arcsin(np.sqrt(x)))**2)


def run_search_with_prior_knowledge(f, n, p, T, oracle):
    """ grover search for f with custom oracle

    Args:
        f(list<int>): the function to be decided
        n(int): the length of input
        p(list<float>): the distribute of priop probability
        T(int): the query times
        oracle(function): the oracle
    Returns:
        int: the a satisfies that f(a) = 1
    """
    global P_GLOBAL
    P_GLOBAL = p[:]
    global T_GLOBAL
    T_GLOBAL = T
    num = int(np.ceil(np.log2(n))) + 2
    # Determine number of qreg
    circuit = Circuit(num)
    qreg = circuit([i for i in range(num - 2)])
    ancilla = circuit(num - 2)
    empty = circuit(num - 1)
    cons = ({'type': 'ineq', 'fun': lambda x: 1 - np.dot(np.ones(n), x)},)
    bnd = [(0, np.sin(np.pi / (4 * T + 2))**2) for _ in range(n)]
    tmp = np.min([1 / n, np.sin(np.pi / (4 * T + 2))**2])
    x = np.array([tmp] * n)
    option = {'maxiter': 4, 'disp': False}
    res = minimize(fun, x, method='SLSQP', constraints=cons,
                   bounds=bnd, options=option)
    q = res.x

    # Start with qreg in equal superposition and ancilla in |->
    QSP = QuantumStatePreparation('uniformly_gates')
    gates_preparation = QSP.execute(list(q))

    MCTOA = MCTOneAux()
    gates_mct = MCTOA.execute(num)

    X | ancilla
    H | ancilla
    gates_preparation | qreg
    for i in range(T):
        oracle(f, qreg, ancilla)
        gates_preparation ^ qreg
        X | qreg
        gates_mct | circuit
        X | qreg
        gates_preparation | qreg
    # Apply H
    H | ancilla
    X | ancilla
    # Measure
    Measure | qreg
    Measure | ancilla
    Measure | empty
    circuit.exec()
    return int(qreg)


class GroverWithPriorKnowledge:
    """ grover search with prior knowledge

    https://arxiv.org/abs/2009.08721

    """
    @staticmethod
    def run(f, n, p, T, oracle):
        """ grover search for f with custom oracle

        Args:
            f(list<int>): the function to be decided
            n(int): the length of input
            p(list<float>): the distribute of priop probability
            T(int): the query times
            oracle(function): the oracle
        Returns:
            int: the a satisfies that f(a) = 1
        """
        return run_search_with_prior_knowledge(f, n, p, T, oracle)
