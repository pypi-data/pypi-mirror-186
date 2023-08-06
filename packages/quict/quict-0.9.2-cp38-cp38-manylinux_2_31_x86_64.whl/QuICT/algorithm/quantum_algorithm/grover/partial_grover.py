#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/6/3 10:14 上午
# @Author  : Peng Sirui
# @File    : partial_grover.py

import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.core.gate.backend import MCTOneAux
from QuICT.tools import Logger
from QuICT.tools.exception.core import *

logger = Logger("Grover-partial")


def calculate_r1_r2_one_target(N, K):
    # see https://arxiv.org/abs/quant-ph/0504157
    r1 = np.sqrt(N) * np.pi * 0.25 - np.sqrt(N / K) * np.sqrt(3 / 4)
    r2 = np.sqrt(N / K) * np.pi * (1 / 6)
    r1 = round(r1)
    r2 = round(r2)
    return r1, r2


class PartialGrover:
    """ partial grover search with one target

    https://arxiv.org/abs/quant-ph/0407122
    """

    def __init__(self, simulator) -> None:
        self.simulator = simulator

    def circuit(self, n, n_block, n_ancilla, oracle, measure=True):
        """ partial grover search with one target

        Args:
            n(int):         bits length of global address
            n_block(int):   bits length of block address
            n_ancilla(int): length of oracle working space. assume clean
            oracle(CompositeGate): the oracle that flip phase of target state.
                [0:n] is index qreg,
                [n:n+k] is ancilla
                also assume that it works in style of QCQI p249 6.2
            measure(bool): measure included or not

        Returns:
            int: the target address, big endian
        """
        K = 1 << n_block
        N = 1 << n
        r1, r2 = calculate_r1_r2_one_target(N, K)

        circuit = Circuit(n + n_ancilla + 1)
        index_q = list(range(n))
        oracle_q = list(range(n, n + n_ancilla))
        ancillia_q = [n + n_ancilla]
        # step 1
        for idx in index_q:
            H | circuit(idx)
        for i in range(r1):
            # global inversion about target
            oracle | circuit(index_q + oracle_q)
            # global inversion about average
            for idx in index_q:
                H | circuit(idx)
            for idx in index_q:
                X | circuit(idx)
            H | circuit(index_q[n - 1])
            MCTOneAux().execute(n + 1) | circuit(index_q + oracle_q[:1])
            H | circuit(index_q[n - 1])
            for idx in index_q:
                X | circuit(idx)
            for idx in index_q:
                H | circuit(idx)
        # step 2
        for i in range(r2):
            # global inversion about target
            oracle | circuit(index_q + oracle_q)
            # local inversion about average
            local_n = n - n_block
            local_index_q = [j for j in range(n_block, n_block + local_n)]
            for idx in local_index_q:
                H | circuit(idx)
            for idx in local_index_q:
                X | circuit(idx)
            H | circuit(local_index_q[local_n - 1])
            MCTOneAux().execute(local_n + 1) | circuit(local_index_q + oracle_q[:1])
            H | circuit(local_index_q[local_n - 1])
            for idx in local_index_q:
                X | circuit(idx)
            for idx in local_index_q:
                H | circuit(idx)
        # step 3
        H | circuit(ancillia_q[0])
        X | circuit(ancillia_q[0])
        oracle | circuit(index_q + [ancillia_q[0]] + oracle_q[1:])
        X | circuit(ancillia_q[0])
        H | circuit(ancillia_q[0])
        # controlled inversion about average
        for idx in index_q:
            CH | circuit([ancillia_q[0], idx])
        for idx in index_q:
            CX | circuit([ancillia_q[0], idx])
        MCTOneAux().execute(n + 2) | circuit([ancillia_q[0]] + index_q + oracle_q[:1])
        for idx in index_q:
            CX | circuit([ancillia_q[0], idx])
        for idx in index_q:
            CH | circuit([ancillia_q[0], idx])
        # Measure
        for idx in index_q:
            if measure:
                Measure | circuit(idx)
        logger.info(
            f"circuit width           = {circuit.width():4}\n" +
            f"global Grover iteration = {r1:4}\n" +
            f"local  Grover iteration = {r2:4}\n" +
            f"oracle  calls           = {r1+r2+1:4}\n" +
            f"other circuit size      = {circuit.size() - oracle.size()*(r1+r2):4}\n"
        )
        return circuit

    def run(self, n, n_block, n_ancilla, oracle, measure=True):
        simulator = self.simulator
        index_q = list(range(n))
        circuit = self.circuit(n, n_block, n_ancilla, oracle, measure)
        simulator.run(circuit)
        return int(circuit[index_q])
