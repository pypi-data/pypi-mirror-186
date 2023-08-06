import numpy as np

from QuICT.core.gate import CompositeGate, CX, CCX, CSwap, X, QFT, IQFT, CU1, U1, CCRz, Phase


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
        raise ValueError("not coprime")
    return (arr[0] % n + n) % n


def draper_adder(gate_set, a, b):
    """ store a + b in b

    (a,b) -> (a,b'=a+b)


    Args:
        gate_set(CompositeGate):
        a(list): the list of indices of qureg stores a, length is n
        b(list): the list of indices of qureg stores b, length is n

    """
    n = len(a)
    with gate_set:
        QFT.build_gate(n) & b
        for i in range(n):
            p = 0
            for j in range(i, n):
                p += 1
                CU1(2 * np.pi / (1 << p)) & [a[j], b[i]]
        IQFT.build_gate(n) & b


def fourier_adder_wired(gate_set, a, phib):
    """ store Φ(a + b) in phib, but a is wired

    (phib) -> (phib'=Φ(a + b))

    Args:
        a(int):      unsigned integer, low n bits used
        phib(Qureg): the qureg stores Φ(b), length is n+1

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    n = len(phib) - 1
    a = a & ~(1 << n)  # clear (n+1)-th bit to zero
    with gate_set:
        for i in range(n + 1):
            p = 0
            for j in range(i, n + 1):
                p += 1
                if a & (1 << (n - j)) != 0:
                    U1(2 * np.pi / (1 << p)) & phib[i]


def fourier_adder_wired_reversed(gate_set, a, phib):
    """ store Φ(b - a) or Φ(b - a + 2**(n+1)) in phib, but a is wired

    (phib) -> (phib')

    Args:
        a(int):      unsigned integer, low n bits used
        phib(Qureg): the qureg stores Φ(b), length is n+1

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    n = len(phib) - 1
    a = a & ~(1 << n)  # clear (n+1)-th bit to zero
    with gate_set:
        for i in reversed(range(n + 1)):
            p = n + 1 - i
            for j in reversed(range(i, n + 1)):
                if a & (1 << (n - j)) != 0:
                    U1(- 2 * np.pi / (1 << p)) & phib[i]
                p -= 1


def cc_fourier_adder_wired(gate_set, a, phib, c, dualControlled):
    """ fourier_adder_wired with 1 or 2 control bits

    (phib,c) -> (phib'=Φ(a + b),c)

    Args:
        a(int):      unsigned integer, low n bits used
        phib(Qureg): the qureg stores Φ(b), length is n
        c(Qureg):    the control qubits,    length is 2 or 1, see dualControlled
        dualControlled(bool): if True, c[0] will be used; else c[0:2] will be used

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    if type(c) == int:
        c = [c]
    n = len(phib) - 1
    a = a & ~(1 << n)  # clear (n+1)-th bit to zero
    with gate_set:
        for i in range(n + 1):
            p = 0
            for j in range(i, n + 1):
                p += 1
                if a & (1 << (n - j)) != 0:
                    phase = 2 * np.pi / (1 << p)
                    # CCU1(2 * np.pi / (1 << p)) | (c[0],c[1],phib[i])
                    if dualControlled:
                        CU1(phase / 2) & [c[1], phib[i]]
                        CX & [c[0], c[1]]
                        CU1(- phase / 2) & [c[1], phib[i]]
                        CX & [c[0], c[1]]
                        CU1(phase / 2) & [c[0], phib[i]]
                    else:
                        CU1(phase) & [c[0], phib[i]]


def cc_fourier_adder_wired_reversed(gate_set, a, phib, c, dualControlled):
    """ fourier_adder_wired_reversed with 1 or 2 control bits

    (phib,c) -> (phib',c)

    Args:
        a(int):      unsigned integer, low n bits used
        phib(Qureg): the qureg stores Φ(b), length is n+1
        c(Qureg):    the control qubits,    length is 2 or 1, see dualControlled
        dualControlled(bool): default True. if True, c[0] will be used; else c[0:1] will be used

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    if type(c) == int:
        c = [c]
    n = len(phib) - 1
    a = a & ~(1 << n)  # clear (n+1)-th bit to zero
    with gate_set:
        for i in reversed(range(n + 1)):
            p = n + 1 - i
            for j in reversed(range(i, n + 1)):
                if a & (1 << (n - j)) != 0:
                    phase = 2 * np.pi / (1 << p)
                    # CCU1(2 * np.pi / (1 << p)) | (c[0],c[1],phib[i])
                    if dualControlled:
                        CU1(- phase / 2) & [c[0], phib[i]]
                        CX & [c[0], c[1]]
                        CU1(phase / 2) & [c[1], phib[i]]
                        CX & [c[0], c[1]]
                        CU1(- phase / 2) & [c[1], phib[i]]
                    else:
                        CU1(- phase) & [c[0], phib[i]]
                p -= 1


def cc_fourier_adder_mod(gate_set, a, N, phib, c, low, dualControlled=True):
    """ use fourier_adder_wired/cc_fourier_adder_wired to calculate (a+b)%N in Fourier space

    (phib=Φ(b),c,low) -> (phib'=Φ((a+b)%N),c,low)


    Args:
        a(int):      low n bits used as unsigned
        N(int):      low n bits used as unsigned
        phib(Qureg): the qureg stores b,        length is n+1,
        c(Qureg):    the control qubits,    length is 2 or 1, see dualControlled
        low(Qureg):  the clean ancillary qubit, length is 1,
        dualControlled(bool): if True, c[0] will be used; else c[0:1] will be used

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    cc_fourier_adder_wired(gate_set, a, phib, c, dualControlled=dualControlled)
    fourier_adder_wired_reversed(gate_set, N, phib)
    with gate_set:
        IQFT.build_gate(len(phib)) & phib
        CX & [phib[0], low[0]]
        QFT.build_gate(len(phib)) & phib
    cc_fourier_adder_wired(gate_set, N, phib, low, dualControlled=False)
    cc_fourier_adder_wired_reversed(
        gate_set, a, phib, c, dualControlled=dualControlled)
    with gate_set:
        IQFT.build_gate(len(phib)) & phib
        X & phib[0]
        CX & [phib[0], low[0]]
        X & phib[0]
        QFT.build_gate(len(phib)) & phib
    cc_fourier_adder_wired(gate_set, a, phib, c, dualControlled=dualControlled)


def fourier_adder_mod(gate_set, a, N, phib, low):
    """ use fourier_adder_wired/cc_fourier_adder_wired
    to calculate (a+b)%N in Fourier space. no control bits.

    (phib=Φ(b),low) -> (phib'=Φ((a+b)%N),low)

    Args:
        a(int):      low n bits used as unsigned
        N(int):      low n bits used as unsigned
        phib(Qureg): the qureg stores b,        length is n+1,
        low(Qureg):  the clean ancillary qubit, length is 1,

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """
    fourier_adder_wired(gate_set, a, phib)
    fourier_adder_wired_reversed(gate_set, N, phib)
    with gate_set:
        IQFT.build_gate(len(phib)) & phib
        CX & [phib[0], low[0]]
        QFT.build_gate(len(phib)) & phib
    cc_fourier_adder_wired(gate_set, N, phib, low, dualControlled=False)
    fourier_adder_wired_reversed(gate_set, a, phib)
    with gate_set:
        IQFT.build_gate(len(phib)) & phib
        X & phib[0]
        CX & [phib[0], low[0]]
        X & phib[0]
        QFT.build_gate(len(phib)) & phib
    fourier_adder_wired(gate_set, a, phib)


def c_fourier_mult_mod(gate_set, a, N, x, phib, c, low):
    """ use cc_fourier_adder_mod to calculate (b+ax)%N in Fourier space

    (phib=Φ(b),x,c,low) -> (phib'=Φ((b+ax)%N),x,c,low)

    Args:
        a(int):      low n bits used as unsigned
        N(int):      low n bits used as unsigned
        x(Qureg):    the qureg stores x,        length is n,
        phib(Qureg): the qureg stores b,        length is n+1,
        c(int):      the control qubits,        length is 1,
        low(int):    the clean ancillary qubit, length is 1,

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """

    n = len(phib) - 1
    p = 1
    for i in range(n - 1, -1, -1):
        cc_fourier_adder_mod(gate_set, p * a % N, N, phib,
                             (c[0], x[i]), low)  # p * a % N
        p = p * 2


def fourier_mult_mod(gate_set, a, N, x, phib, low):
    """ use fourier_adder_mod to calculate (b+ax)%N in Fourier space

    (phib=Φ(b),x,low) -> (phib'=Φ((b+ax)%N),x,low)

    Args:
        a(int):      low n bits used as unsigned
        N(int):      low n bits used as unsigned
        x(Qureg):    the qureg stores x,        length is n,
        phib(Qureg): the qureg stores b,        length is n+1,
        low(Qureg):  the clean ancillary qubit, length is 1,

    Circuit for Shor's algorithm using 2n+3 qubits
    http://arxiv.org/abs/quant-ph/0205095v3
    """

    n = len(phib) - 1
    p = 1
    for i in range(n - 1, -1, -1):
        cc_fourier_adder_mod(gate_set, p * a % N, N, phib,
                             x[i], low, dualControlled=False)  # p * a % N
        p = p * 2


def c_mult_mod(gate_set, a, N, x, b, c, low):
    with gate_set:
        QFT.build_gate(len(b)) & b
        c_fourier_mult_mod(gate_set, a, N, x, b, c, low)
        IQFT.build_gate(len(b)) & b


class BEAAdder(object):
    @staticmethod
    def execute(n):
        """ a circuit calculate a+b, a and b are gotten from some qubits.

        (a,b) -> (a,b'=a+b)

        Args:
            n(int): length of a and b
        """

        gate_set = CompositeGate()
        qreg_a = list(range(n))
        qreg_b = list(range(n, n * 2))
        draper_adder(gate_set, qreg_a, qreg_b)
        return gate_set


class BEAAdderWired(object):
    @staticmethod
    def execute(n, a):
        """ a circuit calculate a+b, a is wired, and b are gotten from some qubits.

        (b) -> (b'=a+b)

        Args:
            n(int): length of a. b is in length n+1
            a(int): the operand to be added. low n bits used
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            fourier_adder_wired(gate_set, a, qreg_b)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class BEAReverseAdderWired(object):
    @staticmethod
    def execute(n, a):
        """
        (b) -> (b'=b-a or b-a+2**(n+1))

        Args:
            n(int): length of a. b is in length n+1
            a(int): the operand to be subtracted. low n bits used
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            fourier_adder_wired_reversed(gate_set, a, qreg_b)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class CCBEAAdderWired(object):
    @staticmethod
    def execute(n, a):
        """
        (b,c) -> (b'=a+b,c) if c=0b11 else (b'=b,c)

        Args:
            n(int): length of a. b is in length n+1
            a(int): the operand to be subtracted. low n bits used
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_c = list(range(n + 1, n + 3))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            cc_fourier_adder_wired(gate_set, a, qreg_b,
                                   qreg_c, dualControlled=True)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class CCBEAReverseAdderWired(object):
    @staticmethod
    def execute(n, a):
        """
        (b,c) -> (b'=b-a,c) if c=0b11 else (b'=b,c)

        Args:
            n(int): length of a. b is in length n+1
            a(int): the operand to be subtracted. low n bits used
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_c = list(range(n + 1, n + 3))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            cc_fourier_adder_wired_reversed(
                gate_set, a, qreg_b, qreg_c, dualControlled=True)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class CCBEAAdderMod(object):
    @staticmethod
    def execute(n, a, N):
        """ use fourier_adder_wired/cc_fourier_adder_wired to calculate (a+b)%N in Fourier space

        (phib=Φ(b),c,low) -> (phib'=Φ((a+b)%N),c,low) if c=0b11 else (phib'==Φ(b),c,low)

        Args:
            n(int):      bits len
            a(int):      least n bits used as unsigned
            N(int):      least n bits used as unsigned

        Quregs:
            phib(Qureg): the qureg stores b,        length is n+1,
            c(Qureg):    the control qubits,        length is 2,
            low(Qureg):  the clean ancillary qubit, length is 1,

        Circuit for Shor's algorithm using 2n+3 qubits
        http://arxiv.org/abs/quant-ph/0205095v3
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_c = list(range(n + 1, n + 3))
        qreg_low = list(range(n + 3, n + 4))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            cc_fourier_adder_mod(gate_set, a, N, qreg_b, qreg_c, qreg_low)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class BEAAdderMod(object):
    @staticmethod
    def execute(n, a, N):
        """ use fourier_adder_wired/cc_fourier_adder_wired
        to calculate (a+b)%N in Fourier space. No cotrol bits

        (phib=Φ(b),low) -> (phib'=Φ((a+b)%N),low)

        Args:
            n(int):      bits len
            a(int):      least n bits used as unsigned
            N(int):      least n bits used as unsigned

        Quregs:
            phib(Qureg): the qureg stores b,        length is n+1,
            low(Qureg):  the clean ancillary qubit, length is 1,

        Circuit for Shor's algorithm using 2n+3 qubits
        http://arxiv.org/abs/quant-ph/0205095v3
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_low = list(range(n + 1, n + 2))
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            fourier_adder_mod(gate_set, a, N, qreg_b, qreg_low)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class CBEAMulMod(object):
    @staticmethod
    def execute(n, a, N):
        """ use cc_fourier_adder_mod to calculate (b+ax)%N in Fourier space

        (phib=Φ(b),x,c,low) -> (phib'=Φ((b+ax)%N),x,c,low) if c=0b1 else (phib'=Φ(b),x,c,low)

        Args:
            n(int):      bits len
            a(int):      least n bits used as unsigned
            N(int):      least n bits used as unsigned

        Quregs:
            phib(Qureg): the qureg stores b,        length is n+1,
            x(Qureg):    the qureg stores x,        length is n,
            c(Qureg):    the control qubits,        length is 1,
            low(Qureg):  the clean ancillary qubit, length is 1,

        Circuit for Shor's algorithm using 2n+3 qubits
        http://arxiv.org/abs/quant-ph/0205095v3
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_x = list(range(n + 1, 2 * n + 1))
        qreg_c = [2 * n + 1]
        qreg_low = [2 * n + 2]
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            c_fourier_mult_mod(gate_set, a, N, qreg_x,
                               qreg_b, qreg_c, qreg_low)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class BEAMulMod(object):
    @staticmethod
    def execute(n, a, N):
        """ use fourier_adder_mod to calculate (b+ax)%N in Fourier space. No control bits

        (phib=Φ(b),x,low) -> (phib'=Φ((b+ax)%N),x,low)


        Args:
            n(int):      bits len
            a(int):      least n bits used as unsigned
            N(int):      least n bits used as unsigned

        Quregs:
            phib(Qureg): the qureg stores b,        length is n+1,
            x(Qureg):    the qureg stores x,        length is n,
            low(Qureg):  the clean ancillary qubit, length is 1,

        Circuit for Shor's algorithm using 2n+3 qubits
        http://arxiv.org/abs/quant-ph/0205095v3
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_x = list(range(n + 1, 2 * n + 1))
        qreg_low = [2 * n + 1]
        with gate_set:
            QFT.build_gate(len(qreg_b)) & qreg_b
            fourier_mult_mod(gate_set, a, N, qreg_x, qreg_b, qreg_low)
            IQFT.build_gate(len(qreg_b)) & qreg_b
        return gate_set


class BEACUa(object):
    @staticmethod
    def execute(n, a, N):
        """ Controlled-U_a, ((a*x)MOD(N)) if c=1, else (x)

        (b=0,x,c,low) -> (b=0,x',c,low)

        Args:
            n(int):      bits len
            a(int):      least n bits used as unsigned
            N(int):      least n bits used as unsigned

        Quregs:
            phib(Qureg): the qureg stores b,        length is n+1,
            x(Qureg):    the qureg stores x,        length is n,
            c(Qureg):    the qureg stores c,        length is 1,
            low(Qureg):  the clean ancillary qubit, length is 1,

        Circuit for Shor's algorithm using 2n+3 qubits
        http://arxiv.org/abs/quant-ph/0205095v3
        """

        gate_set = CompositeGate()
        qreg_b = list(range(n + 1))
        qreg_x = list(range(n + 1, 2 * n + 1))
        qreg_c = [2 * n + 1]
        qreg_low = [2 * n + 2]

        with gate_set:
            gate_set: CompositeGate
            c_mult_mod(gate_set, a, N, qreg_x, qreg_b, qreg_c, qreg_low)
            for i in range(n):  # n bits swapped, b[0] always 0
                CSwap & [qreg_c[0], qreg_x[i], qreg_b[i + 1]]
            # Reverse c_mult_mod(a_inv,N,x,b,c,low)
            c_mult_mod(gate_set, N - mod_reverse(a, N), N, qreg_x, qreg_b, qreg_c, qreg_low)

        return gate_set
