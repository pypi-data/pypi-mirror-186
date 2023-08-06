#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/6/9 下午5:35
# @Author  : Kaiqi Li
# @File    : gate_based

import numpy as np
try:
    import cupy as cp
except ImportError:
    cupy = None

from QuICT.core.operator import Operator
from QuICT.core.utils import GateType


class GateMatrixs:
    """
    The class of storing the gates' compute matrix, without duplicate.

    Args:
        precision(Union[np.complex64, np.complex128]): The precision of the gates.
        gpu_device_id(int): The GPU device ID.
    """
    def __init__(self, precision, gpu_device_id: int = 0):
        self.gate_matrixs = {}
        self.precision = precision
        self.device_id = gpu_device_id
        self.matrix_idx = []
        self.matrix_len = 0
        self._unitary_idx = 0

    @property
    def matrix(self):
        """ Return the matrix with all gates' compute matrix. """
        return self.final_matrix

    def _get_gate_name(self, gate):
        if gate.type == GateType.unitary:
            gate_name = gate.name
        else:
            gate_name = str(gate.type)

        for parg in gate.pargs:
            gate_name += f"_{parg}"

        return gate_name

    def build(self, gates):
        for gate in gates:
            if isinstance(gate, Operator):
                continue

            if gate.type in [GateType.measure, GateType.reset, GateType.barrier]:
                continue

            if gate.type == GateType.unitary:
                gate.name = gate.name + f"_{self._unitary_idx}"
                self._unitary_idx += 1

            gate_name = self._get_gate_name(gate)
            if gate_name not in self.gate_matrixs.keys():
                matrix = gate.matrix
                self._build_matrix_gate(gate_name, matrix)

        self._concentrate_gate_matrixs()

    def _build_matrix_gate(self, gate_name, matrix):
        """ Add gate. """
        self.gate_matrixs[gate_name] = (self.matrix_len, matrix.size)
        self.matrix_len += matrix.size
        if matrix.dtype != self.precision:
            matrix = matrix.astype(self.precision)
        self.matrix_idx.append(matrix)

    def _concentrate_gate_matrixs(self):
        """ Combined all gates' computer matrix in one large matrix."""
        self.final_matrix = np.empty(self.matrix_len, dtype=self.precision)
        start = 0

        for matrix in self.matrix_idx:
            self.final_matrix[start:start + matrix.size] = matrix.ravel()[:]
            start += matrix.size

        with cp.cuda.Device(self.device_id):
            self.final_matrix = cp.array(self.final_matrix)

    def get_target_matrix(self, gate):
        """
        Find the compute matrix of the given gate.

        Args:
            gate(Gate): the gate in circuit.
        """
        if gate.type in [GateType.measure, GateType.reset, GateType.barrier]:
            raise KeyError(f"Wrong gate here. {gate.name}")

        gate_name = self._get_gate_name(gate)
        start, itvl = self.gate_matrixs[gate_name]

        return self.final_matrix[start:start + itvl]
