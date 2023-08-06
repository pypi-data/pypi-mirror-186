#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/1/1 8:11 下午
# @Author  : Han Yu
# @File    : cnot_local_force.py

from itertools import combinations

from .cnot_force_depth import CnotForceDepthBfs
from .cnot_store_force_depth import CnotStoreForceDepthBfs
from QuICT.core import Circuit
from QuICT.core.gate import CX, GateType
from QuICT.qcda.utility import OutputAligner


class CnotLocalForceDepthBfs(object):
    """
    use bfs to optimize the cnot circuit
    """
    def __init__(self, store=False):
        """
        Args:
            store(bool): whether work with local data
        """
        self.store = store

    @OutputAligner()
    def execute(self, circuit: Circuit):
        """ optimize the circuit locally
        Args:
            circuit(Circuit): the circuit to be optimize

        Returns:
            Circuit: output circuit
        """
        gates = circuit.gates
        width = circuit.width()
        last_length = len(gates)
        while True:
            gates = self.traverse(gates, width, self.store)
            new_length = len(gates)
            if last_length == new_length:
                break
            last_length = new_length
        circuit_opt = Circuit(width)
        circuit_opt.extend(gates)
        return circuit_opt

    def traverse(self, input: list, width, store):
        """ find the best circuit by bfs

        Args:
            input(list<BasicGate>): input circuit
            width(int): circuit_width
            store(bool): whether work with local data

        Returns:
            list<BasicGate>: gates after optimization

        """
        all_list = [i for i in range(width)]
        max_local_qubits = 5 if store else 4
        for comb in combinations(all_list, min(width, max_local_qubits)):
            input = self.traverse_with_fix_qubits(input, set(comb), store)
        return input

    def traverse_with_fix_qubits(self, gates: list, fix: set, store):
        """ local optimize for fix qubits

        Args:
            gates(list<CXGate>): the gates to be optimized
            fix(set<int>): the fix qubits
            store(bool): whether work with local data

        Returns:
            list<CXGate>: results after optimization
        """
        mapping = {}
        back_map = {}
        mapping_id = 0
        for element in fix:
            mapping[element] = mapping_id
            back_map[mapping_id] = element
            mapping_id += 1
        output = []
        local_list = []
        for gate in gates:
            if gate.type == GateType.cx:
                fix_in = int(gate.carg in fix) + int(gate.targ in fix)
                if fix_in == 2:
                    local_list.append(gate)
                    continue
                elif fix_in == 0:
                    output.append(gate)
                    continue
            else:
                commu = True
                for s in local_list:
                    if not s.commutative(gate):
                        commu = False
                        break
                if commu:
                    output.append(gate)
                    continue
            if len(local_list) != 0:
                circuit = Circuit(len(fix))
                for local_gate in local_list:
                    CX | circuit([mapping[local_gate.carg], mapping[local_gate.targ]])
                new_circuit = (CnotStoreForceDepthBfs() if store else CnotForceDepthBfs()).execute(circuit)
                for local_gate in new_circuit.gates:
                    new_gate = CX.copy()
                    new_gate.cargs = [back_map[local_gate.carg]]
                    new_gate.targs = [back_map[local_gate.targ]]
                    output.append(new_gate)
                local_list = []
            output.append(gate)

        if len(local_list) != 0:
            circuit = Circuit(len(fix))
            for local_gate in local_list:
                CX | circuit([mapping[local_gate.carg], mapping[local_gate.targ]])
            new_circuit = (CnotStoreForceDepthBfs() if store else CnotForceDepthBfs()).execute(circuit)
            for local_gate in new_circuit.gates:
                new_gate = CX.copy()
                new_gate.cargs = [back_map[local_gate.carg]]
                new_gate.targs = [back_map[local_gate.targ]]
                output.append(new_gate)

        return output
