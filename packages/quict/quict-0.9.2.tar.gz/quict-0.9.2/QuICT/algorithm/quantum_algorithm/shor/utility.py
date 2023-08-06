import numpy as np

from functools import reduce
from math import gcd
from QuICT.core.gate import X
from QuICT.simulation.state_vector import CircuitSimulator

from QuICT.tools import Logger
from QuICT.tools.exception.core import *

logger = Logger("Shor-util")


def ex_gcd(a, b, arr):
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = ex_gcd(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g


def mod_reverse(a, n):
    arr = [0, 1]
    g = ex_gcd(a, n, arr)
    if g != 1:
        raise ValueError(f"imput {a} and {n} does not coprime")
    return (arr[0] % n + n) % n


def fast_power(a, b, N):
    x = 1
    now_a = a
    while b > 0:
        if b % 2 == 1:
            x = x * now_a % N
        now_a = now_a * now_a % N
        b >>= 1
    return x


# transform an integer to n-length bitwise string


def int2bitwise(c, n):
    """
    Transform an integer c to binary n-length bitwise string.
    """
    c_bitwise = bin(c)[2:]
    if len(c_bitwise) > n:
        c_bitwise = c_bitwise[-n:]
        # print('c exceeds the length of a, thus is truncated')
    else:
        c_bitwise = "0" * (n - len(c_bitwise)) + c_bitwise
    return c_bitwise


def set(qreg, N):
    """
    Set the qreg as N, using X gates on specific qubits.
    """
    str = bin(N)[2:]
    n = len(qreg)
    m = len(str)
    if m > n:
        logger.warning(
            f"When set qureg as N={N}, N exceeds the length of qureg n={n}, thus is truncated"
        )

    for i in range(min(n, m)):
        if str[m - 1 - i] == "1":
            X | qreg[n - 1 - i]


def split_invert(n, d, CFE):
    CFE.append(n // d)
    n = n % d
    if n == 1:
        CFE.append(d)
        return
    split_invert(d, n, CFE)


def continued_fraction_expansion(n, d):
    """
    Calculate the continued fraction expansion of a rational number n/d.

    Args:
        n: numerator.
        d: denominator.
    """
    CFE = []
    split_invert(n, d, CFE)
    return CFE


def miller_rabin(num):
    """random prime test
        return True, num is a prime whp
        return False, num is a composite
    """
    Test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if num == 1:
        return False
    t = num - 1
    k = 0
    while (t & 1) == 0:
        k += 1
        t >>= 1
    for test_num in Test:
        # test_num should be generated randomly
        if num == test_num:
            return True
        a = fast_power(test_num, t, num)
        nxt = a
        for _ in range(k):
            nxt = (a * a) % num
            if nxt == 1 and a != 1 and a != num - 1:
                return 0
            a = nxt
        if a != 1:
            return False
    return True


MAX_ROUND = 2


def reinforced_order_finding_constructor(order_finding):
    def reinforced_order_finding(a: int, N: int, eps: float = 1 / 10, simulator=None):
        r_list = []
        i = 0
        while i < MAX_ROUND:
            i += 1
            r = order_finding(a, N, eps, simulator)
            if r != 0 and (a ** r) % N == 1:
                logger.info("\tsuccess!")
                r_list.append(r)
        if len(r_list) == 0:
            return 0
        else:
            return reduce(lambda x, y: (x * y) // gcd(x, y), r_list)

    return reinforced_order_finding


def run_twice_order_finding_constructor(order_finding):
    def run(
        a: int,
        N: int,
        demo: str = None,
        eps: float = 1 / 10,
        simulator=CircuitSimulator(),
    ):
        r1 = order_finding(a, N, eps, simulator)
        r2 = order_finding(a, N, eps, simulator)
        flag1 = pow(a, r1, N) == 1 and r1 != 0
        flag2 = pow(a, r2, N) == 1 and r2 != 0
        if flag1 and flag2:
            r = min(r1, r2)
        elif not flag1 and not flag2:
            r = int(np.lcm(r1, r2))
        else:
            r = int(flag1) * r1 + int(flag2) * r2

        if pow(a, r, N) == 1 and r != 0:
            msg = f"\torder_finding found candidate order: r = {r} of a = {a}"
        else:
            r = 0
            msg = "\torder_finding failed"
        logger.info(msg)
        return r

    return run
