#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/11/5 10:55
# @Author  : Han Yu
# @File    : VBE.py

from numpy import gcd

from QuICT.core import Circuit
from QuICT.core.gate import CompositeGate, X, CX, CCX, Swap


def Inverse(a, N):
    """ Inversion of a in (mod N)

    Args:
        a(int): the parameter a
        N(int): the parameter N

    """
    for i in range(N):
        if i * a % N == 1:
            return i
    return None


def Set(qreg, N):
    """ Set the qreg as N, using X gates on specific qubits

    Args:
        qreg(Qureg): the qureg to be set
        N(int): the parameter N

    """

    string = bin(N)[2:]
    n = len(qreg)
    m = len(string)
    if m > n:
        print('When set qureg as N=%d, N exceeds the length of qureg n=%d, thus is truncated' % (N, n))

    for i in range(min(n, m)):
        if string[m - 1 - i] == '1':
            X | qreg[n - 1 - i]


def ControlSet(control, qreg, N):
    """ Set the qreg as N, using CX gates on specific qubits

    Args:
        control(Qubit): qubit of control bits
        qreg(Qureg): the qureg to be set
        N(int): the parameter N

    """
    string = bin(N)[2:]
    n = len(qreg)
    m = len(string)
    if m > n:
        print(
            f'When cset qureg as N={N}, N exceeds the length of qureg n={n}, thus is truncated')

    for i in range(min(n, m)):
        if string[m - 1 - i] == '1':
            CX | (control, qreg[n - 1 - i])


def CControlSet(control1, control2, qreg, N):
    """ Set the qreg as N, using CCX gates on specific qubits

    Args:
        control1(Qubit): 1st qubit of control bits
        control2(Qubit): 2nd qubit of control bits
        qreg(Qureg): the qureg to be set
        N(int): the parameter N

    """
    string = bin(N)[2:]
    n = len(qreg)
    m = len(string)
    if m > n:
        print(
            f'When ccset qureg as N={N}, N exceeds the length of qureg n={n}, thus is truncated')

    for i in range(min(n, m)):
        if string[m - 1 - i] == '1':
            CCX | (control1, control2, qreg[n - 1 - i])


def Carry(c_in, a, b, c_out):
    """ Carry for one bit plus

    (c_in,a,b,c_out=0) -> (c_in,a,b,c_out')

    Args:
        c_in(Qubit): c_in
        a(Qubit): a
        b(Qubit): b
        c_out(Qubit): c_out

    """
    CCX | (a, b, c_out)
    CX | (a, b)
    CCX | (c_in, b, c_out)


def ReverseCarry(c_in, a, b, c_out):
    """ the inverse of Carry

    Args:
        c_in(Qubit): c_in
        a(Qubit): a
        b(Qubit): b
        c_out(Qubit): c_out
    """
    CCX | (c_in, b, c_out)
    CX | (a, b)
    CCX | (a, b, c_out)


def Sum(c_in, a, b):
    """ Sum circuit

    (c_in,a,b) -> (c_in,a,b'=a+b+c_in)

    Args:
        c_in(Qubit): c_in
        a(Qubit): a
        b(Qubit): b
    """
    CX | (a, b)
    CX | (c_in, b)


def ReverseSum(c_in, a, b):
    """ Reverse of Sum

    Args:
        c_in(Qubit): c_in
        a(Qubit): a
        b(Qubit): b
    """
    CX | (c_in, b)
    CX | (a, b)


def PlainAdder(a, b, c, overflow):
    """ store a + b in b

    (a,b,c=0,overflow=0) -> (a,b'=a+b,c,overflow')


    Args:
        a(Qureg): the qureg stores a, length is n
        b(Qureg): the qureg stores b, length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1

    """
    n = len(a)

    for i in range(n - 1):
        Carry(c[n - 1 - i], a[n - 1 - i], b[n - 1 - i], c[n - 2 - i])
    Carry(c[0], a[0], b[0], overflow)

    CX | (a[0], b[0])
    Sum(c[0], a[0], b[0])

    for i in range(n - 1):
        ReverseCarry(c[1 + i], a[1 + i], b[1 + i], c[i])
        Sum(c[1 + i], a[1 + i], b[1 + i])


