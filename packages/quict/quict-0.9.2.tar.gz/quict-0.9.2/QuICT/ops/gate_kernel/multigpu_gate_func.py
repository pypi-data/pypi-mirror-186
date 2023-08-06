import cupy as cp
import numpy as np

from .gate_function import prop_add_double_kernel, prop_add_single_kernel, MeasureGate_prop


__outward_functions = [
    "complex_multiply",
    "float_multiply"
]


complex_multiply_single = cp.RawKernel(r'''
    #include <cupy/complex.cuh>
    extern "C" __global__
    void SimpleMultiply(complex<float> val, complex<float>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;

        vec[label] = vec[label]*val;
    }
    ''', 'SimpleMultiply')
complex_multiply_single.compile()


complex_multiply_double = cp.RawKernel(r'''
    #include <cupy/complex.cuh>
    extern "C" __global__
    void SimpleMultiply(complex<double> val, complex<double>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;

        vec[label] = vec[label]*val;
    }
    ''', 'SimpleMultiply')
complex_multiply_double.compile()


float_multiply_single = cp.RawKernel(r'''
    #include <cupy/complex.cuh>
    extern "C" __global__
    void FloatMultiply(const float value, complex<float>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;

        vec[label] = vec[label] * value;
    }
    ''', 'FloatMultiply')
float_multiply_single.compile()


float_multiply_double = cp.RawKernel(r'''
    #include <cupy/complex.cuh>
    extern "C" __global__
    void FloatMultiply(const double value, complex<double>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;

        vec[label] = vec[label] * value;
    }
    ''', 'FloatMultiply')
float_multiply_double.compile()


def complex_multiply(val, vec, vec_bit, sync: bool = False):
    task_number = 1 << vec_bit
    thread_per_block = min(256, task_number)
    block_num = task_number // thread_per_block

    if vec.dtype == np.complex64:
        complex_multiply_single(
            (block_num,),
            (thread_per_block,),
            (val, vec)
        )
    else:
        complex_multiply_double(
            (block_num,),
            (thread_per_block,),
            (val, vec)
        )

    if sync:
        cp.cuda.Device().synchronize()


def float_multiply(val, vec, vec_bit, sync: bool = False):
    task_number = 1 << vec_bit
    thread_per_block = min(256, task_number)
    block_num = task_number // thread_per_block

    if vec.dtype == np.complex64:
        float_multiply_single(
            (block_num,),
            (thread_per_block,),
            (val, vec)
        )
    else:
        float_multiply_double(
            (block_num,),
            (thread_per_block,),
            (val, vec)
        )

    if sync:
        cp.cuda.Device().synchronize()
