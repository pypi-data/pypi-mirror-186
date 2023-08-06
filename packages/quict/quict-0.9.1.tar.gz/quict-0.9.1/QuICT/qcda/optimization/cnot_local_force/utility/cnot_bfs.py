#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/1/11 12:26 下午
# @Author  : Han Yu
# @File    : cnot_bfs.py

import os

import numpy as np

from QuICT.qcda.optimization.cnot_local_force.utility.utility import apply_cx, count, path


def generate_json(n):
    """ find the best circuit by bfs

    Args:
        n(int): input qubits
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
    l = 0
    ans = count(n)
    total = 1
    while True:
        now = queue[l]
        for i in range(n):
            for j in range(n):
                if i != j:
                    new_state = apply_cx(now, i, j, n)
                    if vis[new_state] == 0:
                        pre[new_state] = path(now, i, j)
                        vis[new_state] = vis[now] + 1
                        queue.append(new_state)
                        paths = []
                        total += 1
                        while new_state != queue[0]:
                            paths.append(pre[new_state].CX_tuple)
                            new_state = pre[new_state].father_node
                        out[queue[-1]] = []
                        for index in range(len(paths) - 1, -1, -1):
                            out[queue[-1]].append((paths[index]))
        if total == ans:
            break
        l += 1
    # json_data = json.dumps(out)
    # with open("./bfs/" + str(n) + 'qubit_cnot.json', 'w+') as file:
    #    file.write(json_data)
    keys = out.keys()
    with open(f"{os.path.dirname(os.path.abspath(__file__))}{os.path.sep}{n}qubit_cnot.inf", 'w') as file:
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