def ReversePlainAdder(a, b, c, overflow):
    """ the inverse of plainAdder

    Args:
        a(Qureg): the qureg stores a, length is n
        b(Qureg): the qureg stores b, length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1

    """
    n = len(a)

    for i in range(n - 1):
        ReverseSum(c[n - 1 - i], a[n - 1 - i], b[n - 1 - i])
        Carry(c[n - 1 - i], a[n - 1 - i], b[n - 1 - i], c[n - 2 - i])

    ReverseSum(c[0], a[0], b[0])
    CX | (a[0], b[0])

    ReverseCarry(c[0], a[0], b[0], overflow)
    for i in range(n - 1):
        ReverseCarry(c[1 + i], a[1 + i], b[1 + i], c[i])


def AdderMod(N, a, b, c, overflow, qubit_N, t):
    """ store (a+b) mod N in b

    (a,b,c=0,overflow=0,qubit_N=0,t=0) ->
     (a,b'=(a+b)mod N,c,overflow',qubit_N=0,t=0)

    Args:
        N(int): the parameter N
        a(Qureg): the qureg stores a, length is n
        b(Qureg): the qureg stores b, length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1
        qubit_N(Qureg): the ancillary qubits, length is n
        t(Qureg): the ancillary qubits, length is 1

    """
    n = len(qubit_N)

    Set(qubit_N, N)
    PlainAdder(a, b, c, overflow)
    for i in range(n):
        Swap | (a[i], qubit_N[i])
    ReversePlainAdder(a, b, c, overflow)
    X | overflow
    CX | (overflow, t)
    X | overflow
    ControlSet(t, a, N)
    PlainAdder(a, b, c, overflow)
    ControlSet(t, a, N)
    for i in range(n):
        Swap | (a[i], qubit_N[i])
    ReversePlainAdder(a, b, c, overflow)
    CX | (overflow, t)
    PlainAdder(a, b, c, overflow)
    Set(qubit_N, N)


def ReverseAdderMod(N, a, b, c, overflow, qubit_N, t):
    """ Reverse of AdderMod """
    n = len(qubit_N)

    Set(qubit_N, N)
    ReversePlainAdder(a, b, c, overflow)
    CX | (overflow, t)
    PlainAdder(a, b, c, overflow)
    for i in range(n):
        Swap | (a[i], qubit_N[i])
    ControlSet(t, a, N)
    ReversePlainAdder(a, b, c, overflow)
    ControlSet(t, a, N)
    X | overflow
    CX | (overflow, t)
    X | overflow
    PlainAdder(a, b, c, overflow)
    for i in range(n):
        Swap | (a[i], qubit_N[i])
    ReversePlainAdder(a, b, c, overflow)
    Set(qubit_N, N)


def MulAddMod(a, N, x, qubit_a, b, c, overflow, qubit_N, t):
    """ store b + x*a mod N in b

    (x,qubit_a=0,b,c=0,overflow=0,qubit_N=0,t=0) ->
    (x,qubit_a=0,b'=b+a*x mod N,c,overflow',qubit_N,t)

    Args:
        a(int): the parameter a
        N(int): the parameter N
        x(Qureg): the qureg stores x, length is m
        qubit_a(Qureg): the ancillary qubits, length is n
        b(Qureg): length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1
        qubit_N(Qureg): the ancillary qubits, length is n
        t(Qureg): the ancillary qubits, length is 1
    """

    n = len(qubit_N)

    for i in range(n):
        ControlSet(x[n - 1 - i], qubit_a, a)
        AdderMod(N, qubit_a, b, c, overflow, qubit_N, t)
        ControlSet(x[n - 1 - i], qubit_a, a)
        a = (a * 2) % N


