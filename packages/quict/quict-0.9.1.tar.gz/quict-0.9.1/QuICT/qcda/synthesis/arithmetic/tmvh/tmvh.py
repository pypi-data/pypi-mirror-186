#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/11/5 10:55
# @Author  : Zhu Qinlin
# @File    : tmvh.py

from QuICT.core.gate import CX, CCX, CompositeGate, X


def peres_gate(gate_set, a, b, c):
    """
    (a, b, c) -> (a, a xor b, a.b xor c)

    Args:
        a(Qubit): qubit
        b(Qubit): qubit
        c(Qubit): qubit
    """
    with gate_set:
        CCX & (a, b, c)
        CX & (a, b)


def adder_overflow(gate_set, a, b, overflow):
    """
     store a + b in b

    (a,b,overflow) -> (a,b'=a+b,overflow'=overflow xor highest_carry)

    Args:
        a(Qureg): the qureg stores a, length is n
        b(Qureg): the qureg stores b, length is n
        overflow(Qureg): the ancillary qubits, length is 1

    reference: HIMANSHU THAPLIYAL and NAGARAJAN RANGANATHAN -
    Design of Efficient Reversible Logic Based Binary and BCD Adder Circuits
    https://arxiv.org/abs/1712.02630v1
    """

    n = len(a)
    with gate_set:
        if n == 1:
            peres_gate(gate_set, a[0], b[0], overflow)
            return

        # step 1
        for i in range(n - 1):
            CX & (a[i], b[i])

        # step 2
        CX & (a[0], overflow)
        for i in range(n - 2):
            CX & (a[i + 1], a[i])

        # step 3
        for i in range(n - 1):
            CCX & (a[n - 1 - i], b[n - 1 - i], a[n - 2 - i])

        # step 4
        peres_gate(gate_set, a[0], b[0], overflow)
        for i in range(n - 1):
            peres_gate(gate_set, a[i + 1], b[i + 1], a[i])

        # step 5
        for i in range(n - 2):
            CX & (a[n - 2 - i], a[n - 3 - i])

        # step 6
        for i in range(n - 1):
            CX & (a[i], b[i])


def adder(gate_set, a, b):
    """
    (a,b) -> (a,b'=a+b)

    Args:
        a(Qureg): the qureg stores a, length is n
        b(Qureg): the qureg stores b, length is n

    reference: HIMANSHU THAPLIYAL and NAGARAJAN RANGANATHAN -
    Design of Efficient Reversible Logic Based Binary and BCD Adder Circuits
    https://arxiv.org/abs/1712.02630v1
    """

    n = len(a)

    with gate_set:
        # step 1
        for i in range(n - 1):
            CX & (a[i], b[i])

        # step 2
        for i in range(n - 2):
            CX & (a[i + 1], a[i])

        # step 3
        for i in range(n - 1):
            CCX & (a[n - 1 - i], b[n - 1 - i], a[n - 2 - i])

        # step 4
        CX & (a[0], b[0])
        for i in range(n - 1):
            peres_gate(gate_set, a[i + 1], b[i + 1], a[i])

        # step 5
        for i in range(n - 2):
            CX & (a[n - 2 - i], a[n - 3 - i])

        # step 6
        for i in range(n - 1):
            CX & (a[i], b[i])


def subtraction_overflow(gate_set, a, b, overflow):
    """
    (a,b) -> (a,b-a)
    """
    n = len(b)
    with gate_set:
        for i in range(n):
            X & b[i]
        X & overflow
        adder_overflow(gate_set, a, b, overflow)
        for i in range(n):
            X & b[i]
        X & overflow


def ctrl_add_overflow_ancilla(gate_set, ctrl, a, b, overflow, ancilla):
    """
    (c,a,b,of,ancilla) -> (c,a,b+c*a,of',ancilla)
    """
    n = len(a)
    with gate_set:
        if n == 1:
            # CCX | (a[0],b[0],overflow)
            CCX & (a[0], b[0], ancilla)
            CCX & (ancilla, ctrl, overflow)
            CCX & (a[0], b[0], ancilla)
            CX  & (a[0], b[0])
            return

        # step 1
        for i in range(n - 1):
            CX & (a[i], b[i])
        # step 2
        CCX & (ctrl, a[0], overflow)
        for i in range(n - 2):
            CX & (a[i + 1], a[i])
        # step 3
        for i in range(n - 1):
            CCX & (a[n - 1 - i], b[n - 1 - i], a[n - 2 - i])
        # step 4
        CCX & (a[0], b[0], ancilla)
        CCX & (ctrl, ancilla, overflow)
        CCX & (a[0], b[0], ancilla)
        CCX & (ctrl, a[0], b[0])
        # step 5
        for i in range(n - 1):
            CCX & (a[i + 1], b[i + 1], a[i])
            CCX & (ctrl, a[i + 1], b[i + 1])
        # step 6
        for i in range(n - 2):
            CX & (a[n - 2 - i], a[n - 3 - i])
        # step 7
        for i in range(n - 1):
            CX & (a[i], b[i])


