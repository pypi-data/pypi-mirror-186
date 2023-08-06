#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/3/15 1:38
# @Author  : Han Yu
# @File    : _basicInterface.py

from QuICT.core import Circuit


class BasicInterface(object):
    """ the basic interface of general processor

    these interface is devoted to make out circuit more general,
    for example, mutual conversion with qiskit code or OpenQASM 2.0 code.

    the function "load_circuit" and "load_file" should be overloaded

    Attributes:
        circuit(Circuit): the circuit in our framework
        text_content: another form content

    """

    @property
    def circuit(self):
        return self.__circuit

    @circuit.setter
    def circuit(self, circuit):
        self.__circuit = circuit

    @property
    def text_content(self):
        return self.__text_content

    @text_content.setter
    def text_content(self, text_content):
        self.__text_content = text_content

    def __init__(self):
        self.circuit = None
        self.text_content = None

    @staticmethod
    def load_circuit(circuit: Circuit):
        """ load the circuit from our framework

        Args:
            circuit(Circuit): the circuit to be loaded

        """
        instance = BasicInterface()
        instance.circuit = circuit
        return instance

    @staticmethod
    def load_file(filename: str):
        """ load the content from our file

        Args:
            filename(str): filename

        """
        instance = BasicInterface()
        with open(filename) as file:
            instance.text_content = file.read()
        return instance