def ControlMulMod(a, N, control, x, qubit_a, b, c, overflow, qubit_N, t):
    """ store x*(a^control) mod N in b

    (control,x,qubit_a=0,b=0,c=0,overflow=0,qubit_N=0,t=0) ->
     (control,x,qubit_a=0,b'=(a**control)*x mod N,c,overflow',qubit_N,t)

    Args:
        a(int): the parameter a
        N(int): the parameter N
        control(Qureg): the control qureg to store the result, length is 1
        x(Qureg): the qureg stores x, length is m
        qubit_a(Qureg): the ancillary qubits, length is n
        b(Qureg): length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1
        qubit_N(Qureg): the ancillary qubits, length is n
        t(Qureg): the ancillary qubits, length is 1
    """

    n = len(qubit_N)

    for i in range(n):
        CControlSet(control, x[n - 1 - i], qubit_a, a)
        AdderMod(N, qubit_a, b, c, overflow, qubit_N, t)
        CControlSet(control, x[n - 1 - i], qubit_a, a)
        a = (a * 2) % N

    X | control
    for i in range(n):
        CCX | (control, x[i], b[i])
    X | control


def ReverseControlMulMod(a, N, control, x, qubit_a, b, c, overflow, qubit_N, t):
    """ Reverse of ControlMulMod

    Args:
        a(int): the parameter a
        N(int): the parameter N
        control(Qureg): the control qureg to store the result, length is 1
        x(Qureg): the qureg stores x, length is m
        qubit_a(Qureg): the ancillary qubits, length is n
        b(Qureg): length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1
        qubit_N(Qureg): the ancillary qubits, length is n
        t(Qureg): the ancillary qubits, length is 1
    """
    n = len(qubit_N)

    a_list = []
    for i in range(n):
        a_list.append(a)
        a = a * 2 % N

    X | control
    for i in range(n):
        CCX | (control, x[i], b[i])
    X | control

    for i in range(n):
        CControlSet(control, x[i], qubit_a, a_list[n - 1 - i])
        ReverseAdderMod(N, qubit_a, b, c, overflow, qubit_N, t)
        CControlSet(control, x[i], qubit_a, a_list[n - 1 - i])


def ExpMod(a, N, x, result, qubit_a, b, c, overflow, qubit_N, t):
    """ store a^x mod N in result

    Args:
        a(int): the parameter a
        N(int): the parameter N
        x(Qureg): the qureg stores x, length is m
        result(Qureg): the qureg to store the result
        qubit_a(Qureg): the ancillary qubits, length is n
        b(Qureg): the ancillary qubits, length is n
        c(Qureg): the ancillary qubits, length is n
        overflow(Qureg): the ancillary qubits, length is 1
        qubit_N(Qureg): the ancillary qubits, length is n
        t(Qureg): the ancillary qubits, length is 1
    """
    m = len(x)
    n = len(qubit_N)
    a_inv = Inverse(a, N)

    for i in range(m):
        ControlMulMod(a, N, x[m - 1 - i], result,
                      qubit_a, b, c, overflow, qubit_N, t)
        for j in range(n):
            Swap | (result[j], b[j])
        ReverseControlMulMod(
            a_inv, N, x[m - 1 - i], result, qubit_a, b, c, overflow, qubit_N, t)
        a = (a ** 2) % N
        a_inv = (a_inv ** 2) % N


class VBEAdder(object):
    @staticmethod
    def execute(n):
        """ a circuit calculate a+b, a and b are gotten from some qubits.

        (a,b,c=0,overflow) -> (a,b'=a+b,c=0,overflow')

        Quregs:
            a: the qureg stores a, length is n,
            b: the qureg stores b, length is n,
            c: the clean ancillary qubits, length is n,
            overflow: the dirty ancillary qubits, length is 1,
                            flips when overflows.

        Quantum Networks for Elementary Arithmetic Operations
        http://arxiv.org/abs/quant-ph/9511018v1
        """

        circuit = Circuit(3 * n + 1)
        qubit_a = circuit([i for i in range(n)])
        qubit_b = circuit([i for i in range(n, 2 * n)])
        qubit_c = circuit([i for i in range(2 * n, 3 * n)])
        qubit_overflow = circuit(3 * n)

        PlainAdder(qubit_a, qubit_b, qubit_c, qubit_overflow)

        return CompositeGate(gates=circuit.gates)


