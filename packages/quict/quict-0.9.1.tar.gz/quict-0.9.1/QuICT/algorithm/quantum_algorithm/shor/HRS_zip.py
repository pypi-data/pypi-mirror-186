# Author  : Zhu Qinlin

"""
The (2n+2)-qubit circuit used in the Shor algorithm is designed \
by THOMAS HANER, MARTIN ROETTELER, and KRYSTA M. SVORE in \
"Factoring using 2n+2 qubits with Toffoli based modular multiplication"
"""

from fractions import Fraction
from math import pi
import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.qcda.synthesis.arithmetic.hrs import *
from QuICT.simulation.state_vector import CircuitSimulator
from QuICT.core.operator import Trigger, CheckPoint
from .utility import *

from QuICT.tools import Logger
from QuICT.tools.exception.core import *

logger = Logger("HRS-zip")


def construct_circuit(a: int, N: int, eps: float = 1 / 10):
    # phase estimation procedure
    n = int(np.ceil(np.log2(N + 1)))
    t = int(2 * n + 1 + np.ceil(np.log(2 + 1 / (2 * eps))))
    logger.info(f"\tcircuit construction begin: circuit: n = {n} t = {t}")

    circuit = Circuit(2 * n + 2)
    x_reg = list(range(n))
    trickbit = [2 * n + 1]

    # cgates[measured qubit index][added gate index][measured result]
    cgates = [
        [[CompositeGate() for measured in range(2)] for j in range(t + 1)]
        for i in range(t)
    ]
    # triggers[measured qubit index][added gate index]
    triggers = [
        [
            Trigger(1, [cgates[i][j][measured] for measured in range(2)])
            for j in range(t + 1)
        ]
        for i in range(t)
    ]
    triggers_reset = list(range(t))
    # checkpoints[measured qubit index]
    checkpoints = [CheckPoint() for i in range(t)]

    # triggers!!!
    for k in range(t):  # end at k-th checkpoints
        for i in range(k):  # start at i-th qubits (compressed)
            cpc = checkpoints[k].get_child()
            Rz(-np.pi / (1 << (k - i))) | cgates[i][k - 1 - i][1](trickbit)
            cpc | cgates[i][k - 1 - i][1]
    # triggers for reset!!!
    for i in range(t):
        cgate = CompositeGate()
        X | cgate(trickbit)
        triggers_reset[i] = Trigger(1, [CompositeGate(), cgate])

    # subcircuit: init \ket{1}\ket{0}
    X | circuit(x_reg[n - 1])

    history_indices = []
    ptr = 0
    for k in range(t):
        # subcircuit CUa
        H | circuit(trickbit)
        gate_pow = pow(a, 1 << (t - 1 - k), N)
        CHRSMulMod.execute(n, gate_pow, N) | circuit
        # subcircuit: semi-classical QFT
        checkpoints[k] | circuit
        H | circuit(trickbit)
        # subcircuit: measure & reset trickbit
        for i in range(t - k):
            if i == 0:
                history_indices.append(ptr)
            triggers[k][i] | circuit(trickbit)
            ptr += 1
        triggers_reset[k] | circuit(trickbit)
        ptr += 1
    return circuit, trickbit + history_indices[::-1]


def order_finding(a: int, N: int, eps: float = 1 / 10, simulator=CircuitSimulator()):
    """
    Shor algorithm by THOMAS HANER, MARTIN ROETTELER, and KRYSTA M. SVORE \
    in "Factoring using 2n+2 qubits with Toffoli based modular multiplication"
    Quantum algorithm to compute the order of a (mod N), when gcd(a,N)=1.
    """
    # phase estimation procedure
    n = int(np.ceil(np.log2(N + 1)))
    t = int(2 * n + 1 + np.ceil(np.log(2 + 1 / (2 * eps))))
    logger.info(f"\torder_finding begin: circuit: n = {n} t = {t}")
    trickbit_store = [0] * t

    circuit = Circuit(2 * n + 2)
    x_reg = list(range(n))
    ancilla = list(range(n, 2 * n))
    indicator = 2 * n
    trickbit = [2 * n + 1]
    # subcircuit: init \ket{1}\ket{0}
    circuit = Circuit(2 * n + 2)
    X | circuit(x_reg[n - 1])
    simulator.run(circuit)

    for k in range(t):
        # subcircuit CUa
        circuit = Circuit(2 * n + 2)
        H | circuit(trickbit)
        gate_pow = pow(a, 1 << (t - 1 - k), N)
        CHRSMulMod.execute(n, gate_pow, N) | circuit
        simulator.run(circuit, use_previous=True)
        # subcircuit: semi-classical QFT
        circuit = Circuit(2 * n + 2)
        for i in range(k):
            if trickbit_store[i]:
                Rz(-pi / (1 << (k - i))) | circuit(trickbit)
        H | circuit(trickbit)
        simulator.run(circuit, use_previous=True)
        circuit = Circuit(2 * n + 2)
        for idx in [trickbit] + ancilla + [indicator]:
            Measure | circuit(idx)
        simulator.run(circuit, use_previous=True)
        # subcircuit: measure & reset trickbit
        assert int(circuit[indicator]) == 0 and int(circuit[ancilla]) == 0
        logger.info(f"\tthe {k}th trickbit measured to be {int(circuit[trickbit])}")
        trickbit_store[k] = int(circuit[trickbit])
        if trickbit_store[k] == 1:
            circuit = Circuit(2 * n + 2)
            X | circuit(trickbit)
            simulator.run(circuit, use_previous=True)

    # for idx in x_reg: Measure | circuit(idx)
    trickbit_store.reverse()
    logger.info(f"\tphi~ (approximately s/r) in binary form is {trickbit_store}")
    # continued fraction procedure
    phi_ = sum([(trickbit_store[i] * 1.0 / (1 << (i + 1))) for i in range(t)])
    logger.info(f"\tphi~ (approximately s/r) in decimal form is {phi_}")
    if phi_ == 0.0:
        logger.info("\torder_finding failed: phi~ = 0")
        return 0
    frac = Fraction(phi_).limit_denominator(N)
    logger.info(f"\tContinued fraction expansion of phi~ is {frac}")
    return frac.denominator
