#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/4/3 13:12
# @Author  : Li Haomin
# @File    : hrs.py

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.algorithm.quantum_algorithm.shor.utility import int2bitwise, mod_reverse


def var_controlled_X(gate_set, controls, target):
    """0 to 2 controlled-X

    Args:
        controls (list): indices of control qubits
        target (int): target
    """
    n_control = len(controls)
    with gate_set:
        if n_control == 0:
            X & target
        elif n_control == 1:
            CX & [controls[0], target]
        elif n_control == 2:
            CCX.build_gate() & [controls[0], controls[1], target]
        else:
            raise ValueError()


def carry(gate_set, control, a, c_bitwise, g_aug, overflow):
    """
    Compute the overflow of a(quantum)+c(classical) with borrowed qubits g_aug.
    at most 2 control bits can be used

    Args:
        control(list): indices of 0 to 2 qubits.
        a(list): n qubits.
        g_aug(list): indices of n-1 qubits(more bits are OK).
        overflow(int): index of 1 qubit.
        c_bitwise(char array): n bits '0'-'1' array, representing binary int c.
    """
    n = len(a)
    n_control = len(control)
    g = g_aug[0:n - 1]
    # n==1, no borrowed bits g
    with gate_set:
        if n == 1:
            if c_bitwise[0] == "1":
                if n_control == 0:
                    CX & [a[0], overflow]
                elif n_control == 1:
                    CCX.build_gate() & [control[0], a[0], overflow]
                elif n_control == 2:
                    # CCCX | (c[0],c[1],a[0],overflow) with g_aug[0] as ancilla
                    CCX.build_gate() & [a[0], g_aug[0], overflow]
                    CCX.build_gate() & [control[0], control[1], g_aug[0]]
                    CCX.build_gate() & [a[0], g_aug[0], overflow]
                    CCX.build_gate() & [control[0], control[1], g_aug[0]]
                else:
                    raise ValueError()
            return
        # n>=2
        if n_control == 0:
            CX & [g[0], overflow]
        elif n_control == 1:
            CCX.build_gate() & [control[0], g[0], overflow]
        elif n_control == 2:
            # CCCX | (c1,c2,g[0],overflow) with a[0] as ancilla
            CCX.build_gate() & [g[0], a[0], overflow]
            CCX.build_gate() & [control[0], control[1], a[0]]
            CCX.build_gate() & [g[0], a[0], overflow]
            CCX.build_gate() & [control[0], control[1], a[0]]
        else:
            raise ValueError()

        for i in range(n - 2):
            if c_bitwise[i] == "1":
                CX & [a[i], g[i]]
                X & a[i]
            CCX.build_gate() & [g[i + 1], a[i], g[i]]
        if c_bitwise[n - 2] == "1":
            CX & [a[n - 2], g[n - 2]]
            X & a[n - 2]
        if c_bitwise[n - 1] == "1":
            CCX.build_gate() & [a[n - 1], a[n - 2], g[n - 2]]
        for i in range(n - 2):
            CCX.build_gate() & [g[n - 2 - i], a[n - 3 - i], g[n - 3 - i]]

        if n_control == 0:
            CX & [g[0], overflow]
        elif n_control == 1:
            CCX.build_gate() & [control[0], g[0], overflow]
        elif n_control == 2:
            # CCCX | (c1,c2,g[0],overflow) with a[0] as ancilla
            CCX.build_gate() & [g[0], a[0], overflow]
            CCX.build_gate() & [control[0], control[1], a[0]]
            CCX.build_gate() & [g[0], a[0], overflow]
            CCX.build_gate() & [control[0], control[1], a[0]]
        else:
            raise ValueError()

        # uncomputation
        for i in range(n - 2):
            CCX.build_gate() & [g[i + 1], a[i], g[i]]
        if c_bitwise[n - 1] == "1":
            CCX.build_gate() & [a[n - 1], a[n - 2], g[n - 2]]
        if c_bitwise[n - 2] == "1":
            X & a[n - 2]
            CX & [a[n - 2], g[n - 2]]
        for i in range(n - 2):
            CCX.build_gate() & [g[n - 2 - i], a[n - 3 - i], g[n - 3 - i]]
            if c_bitwise[n - 3 - i] == "1":
                X & a[n - 3 - i]
                CX & [a[n - 3 - i], g[n - 3 - i]]


