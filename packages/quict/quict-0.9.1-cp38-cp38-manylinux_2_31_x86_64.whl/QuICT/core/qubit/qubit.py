#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/17 8:44
# @Author  : Han Yu, Li Kaiqi
# @File    : qubit.py
import random
from typing import Union

from QuICT.core.utils import unique_id_generator
from QuICT.tools.exception.core import TypeError, ValueError, IndexExceedError, QubitMeasureError


class Qubit(object):
    """ Implement a quantum bit

    Qubit is the basic unit of quantum circuits, it will appear with some certain circuit.

    Attributes:
        id(int): the unique identity code of a qubit, which is generated globally.
        measured(int):
            the measure result of the qubit.
            After apply measure gate on the qubit, the measured will be 0 or 1,
            otherwise raise an exception
        prob(float):
            the probability of measure result to be 1, which range in [0, 1].
            After apply measure gate on the qubit, this attribute can be read,
            otherwise raise an exception
        historical_measured(list):
            Record all measured result of current qubits.
    """

    @property
    def id(self):
        return self._id

    @property
    def measured(self) -> int:
        return self._measured

    @measured.setter
    def measured(self, measured):
        self._measured = measured
        if self._measured is not None:
            self._historical_measured.append(self._measured)

    @property
    def historical_measured(self):
        return self._historical_measured

    @property
    def prob(self) -> float:
        return self._prob

    @prob.setter
    def prob(self, prob):
        self._prob = prob

    def __init__(self, prob: float = random.random()):
        """ initial a qubit with a circuit

        Args:
            circuit(Circuit): the circuit the qubit attaches to
        """
        self._id = unique_id_generator()
        self._measured = None
        self._prob = prob
        self._historical_measured = []

    def __str__(self):
        """ string describe of the qubit

        Returns:
            str: a simple describe
        """
        return f"qubit id: {self.id}"

    def __int__(self):
        """ int value of the qubit(measure result)

        Returns:
            int: measure result

        Raises:
            The qubit has not be measured.
        """
        if self.measured is None:
            raise QubitMeasureError(f"The qubit {self.id} has not be measured")

        return self.measured

    def __bool__(self):
        """ int value of the qubit(measure result)

        Returns:
            bool: measure result

        Raises:
            The qubit has not be measured.
        """
        return bool(int(self))

    def reset(self):
        """ Reset self qubit status. """
        self._historical_measured = []
        self._measured = None


class Qureg(list):
    """ Implement a quantum register

    Qureg is a list of Qubits, which is a subClass of list.

    Attributes:
        qubits([Qubits]): the list of qubits.
    """
    def __init__(self, qubits=None):
        """ initial a qureg with qubit(s)

        Args:
            qubits: the qubits which make up the qureg, it can have below form,
                1) int
                2) qubit
                3) [qubits/quregs]
        """
        super().__init__()
        if qubits is None:
            return

        if isinstance(qubits, int):
            for _ in range(qubits):
                self.append(Qubit())
        elif isinstance(qubits, Qubit):
            self.append(qubits)
        elif isinstance(qubits, list):
            for qubit in qubits:
                if isinstance(qubit, Qubit):
                    self.append(qubit)
                elif isinstance(qubit, Qureg):
                    for qbit in qubit:
                        self.append(qbit)
                else:
                    raise TypeError("Qureg.qubits", "int/Qubit/list<Qubit/Qureg>", type(qubit))
        else:
            raise TypeError("Qureg.qubits", "int/Qubit/list<Qubit/Qureg>", type(qubit))

    def __call__(self, indexes: object):
        """ get a smaller qureg from this qureg

        Args:
            indexes: the indexes passed in, it can have follow form:
                1) int
                2) list<int>
        Returns:
            Qubit[s]: the qureg correspond to the indexes
        """
        if isinstance(indexes, int):
            return Qureg(self[indexes])

        return self[indexes]

    def __getitem__(self, item):
        """ to fit the slice operator, overloaded this function.

        get a smaller qureg/qubit from this qureg

        Args:
            item(int/slice): slice passed in.

        Return:
            Qubit/Qureg: the result or slice
        """
        if isinstance(item, int):
            return super().__getitem__(item)

        qureg = Qureg()
        if isinstance(item, slice):
            qureg_list = super().__getitem__(item)
            for qubit in qureg_list:
                qureg.append(qubit)
        elif isinstance(item, list) or isinstance(item, tuple):
            for idx in item:
                assert isinstance(idx, int), TypeError("Qureg.getitem.item.value", "int", type(idx))
                if idx < 0 or idx > len(self):
                    raise IndexExceedError("Qureg.getitem", [0, len(self)], idx)

                qureg.append(self[idx])
        else:
            raise TypeError("Qureg.getitem", "int/list[int]/slice", type(item))

        return qureg

    def __int__(self):
        """ the value of the register

        Return the value of the register if all qubits have been measured.
        Note that the compute mode is BigEndian.

        Returns:
            int: the value of the register

        Raises:
            Exception: some qubit has not be measured
        """
        value = 0
        for qubit in self:
            if qubit.measured is None:
                raise QubitMeasureError(f"The qubit {qubit.id} has not be measured")

            value <<= 1
            if qubit.measured == 1:
                value += 1

        return value

    def __str__(self):
        """ the string of the value of the register

        Returns:
            str: the value of the qureg
        """
        bit_idx = "{0:0b}".format(self.__int__())
        bit_idx.zfill(len(self))

        return bit_idx

    def __add__(self, other):
        """ get a combined qureg with this qureg and other qureg

        Args:
            other(Qureg): qureg to be added.

        Return:
            Qureg: the result or slice
        """
        return Qureg([self, other])

    def __iadd__(self, other):
        """ get a combined qureg with this qureg and other qureg

        Args:
            other(Qureg): qureg to be added.

        Return:
            Qureg: the result or slice
        """
        if isinstance(other, Qubit):
            self.append(other)
        elif isinstance(other, Qureg):
            for q in other:
                self.append(q)
        else:
            raise TypeError("Qureg.iadd", "Qureg/Qubit", type(other))

        return self

    def __eq__(self, other):
        """
        check two qureg is same or not. Iff all qubits in two qureg are same will
        return True; otherwise, return False.

        Args:
            other(Qureg): qureg to be checked.
        """
        assert isinstance(other, Qureg), TypeError("Qureg.eq", "Qureg", type(other))
        if not len(other) == len(self):
            return False

        current_qubit_ids = [qubit.id for qubit in self]
        for qubit in other:
            if qubit.id not in current_qubit_ids:
                return False

        return True

    def diff(self, other):
        """ return different qubits between two quregs

        Args:
            other (Qureg): The compare qureg

        Returns:
            Qureg: The qureg with different qubits
        """
        qubit_ids = [qubit.id for qubit in self]
        diff_qubit = []

        for qubit in other:
            if qubit.id not in qubit_ids:
                diff_qubit.append(qubit)

        return Qureg(diff_qubit)

    def index(self, qubit: Union[str, Qubit]):
        if isinstance(qubit, Qubit):
            return super().index(qubit)

        for idx, item in enumerate(self):
            if item.id == qubit:
                return idx

        raise ValueError("Qureg.index.qubit", "within current Qureg", "qubit is not")

    def reset_qubits(self):
        """ Reset all qubits' status. """
        for qubit in self:
            qubit.reset()
