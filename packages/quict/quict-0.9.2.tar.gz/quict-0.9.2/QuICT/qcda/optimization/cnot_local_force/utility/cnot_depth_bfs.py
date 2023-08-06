#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/2/16 4:25 下午
# @Author  : Han Yu
# @File    : cnot_force_depth.py

import os

import numpy as np

from QuICT.qcda.optimization.cnot_local_force.utility.utility import apply_cx, count, generate_layer


def generate_json(n):
    """ find the best circuit by bfs

    Args:
        n(int): input qubits

    Returns:
        Circuit: optimal circuit

    """
    now = 0
    for i in range(n):
        now ^= (1 << (i * n + i))
    vis = np.zeros(1 << (n * n), dtype=int)
    vis[now] = 1
    pre = [None] * (1 << (n * n))
    out = {}
    queue = [now]
    out[now] = []
    ans = count(n)
    l = 0
    total = 1
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
                queue.append(new_state)
                paths = []
                total += 1
                while new_state != queue[0]:
                    paths.extend(layers[pre[new_state][1]])
                    new_state = pre[new_state][0]
                out[queue[-1]] = []
                for index in range(len(paths) - 1, -1, -1):
                    out[queue[-1]].append((paths[index]))

        if total == ans:
            break
        l += 1

    keys = out.keys()
    with open(f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{n}qubit_cnot_depth.inf", 'w') as file:
        file.write(";")
        for key in keys:
            string = f"{key}:"
            tuples = out[key]
            len_tuples = len(tuples)
            for i in range(len_tuples):
                _tuple = tuples[i]
                string += f"{_tuple[0] * 5 + _tuple[1]}"
                if i + 1 < len_tuples:
                    string += ','
                else:
                    string += ';'
            if len_tuples == 0:
                string += ';'
            file.write(string)
