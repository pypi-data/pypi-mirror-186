#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/3/20 4:53 下午
# @Author  : Han Yu
# @File    : gate_transform.py

import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.qcda.synthesis.gate_transform.special_set import *
from QuICT.qcda.utility import OutputAligner


class GateTransform(object):
    def __init__(self, instruction_set=USTCSet):
        """
        Args:
            instruction_set(InstructionSet): the goal instruction set
        """
        self.instruction_set = instruction_set

    @OutputAligner()
    def execute(self, circuit):
        """ equivalently transfrom circuit into goal instruction set

        The algorithm will try two possible path, and return a better result:
        1. make continuous local two-qubit gates into SU(4), then decomposition with goal instruction set
        2. transform the two-qubit gate into instruction set one by one, then one-qubit gate

        Args:
            circuit(Circuit/CompositeGate): the circuit to be transformed

        Returns:
            CompositeGate: the equivalent compositeGate with goal instruction set
        """
        gates = CompositeGate()
        if isinstance(circuit, CompositeGate):
            gates.extend(circuit)
        elif isinstance(circuit, Circuit):
            gates.extend(circuit.gates)
        else:
            raise TypeError("Invalid input for GateTransform")

        gates.gate_decomposition()
        gates = self.two_qubit_transform(gates)
        gates = self.one_qubit_transform(gates)
        return gates

    def one_qubit_transform(self, gates):
        gates_tran = CompositeGate()
        unitaries = [np.identity(2, dtype=np.complex128) for _ in range(gates.width())]
        for gate in gates:
            if gate.targets + gate.controls == 2:
                targs = gate.cargs + gate.targs
                for targ in targs:
                    gates_transformed = self.instruction_set.one_qubit_rule(Unitary(unitaries[targ]) & targ)
                    if gates_transformed.width() == 0:
                        local_matrix = np.eye(2)
                    else:
                        local_matrix = gates_transformed.matrix(local=True)
                    phase = np.angle(np.dot(unitaries[targ], np.linalg.inv(local_matrix))[0][0])
                    if (
                        not np.isclose(np.mod(phase, 2 * np.pi), 0) and
                        not np.isclose(np.mod(phase, 2 * np.pi), 2 * np.pi)
                    ):
                        gates_transformed.append(GPhase(phase) & targ)
                    gates_tran.extend(gates_transformed)
                    unitaries[targ] = np.identity(2, dtype=np.complex128)
                gates_tran.append(gate)
            else:
                unitaries[gate.targ] = np.dot(gate.matrix, unitaries[gate.targ])
        for i in range(gates.width()):
            gates_transformed = self.instruction_set.one_qubit_rule(Unitary(unitaries[i]) & i)
            if gates_transformed.width() == 0:
                local_matrix = np.eye(2)
            else:
                local_matrix = gates_transformed.matrix(local=True)
            phase = np.angle(np.dot(unitaries[i], np.linalg.inv(local_matrix))[0][0])
            if (
                not np.isclose(np.mod(phase, 2 * np.pi), 0) and
                not np.isclose(np.mod(phase, 2 * np.pi), 2 * np.pi)
            ):
                gates_transformed.append(GPhase(phase) & i)
            gates_tran.extend(gates_transformed)
        return gates_tran

    def two_qubit_transform(self, gates):
        gates_tran = CompositeGate()
        for gate in gates:
            if gate.targets + gate.controls > 2:
                raise Exception("gate_transform only support 2-qubit and 1-qubit gate now.")
            if gate.type != self.instruction_set.two_qubit_gate and gate.targets + gate.controls == 2:
                rule = self.instruction_set.select_transform_rule(gate.type)
                gates_tran.extend(rule(gate))
            else:
                gates_tran.append(gate)
        return gates_tran
