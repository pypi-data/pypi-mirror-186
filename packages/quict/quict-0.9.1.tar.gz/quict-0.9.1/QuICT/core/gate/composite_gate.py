#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/14 9:36 下午
# @Author  : Han Yu, Li Kaiqi
# @File    : composite_gate.py
from typing import Union
import numpy as np

from QuICT.core.qubit import Qureg, Qubit
from QuICT.core.gate import BasicGate
from QuICT.core.utils import (
    CircuitBased,
    CGATE_LIST,
    unique_id_generator
)
from QuICT.tools.exception.core import ValueError, CompositeGateAppendError, TypeError, GateQubitAssignedError


class CompositeGate(CircuitBased):
    """ Implement a group of gate

    Attributes:
        name (str): the name of the composite gate
        gates (list<BasicGate>): gates within this composite gate
    """
    @property
    def checkpoint(self):
        return self._check_point

    def __init__(self, name: str = None, gates: list = None):
        if name is None:
            name = "composite_gate_" + unique_id_generator()

        super().__init__(name)
        self._check_point = None        # required checkpoint
        self._min_qubit = np.inf
        self._max_qubit = 0

        if gates is not None:
            self.extend(gates)

    ####################################################################
    ############          CompositeGate Context             ############
    ####################################################################
    def __enter__(self):
        global CGATE_LIST
        CGATE_LIST.append(self)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print(f"{exc_type}: {exc_value}")
        if exc_type is not None:
            raise Exception(exc_value)

        global CGATE_LIST
        CGATE_LIST.remove(self)

        return True

    ####################################################################
    ############        CompositeGate Qureg Mapping         ############
    ####################################################################
    def width(self):
        """ the number of qubits applied by gates

        Returns:
            int: the number of qubits applied by gates
        """
        return self._max_qubit

    def __call__(self, indexes: Union[list, int]):
        if isinstance(indexes, int):
            indexes = [indexes]

        self._update_qubit_limit(indexes)
        self._pointer = indexes
        return self

    def clean(self):
        self._gates = []
        self._min_qubit, self._max_qubit = np.inf, 0
        self._pointer = None

    def __and__(self, targets: Union[int, list, Qubit, Qureg]):
        """ assign qubits or indexes for given gates

        Args:
            targets ([int/qubit/list[int]/qureg]): qubit describe
        """
        if isinstance(targets, int):
            targets = [targets]

        if isinstance(targets, Qubit):
            targets = Qureg(targets)

        if len(targets) != self._max_qubit:
            raise ValueError("CompositeGate.&:len(targets)", f"less than {self._max_qubit}", len(targets))

        self._mapping(targets)
        if CGATE_LIST:
            CGATE_LIST[-1].extend(self.gates)

    def _mapping(self, targets: Qureg):
        """ remapping the gates' affectArgs

        Args:
            targets(Qureg/List): the related qubits
        """
        for gate in self._gates:
            args_index = gate.cargs + gate.targs
            if isinstance(targets, Qureg):
                target_qureg = targets(args_index)
                gate.assigned_qubits = target_qureg
                gate.update_name(target_qureg[0].id)
            else:
                gate.cargs = [targets[carg] for carg in gate.cargs]
                gate.targs = [targets[targ] for targ in gate.targs]

    def _update_qubit_limit(self, indexes: list):
        for idx in indexes:
            assert idx >= 0 and isinstance(idx, int)
            if idx >= self._max_qubit:
                self._max_qubit = idx + 1

            if idx < self._min_qubit:
                self._min_qubit = idx

    ####################################################################
    ############            CompositeGate Build             ############
    ####################################################################
    def __or__(self, targets):
        """ deal the operator '|'

        Use the syntax "gateSet | circuit", "gateSet | gateSet"
        to add the gate of gateSet into the circuit

        Note that the order of qubits is that control bits first
        and target bits followed.

        Args:
            targets: the targets the gate acts on, it can have following form,
                1) Circuit
                2) CompositeGate
        Raise:
            TypeError: the type of other is wrong
        """
        try:
            targets.extend(self)
        except Exception as e:
            raise CompositeGateAppendError(f"Failure to append current CompositeGate, due to {e}.")

    def __xor__(self, targets):
        """deal the operator '^'

        Use the syntax "gateSet ^ circuit", "gateSet ^ gateSet"
        to add the gate of gateSet's inverse into the circuit

        Note that the order of qubits is that control bits first
        and target bits followed.

        Args:
            targets: the targets the gate acts on, it can have following form,
                1) Circuit
        Raise:
            TypeError: the type of other is wrong
        """
        try:
            targets.extend(self.inverse().gates)
        except Exception as e:
            raise CompositeGateAppendError(f"Failure to append the inverse of current CompositeGate, due to {e}.")

    def __getitem__(self, item):
        """ get gates from this composite gate

        Args:
            item(int/slice): slice passed in.

        Return:
            [BasicGates]: the gates
        """
        return self._gates[item]

    def extend(self, gates: list):
        for gate in gates:
            self.append(gate, is_extend=True)

        self._pointer = None

    def append(self, gate, is_extend: bool = False, insert_idx: int = -1):
        from QuICT.core.operator import CheckPointChild, Operator

        if isinstance(gate, BasicGate):
            self._append_gate(gate, insert_idx)
            if not is_extend:
                self._pointer = None

            # Update gate type dict
            if gate.type in self._gate_type.keys():
                self._gate_type[gate.type] += 1
            else:
                self._gate_type[gate.type] = 1
        elif isinstance(gate, CheckPointChild):
            self._check_point = gate
        else:
            assert isinstance(gate, Operator), TypeError("CompositeGate.append", "BasicGate/Operator", type(gate))
            if insert_idx == -1:
                self._gates.append(gate)
            else:
                self._gates.insert(insert_idx, gate)

    def left_extend(self, gates: list):
        for idx, gate in enumerate(gates):
            self.append(gate, is_extend=True, insert_idx=idx)

        self._pointer = None

    def _append_gate(self, gate, insert_idx: int = -1):
        gate = gate.copy()

        if self._pointer is not None:
            qubit_index = self._pointer[:]
            gate_args = gate.controls + gate.targets
            if len(self._pointer) > gate_args:
                gate.cargs = [qubit_index[carg] for carg in gate.cargs]
                gate.targs = [qubit_index[targ] for targ in gate.targs]
            elif len(self._pointer) == gate_args:
                gate.cargs = qubit_index[:gate.controls]
                gate.targs = qubit_index[gate.controls:]
            else:
                raise GateQubitAssignedError(f"{gate.type} need {gate_args} indexes, but given {len(self._pointer)}")
        else:
            qubit_index = gate.cargs + gate.targs
            if not qubit_index:
                raise GateQubitAssignedError(f"{gate.type} need qubit indexes to add into Composite Gate.")

            self._update_qubit_limit(qubit_index)

        if insert_idx == -1:
            self._gates.append(gate)
        else:
            self._gates.insert(insert_idx, gate)

    ####################################################################
    ############            CompositeGate Utils             ############
    ####################################################################
    def inverse(self):
        """ the inverse of CompositeGate

        Returns:
            CompositeGate: the inverse of the gateSet
        """
        inverse_cgate = CompositeGate()
        inverse_gates = [gate.inverse() for gate in self._gates[::-1]]
        inverse_cgate.extend(inverse_gates)

        return inverse_cgate

    def matrix(self, device: str = "CPU", local: bool = False) -> np.ndarray:
        """ matrix of these gates

        Args:
            device (str, optional): The device type for generate circuit's matrix, one of [CPU, GPU]. Defaults to "CPU".
            local: whether regards the min_qubit as the 0's qubit

        Returns:
            np.ndarray: the matrix of the gates
        """
        if local and isinstance(self._min_qubit, int):
            min_value = self._min_qubit
        else:
            min_value = 0

        return super().matrix(device, min_value)