def ctrl_add(gate_set, ctrl, a, b):
    """
    (ctrl,a,b) -> (ctrl,a,b+a)
    """
    n = len(a)
    # step 1
    with gate_set:
        for i in range(n - 1):
            CX & (a[i], b[i])
        # step 2
        # CCX | (ctrl,a[0],ancilla)
        for i in range(n - 2):
            CX & (a[i + 1], a[i])
        # step 3
        for i in range(n - 1):
            CCX & (a[n - 1 - i], b[n - 1 - i], a[n - 2 - i])
        # step 4
        # CCX | (a[0],b[0],ancilla)
        # CCX | (ctrl,ancilla,overflow)
        # CCX | (a[0],b[0],ancilla)
        CCX & (ctrl, a[0], b[0])
        # step 5
        for i in range(n - 1):
            CCX & (a[i + 1], b[i + 1], a[i])
            CCX & (ctrl, a[i + 1], b[i + 1])
        # step 6
        for i in range(n - 2):
            CX & (a[n - 2 - i], a[n - 3 - i])
        # step 7
        for i in range(n - 1):
            CX & (a[i], b[i])


def mult(gate_set, a, b, p, ancilla):
    """
    Multiplicant: a, b
    Product: p
    (a, b, p=0, ancilla=0) -> (a, b, a*b, ancilla=0)
    """
    n = len(a)
    with gate_set:
        if n == 1:
            CCX & (a[0], b[0], p[1])
            return

        # step 1
        for i in range(n):
            CCX & (b[n - 1], a[n - 1 - i], p[2 * n - 1 - i])
        # step 2
        for i in range(n - 2):
            ctrl_add_overflow_ancilla(
                gate_set,
                b[n - 2 - i],
                a,
                p[n - 1 - i:2 * n - 1 - i],
                p[n - 2 - i],
                p[n - 3 - i]
            )
        ctrl_add_overflow_ancilla(
            gate_set,
            b[0],
            a,
            p[1:n + 1],
            p[0],
            ancilla
        )


def division(gate_set, a, b, r, ancilla):
    """
    Divided: a
    Divisor: b
    (a,b,r=0,ancilla=0) -> (a%b,b,a//b,ancilla)
    """
    n = len(a)
    with gate_set:
        for i in range(n - 1):
            # Iteration(y,b,r[i])
            y = r[i + 1:n] + a[0:i + 1]
            subtraction_overflow(gate_set, b, y, ancilla)
            CX & (ancilla, r[i])
            ctrl_add(gate_set, ancilla, b, y)
            CX & (r[i], ancilla)
            X & r[i]
        # Iteration(a,b,r[n-1])
        subtraction_overflow(gate_set, b, a, ancilla)
        CX & (ancilla, r[n - 1])
        ctrl_add(gate_set, ancilla, b, a)
        CX & (r[n - 1], ancilla)
        X & r[n - 1]


class RippleCarryAdder(object):
    """
    (a,b) -> (a,b'=a+b)
    Args:
        n(int): the bit number of a and b

    Quregs:
        a_q(Qureg): the qureg stores a, n qubits.
        b_q(Qureg): the qureg stores b, and stores the sum
                    after computation, n qubits.
    reference: HIMANSHU THAPLIYAL and NAGARAJAN RANGANATHAN -
    Design of Efficient Reversible Logic Based Binary and BCD adder Circuits
    https://arxiv.org/abs/1712.02630v1
    """

    @staticmethod
    def execute(n):
        """
        Construct a compositegate tailored to the size n
        """
        gate_set = CompositeGate()
        a_q = list(range(n))
        b_q = list(range(n, 2 * n))

        adder(gate_set, a_q, b_q)
        return gate_set


class Multiplication(object):
    """
    (a,b,p=0,ancilla=0) -> (a,b,p=a*b,ancilla=0)

    Args:
        n(int): the bit number of a and b

    Quregs:
        a_q(Qureg): the qureg stores a, n qubits.
        b_q(Qureg): the qureg stores b, n qubits.
        p_q(Qureg): the qureg stores the product, 2n qubits.
        ancilla(Qubit): the clean ancilla qubit, 1 qubit.

    reference: Edgard Mu˜noz-Coreas, Himanshu Thapliya -
    T-count Optimized Design of Quantum Integer Multiplication
    https://arxiv.org/abs/1706.05113v1
    """

    @staticmethod
    def execute(n):
        """
        Construct a compositegate tailored to the size n
        """
        gate_set = CompositeGate()
        a_q = list(range(n))
        b_q = list(range(n, 2 * n))
        p_q = list(range(2 * n, 4 * n))
        ancilla = 4 * n

        mult(gate_set, a_q, b_q, p_q, ancilla)

        return gate_set


class RestoringDivision(object):
    """
    (a,b,r=0,overflow=0) -> (a%b,b,a//b,0)
    Args:
        n(int): the bit number of a and b
    Quregs:
        a_q(Qureg): the qureg stores a, n qubits.
        b_q(Qureg): the qureg stores b, and stores the quotient
                    after computation, n qubits.
        r_q(Qureg): the qureg stores the remainder, n qubits.
        of_q(Qubit): the clean ancilla qubit, 1 qubit.
    reference: Himanshu Thapliyal, Edgard Munoz-Coreas, T. S. S. Varun, and Travis S. Humble -
    Quantum Circuit Designs of Integer Division Optimizing T-count and T-depth
    http://arxiv.org/abs/1809.09732v1
    """

    @staticmethod
    def execute(n):
        """
        Construct a compositegate tailored to the size n
        """
        gate_set = CompositeGate()
        a_q = list(range(n))
        b_q = list(range(n, 2 * n))
        r_q = list(range(2 * n, 3 * n))
        of_q = 3 * n

        division(gate_set, a_q, b_q, r_q, of_q)

        return gate_set
