#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/11/12 上午10:10
# @Author  : Kaiqi Li
# @File    : proxy_unit_test.py\

import os
import unittest
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np

import cupy as cp
from cupy import cuda
from cupy.cuda import nccl

from QuICT.utility import Proxy


def sender(ndev, uid, dev_id):
    proxy = Proxy(ndev, uid, dev_id)
    based_data = np.random.rand(10).astype(np.complex64)
    gpu_data = cp.array(based_data)

    proxy.send(gpu_data, 1)

    return based_data


def receiver(ndev, uid, dev_id):
    proxy = Proxy(ndev, uid, dev_id)
    gpu_receive_buff = cp.zeros(10, dtype=np.complex64)

    proxy.recv(gpu_receive_buff, 0)

    return gpu_receive_buff.get()


def broadcast(ndev, uid, dev_id):
    proxy = Proxy(ndevs=ndev, uid=uid, dev_id=dev_id)
    if dev_id == 0:
        based_data = np.random.rand(10).astype(np.complex64)
        gpu_bd = cp.array(based_data)
    else:
        gpu_bd = cp.zeros(10, dtype=cp.complex64)

    proxy.broadcast(gpu_bd, 0)

    return gpu_bd.get()


@unittest.skipUnless(os.environ.get("test_with_gpu", False), "require GPU")
class TestProxy(unittest.TestCase):
    def test_send(self):
        ndev = 2
        uid = nccl.get_unique_id()
        with ProcessPoolExecutor(max_workers=2) as executor:
            st = executor.submit(sender, ndev, uid, 0)
            rt = executor.submit(receiver, ndev, uid, 1)

            tasks = [st, rt]

        results = []
        for t in as_completed(tasks):
            results.append(t.result())

        assert np.allclose(results[0], results[1])

    def test_broadcast(self):
        ndev = 3
        uid = nccl.get_unique_id()
        with ProcessPoolExecutor(max_workers=ndev) as executor:
            tasks = [executor.submit(broadcast, ndev, uid, dev_id) for dev_id in range(ndev)]

        results = []
        for t in as_completed(tasks):
            results.append(t.result())

        assert np.allclose(results[0], results[1])
        assert np.allclose(results[0], results[2])


if __name__ == "__main__":
    unittest.main()
