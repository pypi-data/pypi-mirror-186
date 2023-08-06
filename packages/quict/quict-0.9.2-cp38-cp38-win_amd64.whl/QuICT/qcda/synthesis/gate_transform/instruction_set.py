#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/3/20 4:31 下午
# @Author  : Han Yu
# @File    : instruction_set.py

from QuICT.core.gate import GateType
from .transform_rule.one_qubit_gate_rules import *
from .transform_rule.two_qubit_gate_rules import *


class InstructionSet(object):
    """ InstructionSet describes a set of gates(expectly to be universal set)

    Instruction Set contains gates and some rules, which can be assigned by user.

    Attributes:
        one_qubit_gates(list<GateType>): the types of the one_qubit_gate
        one_qubit_rule(callable): rules to transform SU(2) into instruction set
        two_qubit_gate(GateType): the type of the two_qubit_gate
        rule_map(dictionary): A two-dimensional map from source gate and target gate to transform rule
    """
    # Two-qubit gate and two-qubit rules
    @property
    def two_qubit_gate(self):
        return self.__two_qubit_gate

    @two_qubit_gate.setter
    def two_qubit_gate(self, two_qubit_gate):
        """ set two_qubit_gate

        Args:
            two_qubit_gate(GateType): two-qubit gate in the InstructionSet
        """
        assert isinstance(two_qubit_gate, GateType), TypeError('two_qubit_gate should be a GateType')
        self.__two_qubit_gate = two_qubit_gate

    @property
    def two_qubit_rule_map(self):
        return self.__two_qubit_rule_map

    @two_qubit_rule_map.setter
    def two_qubit_rule_map(self, two_qubit_rule_map):
        self.__two_qubit_rule_map = two_qubit_rule_map

    # One-qubit gates and one-qubit rule
    @property
    def one_qubit_gates(self):
        return self.__one_qubit_gates

    @one_qubit_gates.setter
    def one_qubit_gates(self, one_qubit_gates):
        """ set one_qubit_gates

        Args:
            one_qubit_gates(list<GateType>): one-qubit gates in the InstructionSet
        """
        assert isinstance(one_qubit_gates, list), TypeError('one_qubit_gates should be a list')
        for one_qubit_gate in one_qubit_gates:
            assert isinstance(one_qubit_gate, GateType), TypeError('each one_qubit_gate should be a GateType')
        self.__one_qubit_gates = one_qubit_gates

    @property
    def one_qubit_rule(self):
        """ the rule of decompose 2*2 unitary into target gates

        If not assigned by the register_one_qubit_rule method, some pre-implemented method would be chosen
        corresponding to the one_qubit_gates. An Exception will be raised when no method is chosen.

        Returns:
            callable: the corresponding rule
        """
        if self.__one_qubit_rule:
            return self.__one_qubit_rule
        if set((GateType.rz, GateType.ry)).issubset(set(self.one_qubit_gates)):
            return zyz_rule
        if set((GateType.rz, GateType.rx)).issubset(set(self.one_qubit_gates)):
            return zxz_rule
        if set((GateType.rx, GateType.ry)).issubset(set(self.one_qubit_gates)):
            return xyx_rule
        if set((GateType.h, GateType.rz)).issubset(set(self.one_qubit_gates)):
            return hrz_rule
        if set((GateType.rz, GateType.sx, GateType.x)).issubset(set(self.one_qubit_gates)):
            return ibmq_rule
        if set((GateType.u3)).issubset(set(self.one_qubit_gates)):
            return u3_rule
        raise Exception("please register the SU2 decomposition rule.")

    def __init__(self, two_qubit_gate, one_qubit_gates):
        self.two_qubit_gate = two_qubit_gate
        self.one_qubit_gates = one_qubit_gates
        self.__one_qubit_rule = None
        self.__two_qubit_rule_map = {}

    def select_transform_rule(self, source):
        """ choose a rule which transforms source gate into target gate(2-qubit)

        Args:
            source(GateType): the type of source gate

        Returns:
            callable: the transform rules
        """
        assert isinstance(source, GateType)
        if source in self.two_qubit_rule_map:
            return self.two_qubit_rule_map[source]
        rule = eval(f"{source.name}2{self.two_qubit_gate.name}_rule")
        self.two_qubit_rule_map[source] = rule
        return rule

    def register_one_qubit_rule(self, one_qubit_rule):
        """ register one-qubit gate decompostion rule

        Args:
            one_qubit_rule(callable): decompostion rule
        """
        self.__one_qubit_rule = one_qubit_rule

    def register_two_qubit_rule_map(self, two_qubit_rule, source):
        """ register rule which transforms from source gate into target gate

        Args:
            two_qubit_rule(callable): the transform rule
            source(GateType): the type of source gate
        """
        assert isinstance(source, GateType)
        self.two_qubit_rule_map[source] = two_qubit_rule