def sub_widget(gate_set, v, g):
    """
    sub_widget used in incrementer().

    Args:
        v(list): indices of n qubits.
        g(list): indices of n qubits(more qubits are OK).
    """
    n = len(v)
    if len(g) < n:
        print("When do Sub_Widget, no edequate ancilla qubit")
    with gate_set:
        for i in range(n - 1):
            CX & [g[n - 1 - i], v[n - 1 - i]]
            CX & [g[n - 2 - i], g[n - 1 - i]]
            CCX.build_gate() & [g[n - 1 - i], v[n - 1 - i], g[n - 2 - i]]
        CX & [g[0], v[0]]
        for i in range(n - 1):
            CCX.build_gate() & [g[i + 1], v[i + 1], g[i]]
            CX & [g[i], g[i + 1]]
            CX & [g[i], v[i + 1]]


def incrementer(gate_set, v, g):
    """
    Incremente v by 1, with borrowed qubits g.

    Args:
        v(list): indices of n qubits.
        g(list): indices of n qubits(more qubits are OK).
    """
    n = len(v)
    if len(g) < n:
        print("When do Increment, no edequate borrowed qubit")
    with gate_set:
        for i in range(n):
            CX & [g[n - 1], v[i]]
        for i in range(n - 1):
            X & g[i]
        X & v[0]
        sub_widget(gate_set, v, g)
        for i in range(n - 1):
            X & g[i]
        sub_widget(gate_set, v, g)
        for i in range(n):
            CX & [g[n - 1], v[i]]


def c_incrementer(gate_set, control, v, g_aug):
    """
    1-controlled incremente v by 1, with borrowed qubits g.

    Constructed by attaching the control qubit to the little-end of v,
    and apply an (n+1)-bit incrementer() to it.

    Args:
        control(int): index of 1 qubit.
        v(Qureg): indices of n qubits.
        g(Qureg): indices of n + 1 qubits(more qubits are OK).
    """
    n = len(v)
    m = len(g_aug)
    if m < n + 1:
        print("no edequate ancilla bits")
    g = g_aug[0:n + 1]
    vc = v + [control]
    with gate_set:
        incrementer(gate_set, vc, g)
        X & vc[n]


def adder_rec(gate_set, control, x, c_bitwise, ancilla, ancilla_g):
    """
    The recursively applied partial-circuit in adder().

    Controlled version constructed by changing carry() to c_carry().

    Args:
        control(list): indices of 0 or 1 qubit.
        x(Qureg): indices of n qubits.
        ancilla(Qubit): index of 1 qubit.
        ancilla_g(Qubit): index of 1 qubit,
            might be used as borrowed qubit in c_incrementer
            when x_H and x_L are of the same length.
        c_bitwise(char array): n bits '0'-'1' array, representing binary int c.
    """
    n = len(x)
    # n_control = len(control)
    if n == 1:
        return
    mid = n // 2
    x_H = x[0:mid]
    x_L = x[mid:n]
    c_H = c_bitwise[0:mid]
    c_L = c_bitwise[mid:n]
    g = x_L + [ancilla_g]
    with gate_set:
        c_incrementer(gate_set, ancilla, x_H, g)
        for i in range(mid):
            CX & [ancilla, x_H[i]]
        carry(gate_set, control, x_L, c_L, x_H, ancilla)
        c_incrementer(gate_set, ancilla, x_H, g)
        carry(gate_set, control, x_L, c_L, x_H, ancilla)
        for i in range(mid):
            CX & [ancilla, x_H[i]]
        adder_rec(gate_set, control, x_L, c_L, ancilla, ancilla_g)
        adder_rec(gate_set, control, x_H, c_H, ancilla, ancilla_g)


def adder(gate_set, control, x, c, ancilla, ancilla_g):
    """
    Compute x(quantum) + c(classical) with borrowed qubits, at most 1-controlled.

    Args:
        control(list): indices of 0 or 1 qubit.
        x(list): indices of n qubits.
        ancilla(int): index of 1 qubit, borrowed ancilla.
        ancilla_g(int): index of 1 qubit, borrowed ancilla.
        c(int): integer.
    """
    n = len(x)
    c_bitwise = int2bitwise(c, n)
    with gate_set:
        adder_rec(gate_set, control, x, c_bitwise, ancilla, ancilla_g)
        for i in range(n):
            if c_bitwise[i] == "1":
                var_controlled_X(gate_set, control, x[i])


def c_sub(gate_set, control, x, c, ancilla, ancilla_g):
    """
    Compute x(quantum) - c(classical) with borrowed qubits, 1-controlled.

    Constructed on the basis of c_adder() with complement technique.

    Args:
        control(Qubit): 1 qubit.
        x(Qureg): n qubits.
        ancilla(Qubit): 1 qubit, borrowed ancilla.
        ancilla_g(Qubit): 1 qubit, borrowed ancilla.
        c(int): integer.
    """
    n = len(x)
    c_complement = 2 ** n - c
    cc_bitwise = int2bitwise(c_complement, n)
    with gate_set:
        adder_rec(gate_set, [control], x, cc_bitwise, ancilla, ancilla_g)
        for i in range(n):
            if cc_bitwise[i] == "1":
                CX & [control, x[i]]


