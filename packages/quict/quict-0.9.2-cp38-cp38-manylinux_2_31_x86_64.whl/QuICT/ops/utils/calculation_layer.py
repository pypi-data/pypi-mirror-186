#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/5/21 下午3:24
# @Author  : Kaiqi Li
# @File    : calculation_layer

import weakref
import cupy as cp
import numpy as np

import QuICT.ops.linalg.gpu_calculator as GPUCalculator


class CalculationLayer:
    """ The context class of GPU linear algorithm and GPU memory management.

    Args:
        gpu_device (int): Indicated GPU device.
        memory_limit (int): the limitation of memory pool. Unit is GiB

    Examples:
        with CalculationLayer(gpu_device=0, memory_limit=4) as CL:
            gpu_A = cp.array(cpu_A)
            gpu_B = cp.array(cpu_B)

            result = CL.dot(gpu_A, gpu_B, gpu_out=True)
    """

    def __init__(self, gpu_device: int = 0, memory_limit: int = None):
        if gpu_device != cp.cuda.runtime.getDevice() and gpu_device < cp.cuda.runtime.getDeviceCount():
            dev = cp.cuda.Device(gpu_device)
            cp.cuda.Device.use(dev)

        self.mempool = cp.get_default_memory_pool()
        self.pinned_mempool = cp.get_default_pinned_memory_pool()

        if memory_limit:
            self.mempool.set_limit(memory_limit * 1024 ** 3)

        # Set Memory allocator
        cp.cuda.set_allocator(self.mempool.malloc)

        # Memory Record
        self.mempool_used = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear_memory()

    @property
    def memory_pool(self):
        return self.mempool

    @property
    def pinned_memory_pool(self):
        return self.pinned_mempool

    def clear_memory(self):
        """ released unused memory in current memory pool. """
        self.mempool_used.clear()
        self.mempool.free_all_blocks()
        self.pinned_mempool.free_all_blocks()

    def htod(self, target):
        """ mv target from host into GPU device. """
        if type(target) is not cp.ndarray:
            cp_t = cp.array(target)
            weak_r = weakref.ref(cp_t)
            self.mempool_used.append(cp_t)

            return weak_r

        raise ("The given value has been added in the GPU.")

    def dtoh(self, target):
        """ mv target from GPU device into host. """
        if type(target) is cp.ndarray:
            return target.get()

        if type(target) is weakref.ref:
            return target().get()

        raise ("The given value not in GPU.")

    def _var_normalized(self, target):
        if type(target) is weakref.ref:
            return target()

        if type(target) is np.ndarray:
            wr_target = self.htod(target)
            return wr_target()

        return target

    def _result_normalized(self, result, gpu_out):
        if gpu_out:
            return result
        else:
            self.mempool_used.append(result)
            wr_result = weakref.ref(result)
            return wr_result

    def dot(self, A, B, gpu_out: bool = True, sync: bool = True):
        """ dot matrix A and matrix B

        Args:
            A(np.array<np.complex>): the matrix A
            B(np.array<np.complex>): the matrix B
            gpu_out(bool): return result from GPU into CPU

        Returns:
            np.array<np.complex>: A * B
        """
        gpu_A = self._var_normalized(A)
        gpu_B = self._var_normalized(B)

        result = GPUCalculator.dot(gpu_A, gpu_B, gpu_out, sync)

        return self._result_normalized(result, gpu_out)

    def tensor(self, A, B, gpu_out: bool = True, sync: bool = True):
        """ tensor A and B

        Args:
            A(np.array<np.complex>): the matrix A
            B(np.array<np.complex>): the matrix B
            gpu_out(bool): return result from GPU into CPU

        Returns:
            np.array<np.complex>: the tensor result A ⊗ B
        """
        gpu_A = self._var_normalized(A)
        gpu_B = self._var_normalized(B)

        result = GPUCalculator.tensor(gpu_A, gpu_B, gpu_out, sync)

        return self._result_normalized(result, gpu_out)

    def MatrixTensorI(self, A, n, m, gpu_out: bool = True, sync: bool = True):
        """ tensor I^n and A and I^m

        Args:
            A(np.array<np.complex>): the matrix A
            n(int): the index of indentity
            m(int): the index of indentity
            gpu_out(bool): return result from GPU into CPU

        Returns:
            np.array<np.complex>: the tensor result I^n ⊗ A ⊗ I^m
        """
        gpu_A = self._var_normalized(A)

        result = GPUCalculator.MatrixTensorI(gpu_A, n, m, gpu_out, sync)

        return self._result_normalized(result, gpu_out)

    def VectorPermutation(
            self,
            A,
            mapping,
            changeInput: bool = False,
            gpu_out: bool = True,
            sync: bool = True
    ):
        """ permutaion A with mapping, inplace

        Args:
            A(np.array<np.complex>): the matrix A.
            mapping(np.array<int>): the qubit mapping.
            changeInput(bool): whether changes in A.
            gpu_out(bool): return result from GPU.

        Returns:
            np.array<np.complex>: the result of Permutation
        """
        gpu_A = self._var_normalized(A)

        result = GPUCalculator.VectorPermutation(gpu_A, mapping, changeInput, gpu_out, sync)

        return self._result_normalized(result, gpu_out)

    def MatrixPermutation(
            self,
            A,
            mapping,
            changeInput: bool = False,
            gpu_out: bool = True,
            sync: bool = True
    ):
        """ permute mat with mapping, inplace

        Args:
            A(np.array<np.complex>): the matrix A.
            mapping(np.array<int>): the qubit mapping.
            changeInput(bool): whether changes in A.
            gpu_out(bool): return result from GPU.
        """
        gpu_A = self._var_normalized(A)

        result = GPUCalculator.MatrixPermutation(gpu_A, mapping, changeInput, gpu_out, sync)

        return self._result_normalized(result, gpu_out)
