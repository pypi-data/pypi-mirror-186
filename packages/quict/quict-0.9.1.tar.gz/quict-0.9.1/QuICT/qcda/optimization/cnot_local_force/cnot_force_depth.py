#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/2/16 4:25 下午
# @Author  : Han Yu
# @File    : cnot_force_depth.py

import numpy as np

from QuICT.core import *
from QuICT.core.gate import CX, GateType
from QuICT.qcda.utility import OutputAligner
from QuICT.qcda.optimization.cnot_local_force.utility.utility import apply_cx, generate_layer


class CnotForceDepthBfs(object):
    """
    use bfs to optimize the cnot circuit
    """
    @OutputAligner()
    def execute(self, circuit: Circuit):
        """ find the best circuit by bfs

        Args:
            input(Circuit): input circuit

        Returns:
            Circuit: optimal circuit

        """
        n = circuit.width()
        circuit_opt = Circuit(n)
        input_matrix = np.identity(n, dtype=bool)
        now = 0
        goal = 0
        for gate in circuit.gates:
            if gate.type != GateType.cx:
                raise Exception("the circuit should only contain CX gate")
            input_matrix[gate.targ, :] = input_matrix[gate.targ, :] ^ input_matrix[gate.carg, :]
        for i in range(n):
            for j in range(n):
                if input_matrix[i, j]:
                    goal ^= 1 << (i * n + j)
        for i in range(n):
            now ^= (1 << (i * n + i))
        vis = np.zeros(1 << (n * n), dtype=int)
        vis[now] = 1
        pre = [None] * (1 << (n * n))
        queue = [now]
        l = 0
        if now == goal:
            return circuit_opt

        layers = generate_layer(n)

        while True:
            now = queue[l]
            for i in range(len(layers)):
                layer = layers[i]
                for cx in layer:
                    new_state = apply_cx(now, cx[0], cx[1], n)
                if vis[new_state] == 0:
                    pre[new_state] = (now, i)
                    vis[new_state] = vis[now] + 1
                    if new_state == goal:
                        paths = []
                        while new_state != queue[0]:
                            paths.extend(layers[pre[new_state][1]])
                            new_state = pre[new_state][0]
                        for index in range(len(paths) - 1, -1, -1):
                            CX | circuit_opt(list(paths[index]))

                        return circuit_opt
                    queue.append(new_state)
            l += 1