def compare(gate_set, control, b, c, g_aug, indicator):
    """
    compare b and c with borrowed qubits g_aug.
    The Indicator toggles if c > b, not if c <= b.
    at most 2-controlled.

    Constructed on the basis of carry().

    Args:
        control(list): 0 or 2 qubit.
        b(Qureg): n qubits.
        g_aug(Qureg): n-1 qubits(more qubits are OK).
        indicator(Qubit): 1 qubit.
        c(int): integer with less-than-n length.
    """
    n = len(b)
    m = len(g_aug)
    if m < n - 1:
        print("No edequate ancilla bits when compare\n")
        return
    c_bitwise = int2bitwise(c, n)
    with gate_set:
        for i in range(n):
            X & b[i]
        carry(gate_set, control, b, c_bitwise, g_aug, indicator)
        for i in range(n):
            X & b[i]


def adder_mod(gate_set, control, b, a, N, g, indicator):
    """
    Compute b(quantum) + a(classical) mod N(classical),
    with borrowed qubits g and ancilla qubit indicator, at most 2-controlled.

    Args：
        control(list): 0 or 2 qubit.
        b(Qreg): n qubits.
        g(Qureg): n-1 borrowed qubits(more qubits are OK).
        indicator(Qubit): 1 ancilla qubit.
        a(int): integer less than N.
        N(int): integer.

    Note that this circuit works only when n > 2.
    So for smaller numbers, use another design.
    """
    if len(b) <= 2:
        raise Exception("The numbers should be more than 2-length to use HRS circuits.")
    with gate_set:
        compare(gate_set, control, b, N - a, g, indicator)
        adder(gate_set, [indicator], b, a, g[0], g[1])
        var_controlled_X(gate_set, control, indicator)
        c_sub(gate_set, indicator, b, N - a, g[0], g[1])
        var_controlled_X(gate_set, control, indicator)
        compare(gate_set, control, b, a, g, indicator)
        var_controlled_X(gate_set, control, indicator)


def adder_mod_reversed(gate_set, control, b, a, N, g, indicator):
    """
    The reversed circuit of adder_mod()
    """
    adder_mod(gate_set, control, b, N - a, N, g, indicator)


def mul_mod_raw(gate_set, control, x, a, b, N, indicator):
    """
    Compute b(quantum) + x(quantum) * a(classical) mod N(classical),
    with target qubits b and ancilla qubit indicator.

    Args:
        control(Qubit): 0 or 1 qubit.
        x(Qureg): n qubits.
        b(Qureg): n qubits, target.
        indicator(Qubit): 1 ancilla qubit.
        a(int): integer.
        N(int): integer.

    Note that this circuit works only when n > 2.
    So for smaller numbers, use another design.
    """

    n = len(x)
    if n <= 2:
        raise Exception("The numbers should be more than 2-length to use HRS circuits.")
    a_list = []
    for i in range(n):
        a_list.append(a)
        a = (a * 2) % N
    with gate_set:
        for i in range(n):
            # borrow all the n-1 unused qubits in x
            g = x[:n - i - 1] + x[n - i:]
            if len(control) == 0:
                adder_mod(gate_set, [x[n - 1 - i]], b, a_list[i], N, g, indicator)
            elif len(control) == 1:
                adder_mod(
                    gate_set, control + [x[n - 1 - i]], b, a_list[i], N, g, indicator
                )


def mul_mod_raw_reversed(
    gate_set, control, x, a, b, N, indicator
):  # TODO: this can be done classically with `mul_mod_raw`
    """
    The reversed circuit of mul_mod_raw()
    Note that this circuit works only when n > 2.
    So for smaller numbers, use another design.
    """

    n = len(x)
    if n <= 2:
        raise Exception("The numbers should be more than 2-length to use HRS circuits.")
    a_list = []
    for i in range(n):
        a_list.append(a)
        a = a * 2 % N
    with gate_set:
        for i in range(n):
            g = x[:i] + x[i + 1:]
            if len(control) == 0:
                adder_mod(gate_set, [x[i]], b, N - a_list[n - i - 1], N, g, indicator)
            elif len(control) == 1:
                adder_mod(
                    gate_set,
                    control + [x[i]],
                    b,
                    N - a_list[n - i - 1],
                    N,
                    g,
                    indicator,
                )
            else:
                raise ValueError()


