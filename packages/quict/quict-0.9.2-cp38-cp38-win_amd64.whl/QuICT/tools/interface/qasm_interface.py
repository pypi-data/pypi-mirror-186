#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/3/22 10:31
# @Author  : Han Yu
# @File    : _qasmInterface.py

import os
from collections import OrderedDict
from configparser import ConfigParser

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.core.utils import GateType
from QuICT.lib import Qasm
from QuICT.tools.exception.core import QASMError

from .basic_interface import BasicInterface


class qasm_qreg(object):
    """ the target bit in the qasm grammer tree

    """

    def __init__(self, index_list, name):
        self.index = index_list
        self.name = name


class qasm_creg(object):
    """ the control bit in the qasm grammer tree

    """

    def __init__(self, index_list, name):
        self.index = index_list
        self.name = name


class OPENQASMInterface(BasicInterface):
    # qasm mapping to QuICT
    standard_extension = {
        "u1": GateType.u1,
        "u2": GateType.u2,
        "u3": GateType.u3,
        "U": GateType.u3,
        "x": GateType.x,
        "y": GateType.y,
        "z": GateType.z,
        "t": GateType.t,
        "tdg": GateType.tdg,
        "s": GateType.s,
        "sdg": GateType.sdg,
        "sx": GateType.sx,
        "sy": GateType.sy,
        "sw": GateType.sw,
        "p": GateType.phase,
        "phase": GateType.gphase,
        "swap": GateType.swap,
        "iswap": GateType.iswap,
        "iswapdg": GateType.iswapdg,
        "sqiswap": GateType.sqiswap,
        "rx": GateType.rx,
        "ry": GateType.ry,
        "rz": GateType.rz,
        "id": GateType.id,
        "h": GateType.h,
        "hy": GateType.hy,
        "cx": GateType.cx,
        "ccx": GateType.ccx,
        "ccz": GateType.ccz,
        "cy": GateType.cy,
        "cz": GateType.cz,
        "ch": GateType.ch,
        "crz": GateType.crz,
        "ccrz": GateType.ccrz,
        "rzz": GateType.rzz,
        "rxx": GateType.rxx,
        "ryy": GateType.ryy,
        "rzx": GateType.rzx,
        "cu1": GateType.cu1,
        "cu3": GateType.cu3,
        "cswap": GateType.cswap,
        "fsim": GateType.fsim
    }

    token = None

    DEFAULT_QUICT_PATH = os.path.join(os.path.expanduser("~"),
                                      '.QuICT')

    DEFAULT_QUICT_FILE = os.path.join(os.path.expanduser("~"),
                                      '.QuICT', 'accounts.ini')

    @staticmethod
    def load_circuit(circuit: Circuit):
        instance = OPENQASMInterface()
        instance.circuit = circuit
        instance.analyse_code_from_circuit()
        return instance

    @staticmethod
    def load_file(filename: str):
        instance = OPENQASMInterface()
        instance.ast = Qasm(filename).parse()
        instance.analyse_circuit_from_ast(instance.ast)
        return instance

    @staticmethod
    def load_string(qasm: str):
        instance = OPENQASMInterface()
        instance.ast = Qasm(data=qasm).parse()
        instance.analyse_circuit_from_ast(instance.ast)
        return instance

    def __init__(self):
        super().__init__()
        self.circuit = None
        self.ast = None
        self.qasm = None

        self.qbits = 0
        self.cbits = 0
        self.valid_circuit = False
        self.valid_qasm = False
        self.gates = OrderedDict()
        self.node_gates = []
        self.qregs = {}
        self.cregs = {}
        self.arg_stack = [{}]
        self.bit_stack = [{}]
        self.circuit_gates = []
        self.version = None

    def analyse_circuit_from_ast(self, node):
        self.valid_circuit = True
        self.analyse_node(node)
        if self.valid_circuit:
            self.circuit = Circuit(self.qbits)
            self.circuit.extend(self.circuit_gates)

    def analyse_code_from_circuit(self):
        self.valid_qasm = True
        self.qasm = self.circuit.qasm()
        if self.qasm == "error":
            self.qasm = None
            self.valid_qasm = False

    def output_qasm(self, filename=None):
        if not self.valid_qasm or self.qasm is None:
            if self.circuit is None:
                return
            self.qasm = self.circuit.qasm()
            if self.qasm != 'error':
                self.valid_qasm = True
            else:
                return False
        if filename is None:
            print(self.qasm)
        else:
            with open(filename, 'w+') as file:
                file.write(self.qasm)

    def enable_path(self):
        if not os.path.exists(self.DEFAULT_QUICT_PATH):
            os.mkdir(self.DEFAULT_QUICT_PATH)

    def load_token(self):
        self.enable_path()
        config_parser = ConfigParser()
        config_parser.read(self.DEFAULT_QUICT_FILE)
        if 'account' in config_parser:
            dic = dict(config_parser.items('account'))
            if 'token' in dic:
                self.token = dic['token']

    def save_token(self, token):
        self.token = token
        self.enable_path()
        config_parser = ConfigParser()
        config_parser['account'] = {
            'token': token,
        }
        with open(self.DEFAULT_QUICT_FILE, 'w') as f:
            config_parser.write(f)

    def analyse_node(self, node):
        if not self.valid_circuit:
            return
        if node.type == "program":
            for child in node.children:
                self.analyse_node(child)

        elif node.type == "qreg":
            self.qregs[node.name] = qasm_qreg([i for i in range(self.qbits, self.qbits + node.index)], node.name)
            self.qbits += node.index

        elif node.type == "creg":
            self.cregs[node.name] = qasm_creg([i for i in range(self.cbits, self.cbits + node.index)], node.name)
            self.cbits += node.index

        elif node.type == "id_list":
            return [self.get_analyse_id(child) for child in node.children]

        elif node.type == "primary_list":
            return [self.get_analyse_id(child) for child in node.children]

        elif node.type == "gate":
            self.analyse_gate(node)

        elif node.type == "custom_unitary":
            self.analyse_custom(node)

        elif node.type == "universal_unitary":
            QASMError("universal_unitary is deprecated", node.line, node.file)

        elif node.type == "cnot":
            self.analyse_cnot(node)

        elif node.type == "expression_list":
            return node.children

        elif node.type == "measure":
            self.analyse_measure(node)

        elif node.type == "format":
            self.version = node.version()

        elif node.type == "barrier":
            pass

        elif node.type == "reset":
            self.analyse_reset(node)

        elif node.type == "if":
            self.analyse_if(node)

        elif node.type == "opaque":
            self.analyse_opaque(node)

        else:
            QASMError("QASM grammer error", node.line, node.file)

    def analyse_gate(self, node):
        self.gates[node.name] = {}
        de_gate = self.gates[node.name]
        de_gate["n_args"] = node.n_args()
        de_gate["n_bits"] = node.n_bits()
        if node.n_args() > 0:
            de_gate["args"] = [element.name for element in node.arguments.children]
        else:
            de_gate["args"] = []
        de_gate["bits"] = [child.name for child in node.bitlist.children]
        if node.name in self.standard_extension:
            return
        de_gate["body"] = node.body

    def analyse_custom(self, node):
        name = node.name
        if node.arguments is not None:
            args = self.analyse_node(node.arguments)
        else:
            args = []
        bits = [
            self.get_analyse_id(node_element)
            for node_element in node.bitlist.children
        ]
        if name in self.gates:
            gargs = self.gates[name]["args"]
            gbits = self.gates[name]["bits"]

            maxidx = max(map(len, bits))
            for idx in range(maxidx):
                self.arg_stack.append({gargs[j]: args[j]
                                       for j in range(len(gargs))})
                element = [idx * x for x in
                           [len(bits[j]) > 1 for j in range(len(bits))]]
                self.bit_stack.append({gbits[j]: bits[j][element[j]]
                                       for j in range(len(gbits))})
                self.analyse_name(name,
                                  gargs,
                                  gbits)
                self.arg_stack.pop()
                self.bit_stack.pop()
        else:
            raise QASMError("undefined gate:", node.line, node.file)

    def analyse_cnot(self, node):
        id0 = self.get_analyse_id(node.children[0])
        id1 = self.get_analyse_id(node.children[1])
        if not (len(id0) == len(id1) or len(id0) == 1 or len(id1) == 1):
            raise QASMError("the number of bits unmatched:", node.line, node.file)

        maxidx = max([len(id0), len(id1)])
        for idx in range(maxidx):
            if len(id0) > 1 and len(id1) > 1:
                qubit_idxes = [id0[idx], id1[idx]]
            elif len(id0) > 1:
                qubit_idxes = [id0[idx], id1[0]]
            else:
                qubit_idxes = [id0[0], id1[idx]]

            cx_gate = build_gate(GateType.cx, qubit_idxes)
            self.circuit_gates.append(cx_gate)

    def analyse_measure(self, node):
        id0 = self.get_analyse_id(node.children[0])
        id1 = self.get_analyse_id(node.children[1])
        if len(id0) != len(id1):
            raise QASMError("the number of bits of registers unmatched:", node.line, node.file)

        for idx, _ in zip(id0, id1):
            m_gate = build_gate(GateType.measure, [idx])
            self.circuit_gates.append(m_gate)

    def analyse_reset(self, node):
        id0 = self.get_analyse_id(node.children[0])
        for i, _ in enumerate(id0):
            r_gate = build_gate(GateType.reset, [id0[i]])
            self.circuit_gates.append(r_gate)

    def analyse_if(self, node):
        print("if op is not supported:{}", node.type)
        self.valid_circuit = False

    def analyse_opaque(self, node):
        pass

    def analyse_name(self, name, gargs, gbits):
        if name in self.standard_extension:
            pargs = [self.arg_stack[-1][s].sym(self.arg_stack[:-1]) for s in gargs]
            targs = [self.bit_stack[-1][s] for s in gbits]
            type = self.standard_extension[name]
            gate = build_gate(type, targs, pargs)
            self.circuit_gates.append(gate)
        else:
            body = self.gates[name]['body']
            for child in body.children:
                if child.arguments is not None:
                    args = self.analyse_node(child.arguments)
                else:
                    args = []
                bits = [
                    self.get_analyse_id(node_element)
                    for node_element in child.bitlist.children
                ]
                gargs = self.gates[child.name]["args"]
                gbits = self.gates[child.name]["bits"]

                maxidx = max(map(len, bits))
                for idx in range(maxidx):
                    self.arg_stack.append({gargs[j]: args[j]
                                           for j in range(len(gargs))})
                    element = [idx * x for x in
                               [len(bits[j]) > 1 for j in range(len(bits))]]
                    self.bit_stack.append({gbits[j]: bits[j][element[j]]
                                           for j in range(len(gbits))})
                    self.analyse_name(child.name,
                                      gargs,
                                      gbits)
                    self.arg_stack.pop()
                    self.bit_stack.pop()

    def get_analyse_id(self, node):
        if node.name in self.qregs:
            reg = self.qregs[node.name]
        elif node.name in self.cregs:
            reg = self.cregs[node.name]
        elif self.bit_stack[-1] and node.name in self.bit_stack[-1]:
            reg = self.bit_stack[-1][node.name]
        else:
            raise QASMError("expected qreg or creg name:", node.line, node.file)

        if node.type == "indexed_id":
            return [reg.index[node.index]]
        elif node.type == "id":
            if not self.bit_stack[-1]:
                return [bit for bit in reg.index]
            else:
                if node.name in self.bit_stack[-1]:
                    return [self.bit_stack[-1][node.name]]
                raise QASMError("expected qreg or creg name:", node.line, node.file)
        return None
