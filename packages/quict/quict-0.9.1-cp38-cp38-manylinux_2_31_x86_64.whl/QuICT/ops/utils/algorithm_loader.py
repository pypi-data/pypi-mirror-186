#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/6/30 下午5:47
# @Author  : Kaiqi Li
# @File    : algorithm loader

import importlib


DEVICE_LIST = ["CPU", "GPU"]
BASED_LINALG = [
    "dot", "tensor", "MatrixTensorI", "MatrixPermutation", "VectorPermutation",
    "matrix_dot_vector", "simple_vp", "qubit_vp"
]


class LinAlgLoader:
    """
    The Algorithm class with used to load all required algorithm, including based linear algorithm, gate-based matrix
    dot vector algorithm, and algorithms for multi-GPUs.

    Args:
        device(str): one of ["GPU", "CPU"].
        enable_gate_kernel(bool): loading gate-based matrix dot vector algorithm if True.
        enable_multigpu_gate_kernel(bool): loading the required algorithms of multi-GPUs if True.
    """
    def __init__(self, device: str, enable_gate_kernel: bool = False, enable_multigpu_gate_kernel: bool = False):
        if device not in DEVICE_LIST:
            raise KeyError(f"Not supported the given device, please choice one of {DEVICE_LIST}")

        if device == "CPU":
            linalg_lib = importlib.import_module('QuICT.ops.linalg.cpu_calculator')
        else:
            linalg_lib = importlib.import_module('QuICT.ops.linalg.gpu_calculator')

        for attr, value in linalg_lib.__dict__.items():
            if attr in BASED_LINALG:
                self.__dict__[attr] = value

        if enable_gate_kernel:
            gate_lib = importlib.import_module('QuICT.ops.gate_kernel.gate_function')
            GATE_KERNEL_FUNCTIONS = gate_lib.__dict__["__outward_functions"]

            for attr, value in gate_lib.__dict__.items():
                if attr in GATE_KERNEL_FUNCTIONS:
                    self.__dict__[attr] = value

        if enable_multigpu_gate_kernel:
            proxy_lib = importlib.import_module('QuICT.ops.gate_kernel.multigpu_gate_func')
            PROXY_GATE_FUNCTIONS = proxy_lib.__dict__["__outward_functions"]

            for attr, value in proxy_lib.__dict__.items():
                if attr in PROXY_GATE_FUNCTIONS:
                    self.__dict__[attr] = value