def mul_mod(gate_set, control, x, a, ancilla, N, indicator):
    """
    Compute x(quantum) * a(classical) mod N(classical), with ancilla qubits.

    Args:
        control(Qubit): 0 or 1 qubit.
        x(Qureg): n qubits.
        ancilla(Qureg): n qubits.
        indicator(Qubit): 1 qubit.
        a(int): integer.
        N(int): integer.

    Note that this circuit works only when n > 2.
    So for smaller numbers, use another design.
    """

    n = len(x)
    if n <= 2:
        raise Exception("The numbers should be more than 2-length to use HRS circuits.")
    a_r = mod_reverse(a, N)
    with gate_set:
        mul_mod_raw(gate_set, control, x, a, ancilla, N, indicator)
        # Swap
        for i in range(n):
            if len(control) == 0:
                Swap & [x[i], ancilla[i]]
            elif len(control) == 1:
                CSwap & [control[0], x[i], ancilla[i]]
            else:
                raise ValueError()
        mul_mod_raw_reversed(gate_set, control, x, a_r, ancilla, N, indicator)


class HRSAdder(object):
    @staticmethod
    def execute(n, c):
        """
        Compute x(quantum) + c(classical) with borrowed qubits.

        Args:
            n(int): length of numbers
            c(int): the constant added to the quantum number

        Quregs:
            x(Qureg): n qubits.
            ancilla(Qubit): 1 qubit, borrowed ancilla.
            ancilla_g(Qubit): 1 qubit, borrowed ancilla.
        """

        gate_set = CompositeGate()
        qubit_x = list(range(n))
        ancilla = n
        ancilla_g = n + 1

        adder(gate_set, [], qubit_x, c, ancilla, ancilla_g)

        return gate_set


class HRSAdderMod(object):
    @staticmethod
    def execute(n, a, N):
        """
        Compute b(quantum) + a(classical) mod N(classical),
        with borrowed qubits g and ancilla qubit indicator.

        Args:
            n(int): length of numbers
            a(int): the constant added to the quantum number
            N(int): the modulus

        Quregs：
            b(Qreg): n qubits.
            g(Qureg): n-1 borrowed qubits(more qubits are OK).
            indicator(Qubit): 1 ancilla qubit.

        Note that this circuit works only when n > 2.
        So for smaller numbers we use another design.
        """

        if n <= 2:
            raise Exception(
                "The numbers should be more than 2-length to use HRS circuits."
            )

        gate_set = CompositeGate()
        qubit_b = list(range(n))
        g = list(range(n, 2 * n - 1))
        indicator = 2 * n - 1

        adder_mod(gate_set, [], qubit_b, a, N, g, indicator)

        return gate_set


class HRSMulMod(object):
    @staticmethod
    def execute(n, a, N):
        """
        Compute x(quantum) * a(classical) mod N(classical), with ancilla qubits.

        Args:
            n(int): length of numbers
            a(int): the constant multiplied to the quantum number
            N(int): the modulus

        Quregs:
            x(Qureg): n qubits.
            ancilla(Qureg): n qubits.
            indicator(Qubit): 1 qubit.

        Note that this circuit works only when n > 2.
        So for smaller numbers we use another design.
        """

        if n <= 2:
            raise Exception(
                "The numbers should be more than 2-length to use HRS circuits."
            )

        gate_set = CompositeGate()
        qubit_x = list(range(n))
        ancilla = list(range(n, 2 * n))
        indicator = 2 * n

        mul_mod(gate_set, [], qubit_x, a, ancilla, N, indicator)

        return gate_set


class CHRSMulMod(object):
    @staticmethod
    def execute(n, a, N):
        """
        Compute x(quantum) * a(classical) mod N(classical), with ancilla qubits, 1-controlled.

        Args:
            n(int): length of numbers
            a(int): the constant multiplied to the quantum number
            N(int): the modulus

        Quregs:
            control(Qubit): 1 qubit.
            x(Qureg): n qubits.
            ancilla(Qureg): n qubits.
            indicator(Qubit): 1 qubit.

        Note that this circuit works only when n > 2.
        So for smaller numbers we use another design.
        """
        if n <= 2:
            raise Exception(
                "The numbers should be more than 2-length to use HRS circuits."
            )

        gate_set = CompositeGate()
        qubit_x = list(range(n))
        ancilla = list(range(n, 2 * n))
        indicator = 2 * n
        control = 2 * n + 1

        mul_mod(gate_set, [control], qubit_x, a, ancilla, N, indicator)

        return gate_set
