# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Modification Notice: Code revised for QuICT

import time
from collections import Counter

from QuICT.core.circuit import Circuit
from QuICT.core.gate import *


class TemplateSearching:
    """ for clifford gates search for S, CNOT, H gates """

    def __init__(self, qubit_num, gate_num, gate_dep):
        self.qubit_num = qubit_num
        self.gate_num = gate_num
        self.dep = gate_dep
        self.template_list = []
        self.temp_qubit_dep = [0] * qubit_num
        self.target = []
        for i in range(qubit_num):
            self.target.append(i)

    def copy_circuit(self, temp_circuit):
        new_circuit = Circuit(temp_circuit.width())
        new_circuit.extend(temp_circuit.gates)
        return new_circuit

    def identity(self, temp_circuit):
        matrix = temp_circuit.matrix()
        n = np.size(matrix, 0)
        tot = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    tot += abs(matrix[i, j])
                else:
                    tot += abs(matrix[i, j] - 1)
        return abs(tot) < 1e-2

    def check_minimum(self, temp_circuit):
        n = temp_circuit.size()
        if self.identity(temp_circuit):
            for i in range(n):
                for j in range(1, n - i):
                    new_circuit = self.copy_circuit(temp_circuit.sub_circuit(i, j, self.target))
                    if self.identity(new_circuit):
                        return False
            return True
        return False

    def graph_isomorphism(self, inform_list_a, inform_list_b, status_list_a, status_list_b):

        # check if an ordered-list graph is not isomorphism with the other
        flag_all_mapping = True
        for vertex_a in range(self.qubit_num):
            if self.mapping[vertex_a] == -1:
                flag_all_mapping = False
                break

        if flag_all_mapping:
            flag_check_graph = True
            for i in range(self.qubit_num):
                j = self.mapping[i]
                if len(inform_list_a[i]) == len(inform_list_b[j]) and len(status_list_a[i]) == len(status_list_b[j]):
                    for k in range(len(inform_list_a[i])):
                        if not flag_check_graph:
                            break
                        if status_list_a[i][k] != status_list_b[j][k]:
                            flag_check_graph = False
                        else:
                            if status_list_a[i][k] == 'S':
                                flag_check_graph = flag_check_graph & (
                                    Counter(inform_list_a[i][k]) == Counter(inform_list_b[j][k])
                                )
                            else:
                                mapping_list_a = Counter(inform_list_a[i][k])
                                mapping_list_b = Counter(inform_list_b[j][k])
                                if len(mapping_list_a) == len(mapping_list_b):
                                    for p in mapping_list_a:
                                        q = self.mapping[p]
                                        flag_check_graph = flag_check_graph & (mapping_list_a[p] == mapping_list_b[q])
                                else:
                                    flag_check_graph = False
                                    break
                else:
                    flag_check_graph = False
                    break
            return flag_check_graph
        else:
            flag_check_graph = False
            for i in range(self.qubit_num):
                if not self.mapped[i]:
                    if (
                        len(inform_list_a[vertex_a]) == len(inform_list_b[i]) and
                        len(status_list_a[vertex_a]) == len(status_list_b[i])
                    ):
                        flag_check_list = True
                        self.mapped[i] = True
                        self.mapping[vertex_a] = i
                        for j in range(len(status_list_a[vertex_a])):
                            check_a = status_list_a[vertex_a][j]
                            check_b = status_list_b[i][j]
                            flag_check_list = flag_check_list & (check_a == check_b)
                        if flag_check_list:
                            flag_check_graph = flag_check_graph or self.graph_isomorphism(
                                inform_list_a, inform_list_b, status_list_a, status_list_b
                            )
                            if flag_check_graph:
                                break
                        if not flag_check_graph:
                            self.mapped[i] = False
                            self.mapping[vertex_a] = -1

            return flag_check_graph

    def commutative_processing(self, temp_circuit):
        for i in range(len(temp_circuit.gates) - 1):
            gate_a = temp_circuit.gates[i]
            gate_b = temp_circuit.gates[i + 1]
            if gate_a.commutative(gate_b):
                if gate_a.is_control_single() and not gate_b.is_control_single():
                    temp_circuit.gates[i] = gate_b
                    temp_circuit.gates[i + 1] = gate_a
                    temp_circuit = self.commutative_processing(temp_circuit)
        return temp_circuit

    def check_circuit_not_isomorphism(self, circuit_a, circuit_b):

        # check if a circuit is not isomorphism with the other
        # first only check cnot circuit

        # commutative processing
        circuit_a = self.commutative_processing(circuit_a)
        circuit_b = self.commutative_processing(circuit_b)

        inform_list_a = []
        status_list_a = []
        inform_list_b = []
        status_list_b = []
        for i in range(self.qubit_num):
            inform_list_a.append([])
            status_list_a.append([])
            inform_list_b.append([])
            status_list_b.append([])

        temp_inform_list = []
        for i in range(self.qubit_num):
            temp_inform_list.append([])
        for gate_a in circuit_a.gates:
            if gate_a.is_control_single():
                temp_gate_c = gate_a.carg
                temp_gate_t = gate_a.targ
                if status_list_a[temp_gate_c] == []:
                    status_list_a[temp_gate_c].append('C')
                    temp_inform_list[temp_gate_c].append(temp_gate_t)
                else:
                    if status_list_a[temp_gate_c][-1] == 'C':
                        temp_inform_list[temp_gate_c].append(temp_gate_t)
                    else:
                        inform_list_a[temp_gate_c].append(temp_inform_list[temp_gate_c])
                        status_list_a[temp_gate_c].append('C')
                        temp_inform_list[temp_gate_c] = [temp_gate_t]
            else:
                temp_gate = gate_a.targ
                if status_list_a[temp_gate] == []:
                    status_list_a[temp_gate].append('S')
                    if gate_a.type == GateType.h:
                        temp_inform_list[temp_gate].append(1)
                    else:
                        temp_inform_list[temp_gate].append(2)
                else:
                    if status_list_a[temp_gate][-1] == 'S':
                        if gate_a.type == GateType.h:
                            temp_inform_list[temp_gate].append(1)
                        else:
                            temp_inform_list[temp_gate].append(2)
                    else:
                        inform_list_a[temp_gate].append(temp_inform_list[temp_gate])
                        status_list_a[temp_gate].append('S')
                        if gate_a.type == GateType.h:
                            temp_inform_list[temp_gate] = [1]
                        else:
                            temp_inform_list[temp_gate] = [2]

        for i in range(self.qubit_num):
            if temp_inform_list[i] != []:
                inform_list_a[i].append(temp_inform_list[i])

        temp_inform_list = []
        for i in range(self.qubit_num):
            temp_inform_list.append([])
        for gate_b in circuit_b.gates:
            if gate_b.is_control_single():
                temp_gate_c = gate_b.carg
                temp_gate_t = gate_b.targ
                if status_list_b[temp_gate_c] == []:
                    status_list_b[temp_gate_c].append('C')
                    temp_inform_list[temp_gate_c].append(temp_gate_t)
                else:
                    if status_list_b[temp_gate_c][-1] == 'C':
                        temp_inform_list[temp_gate_c].append(temp_gate_t)
                    else:
                        inform_list_b[temp_gate_c].append(temp_inform_list[temp_gate_c])
                        status_list_b[temp_gate_c].append('C')
                        temp_inform_list[temp_gate_c] = [temp_gate_t]
            else:
                temp_gate = gate_b.targ
                if status_list_b[temp_gate] == []:
                    status_list_b[temp_gate].append('S')
                    if gate_b.type == GateType.h:
                        temp_inform_list[temp_gate].append(1)
                    else:
                        temp_inform_list[temp_gate].append(2)
                else:
                    if status_list_b[temp_gate][-1] == 'S':
                        if gate_b.type == GateType.h:
                            temp_inform_list[temp_gate].append(1)
                        else:
                            temp_inform_list[temp_gate].append(2)
                    else:
                        inform_list_b[temp_gate].append(temp_inform_list[temp_gate])
                        status_list_b[temp_gate].append('S')
                        if gate_b.type == GateType.h:
                            temp_inform_list[temp_gate] = [1]
                        else:
                            temp_inform_list[temp_gate] = [2]

        for i in range(self.qubit_num):
            if temp_inform_list[i] != []:
                inform_list_b[i].append(temp_inform_list[i])

        self.mapping = []
        self.mapped = []
        for i in range(self.qubit_num):
            self.mapping.append(-1)
            self.mapped.append(False)
        flag_carg_graph = self.graph_isomorphism(inform_list_a, inform_list_b, status_list_a, status_list_b)

        return not flag_carg_graph