class VBEAdderMod(object):
    @staticmethod
    def execute(N, n):
        """ a circuit calculate (a+b) mod N.
        N are inherently designed in the circuit.

        (a,b,c=0,overflow=0,t=0,N) -> (a,b'=(a+b)%N,c=0,overflow=0,t=0,N)

        Quregs:
            a: the qureg stores a, length is n,
            b: the qureg stores b, length is n,
            c: the clean ancillary qubits, length is n,
            overflow: the clean ancillary qubits, length is 1,
            t: the clean ancillary qubits, length is 1.
            N: the qureg stores N, length is n,

        Quantum Networks for Elementary Arithmetic Operations
        http://arxiv.org/abs/quant-ph/9511018v1
        """

        circuit = Circuit(4 * n + 2)
        qubit_a = circuit([i for i in range(n)])
        qubit_b = circuit([i for i in range(n, 2 * n)])
        qubit_c = circuit([i for i in range(2 * n, 3 * n)])
        qubit_N = circuit([i for i in range(3 * n, 4 * n)])
        qubit_overflow = circuit(4 * n)
        qubit_t = circuit(4 * n + 1)

        AdderMod(N, qubit_a, qubit_b, qubit_c,
                 qubit_overflow, qubit_N, qubit_t)

        return CompositeGate(gates=circuit.gates)


class VBEMulAddMod(object):
    @staticmethod
    def execute(a, N, n, m):
        """ a circuit calculate b + x*a mod N.
        x are gotten from some qubits, a and N are inherently designed in the circuit.

        (x,b,qubit_a=0,c=0,overflow=0,qubit_N=0,t=0) ->
        (x,b'=b+a*x mod N,qubit_a,c,overflow,qubit_N,t)

        Quregs:
            x: the qureg stores x, length is m,
            b: the qureg stores b, length is n,
            qubit_a: the clean ancillary qubits, length is n,
            c: the clean ancillary qubits, length is n,
            overflow: the clean ancillary qubit, length is 1,
            qubit_N: the clean ancillary qubits, length is n,
            t: the clean ancillary qubit, length is 1.

        Quantum Networks for Elementary Arithmetic Operations
        http://arxiv.org/abs/quant-ph/9511018v1
        """

        circuit = Circuit(4 * n + m + 2)
        qubit_x = circuit([i for i in range(m)])
        qubit_a = circuit([i for i in range(m, n + m)])
        qubit_b = circuit([i for i in range(n + m, 2 * n + m)])
        qubit_c = circuit([i for i in range(2 * n + m, 3 * n + m)])
        qubit_overflow = circuit(3 * n + m)
        qubit_N = circuit([i for i in range(3 * n + m + 1, 4 * n + m + 1)])
        qubit_t = circuit(4 * n + m + 1)

        MulAddMod(a, N, qubit_x, qubit_a, qubit_b, qubit_c,
                  qubit_overflow, qubit_N, qubit_t)

        return CompositeGate(gates=circuit.gates)


class VBEExpMod(object):
    @staticmethod
    def execute(a, N, n, m):
        """ give parameters to the VBE
        Args:
            n(int): number of qubits of N
            m(int): number of qubits of x
            a(int): a
            N(int): N
        Returns:
            CompositeGate: the model filled by parameters.
        """
        if N <= 2:
            raise Exception("modulus should be great than 2")
        if gcd(a, N) != 1:
            raise Exception("a and N should be co-prime")
        # n = int(floor(log2(N))) + 1

        circuit = Circuit(m + 5 * n + 2)
        qubit_x = circuit([i for i in range(m)])
        qubit_r = circuit([i for i in range(m, m + n)])
        qubit_a = circuit([i for i in range(m + n, m + 2 * n)])
        qubit_b = circuit([i for i in range(m + 2 * n, m + 3 * n)])
        qubit_c = circuit([i for i in range(m + 3 * n, m + 4 * n)])

        overflow = circuit(m + 4 * n)
        qubit_N = circuit([i for i in range(m + 4 * n + 1, m + 5 * n + 1)])
        t = circuit(m + 5 * n + 1)
        X | qubit_r[n - 1]
        ExpMod(a, N, qubit_x, qubit_r, qubit_a,
               qubit_b, qubit_c, overflow, qubit_N, t)
        return CompositeGate(gates=circuit.gates)
