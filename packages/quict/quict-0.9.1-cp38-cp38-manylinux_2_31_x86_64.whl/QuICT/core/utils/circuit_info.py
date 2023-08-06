#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/15 10:31
# @Author  : Han Yu, Li Kaiqi
# @File    : _circuit_computing.py
from collections import Iterable
from typing import List
import numpy as np
from enum import Enum

from .gate_type import GateType
from .circuit_matrix import CircuitMatrix, get_gates_order_by_depth


class CircuitBased(object):
    """ Based Class for Circuit and Composite Gate. """
    @property
    def name(self) -> int:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def gates(self) -> list:
        return self._gates

    @gates.setter
    def gates(self, gates):
        self._gates = gates

    def __init__(self, name: str):
        self._name = name
        self._gates = []
        self._gate_type = {}        # gate_type: # of gates
        self._pointer = None
        self._precision = np.complex128

    def size(self) -> int:
        """ the number of gates in the circuit/CompositeGate

        Returns:
            int: the number of gates in circuit
        """
        return len(self._gates)

    def width(self):
        """ the number of qubits in circuit

        Returns:
            int: the number of qubits in circuit
        """
        return len(self.qubits)

    def depth(self) -> int:
        """ the depth of the circuit/CompositeGate.

        Returns:
            int: the depth
        """
        depth = np.zeros(self.width(), dtype=int)
        for gate in self._gates:
            targs = gate.cargs + gate.targs
            depth[targs] = np.max(depth[targs]) + 1

        return np.max(depth)

    def count_2qubit_gate(self) -> int:
        """ the number of the two qubit gates in the circuit/CompositeGate

        Returns:
            int: the number of the two qubit gates
        """
        count = 0
        for gate in self._gates:
            if gate.controls + gate.targets == 2:
                count += 1

        return count

    def count_1qubit_gate(self) -> int:
        """ the number of the one qubit gates in the circuit/CompositeGate

        Returns:
            int: the number of the one qubit gates
        """
        count = 0
        for gate in self._gates:
            if gate.is_single():
                count += 1

        return count

    def count_gate_by_gatetype(self, gate_type: GateType) -> int:
        """ the number of the gates which are some type in the circuit/CompositeGate

        Args:
            gateType(GateType): the type of gates to be count

        Returns:
            int: the number of the gates which are some type
        """
        if gate_type in self._gate_type.keys():
            return self._gate_type[gate_type]

        return 0

    def __str__(self):
        circuit_info = {
            "name": self.name,
            "width": self.width(),
            "size": self.size(),
            "depth": self.depth(),
            "1-qubit gates": self.count_1qubit_gate(),
            "2-qubit gates": self.count_2qubit_gate()
        }

        return str(circuit_info)

    def qasm(self, output_file: str = None):
        """ The qasm of current CompositeGate/Circuit.

        Args:
            output_file (str): The output qasm file's name or path

        Returns:
            str: The string of Circuit/CompositeGate's qasm.
        """
        qreg = self.width()
        creg = min(self.count_gate_by_gatetype(GateType.measure), qreg)
        if creg == 0:
            creg = qreg

        qasm_string = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n'
        qasm_string += f"qreg q[{qreg}];\n"
        qasm_string += f"creg c[{creg}];\n"

        cbits = 0
        for gate in self._gates:
            if gate.qasm_name == "measure":
                qasm_string += f"measure q[{gate.targ}] -> c[{cbits}];\n"
                cbits += 1
                cbits = cbits % creg
            else:
                qasm_string += gate.qasm()

        if output_file is not None:
            with open(output_file, 'w+') as of:
                of.write(qasm_string)

        return qasm_string

    def get_lastcall_for_each_qubits(self) -> List[GateType]:
        lastcall_per_qubits = [None] * self.width()
        inside_qargs = []
        for i in range(self.size() - 1, -1, -1):
            gate_args = self._gates[i].cargs + self._gates[i].targs
            gate_type = self._gates[i].type
            for garg in gate_args:
                if lastcall_per_qubits[garg] is None:
                    lastcall_per_qubits[garg] = gate_type
                    inside_qargs.append(garg)

            if len(inside_qargs) == self.width():
                break

        return lastcall_per_qubits

    def get_gates_order_by_depth(self) -> List[List]:
        """ Order the gates of circuit by its depth layer

        Returns:
            List[List[BasicGate]]: The list of gates which at same layers in circuit.
        """
        return get_gates_order_by_depth(self.gates)

    def matrix(self, device: str = "CPU", mini_arg: int = 0) -> np.ndarray:
        """ Generate the circuit's unitary matrix which compose by all quantum gates' matrix in current circuit.

        Args:
            device (str, optional): The device type for generate circuit's matrix, one of [CPU, GPU]. Defaults to "CPU".
            mini_arg (int, optional): The minimal qubit args, only use for CompositeGate local mode. Default to 0.
        """
        assert device in ["CPU", "GPU"]
        circuit_matrix = CircuitMatrix(device)

        if self.size() == 0:
            if device == "CPU":
                circuit_matrix = np.identity(1 << self.width(), dtype=self._precision)
            else:
                import cupy as cp

                circuit_matrix = cp.identity(1 << self.width(), dtype=self._precision)

            return circuit_matrix

        if self.size() > self.count_1qubit_gate() + self.count_2qubit_gate():
            self.gate_decomposition()

        return circuit_matrix.get_unitary_matrix(self.gates, self.width(), mini_arg)

    def convert_precision(self):
        """ Convert all gates in Cicuit/CompositeGate into single precision. """
        for gate in self.gates:
            if hasattr(gate, "convert_precision"):
                gate.convert_precision()

        self._precision = np.complex64 if self._precision == np.complex128 else np.complex128

    def gate_decomposition(self):
        added_idxes = 0     # The number of gates which add from gate.build_gate()
        for i in range(self.size()):
            gate = self.gates[i + added_idxes]
            if hasattr(gate, "build_gate"):
                decomp_gates = gate.build_gate()
                self.gates.remove(gate)
                for g in decomp_gates:
                    self._gates.insert(i + added_idxes, g)
                    added_idxes += 1

                added_idxes -= 1    # minus the original gate


class CircuitMode(Enum):
    Clifford = "Clifford"
    CliffordRz = "CliffordRz"
    Arithmetic = 'Arithmetic'
    Misc = "Misc"