#    def check_list_not_isomorphism(self, temp_circuit):

        # check if the circuit is not isomorphism with every template in the list

#        no_isomorphism = True
#        for template in self.template_list:
#            no_isomorphism = no_isomorphism & self.check_circuit_not_isomorphism(temp_circuit, template)
#        return no_isomorphism

    def search(self, temp_gate_num, temp_circuit):

        # check whether it is a template
        if 1 <= temp_gate_num <= self.gate_num:
            if self.identity(temp_circuit):
                # if self.check_list_not_isomorphism(temp_circuit):
                #     self.template_list.append(temp_circuit)
                self.template_list.append([temp_circuit, self.check_minimum(temp_circuit)])
                return
        if temp_gate_num == self.gate_num:
            return

        # brute-force searching
        # s gate
        for s in range(0, self.qubit_num):
            if self.temp_qubit_dep[s] + 1 <= self.dep:
                new_circuit = self.copy_circuit(temp_circuit)
                S | new_circuit(s)
                self.temp_qubit_dep[s] += 1
                self.search(temp_gate_num + 1, new_circuit)
                self.temp_qubit_dep[s] -= 1

        # hadamard gate
        for h in range(0, self.qubit_num):
            if self.temp_qubit_dep[h] + 1 <= self.dep:
                new_circuit = self.copy_circuit(temp_circuit)
                H | new_circuit(h)
                self.temp_qubit_dep[h] += 1
                self.search(temp_gate_num + 1, new_circuit)
                self.temp_qubit_dep[h] -= 1

        # cnot gate
        for cnot_a in range(0, self.qubit_num):
            for cnot_b in range(0, self.qubit_num):
                if cnot_a != cnot_b:
                    temp_max_dep = max(self.temp_qubit_dep[cnot_a], self.temp_qubit_dep[cnot_b]) + 1
                    if temp_max_dep <= self.dep:
                        new_circuit = self.copy_circuit(temp_circuit)
                        CX | new_circuit([cnot_a, cnot_b])
                        temp_dep_a = self.temp_qubit_dep[cnot_a]
                        temp_dep_b = self.temp_qubit_dep[cnot_b]
                        self.temp_qubit_dep[cnot_a] = temp_max_dep
                        self.temp_qubit_dep[cnot_b] = temp_max_dep
                        self.search(temp_gate_num + 1, new_circuit)
                        self.temp_qubit_dep[cnot_a] = temp_dep_a
                        self.temp_qubit_dep[cnot_b] = temp_dep_b
        return

    def run_template_searching(self):
        circuit_temp = Circuit(self.qubit_num)
        self.search(0, circuit_temp)
        len_list = len(self.template_list)
        relationship_iso = [-1] * len_list
        for i in range(len_list):
            if relationship_iso[i] == -1:
                relationship_iso[i] = i
                for j in range(len_list):
                    if relationship_iso[j] == -1 and not self.check_circuit_not_isomorphism(
                        self.template_list[i][0], self.template_list[j][0]
                    ):
                        self.template_list[i][1] = self.template_list[i][1] and self.template_list[j][1]
                        relationship_iso[j] = i
                        self.template_list[j][1] = False

        return self.template_list
