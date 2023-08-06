import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import CompositeGate, Swap, H, Measure, IQFT

from ..utility import OracleInfo, StatePreparationInfo


def construct_circuit(
    eps,
    oracle: OracleInfo,
    state_preparation: StatePreparationInfo,
):
    # see Theorem 12, case k=1
    n = oracle.n
    m = int(np.ceil(np.log2(2 * np.pi / (np.sqrt(1 + 4 * eps) - 1))))
    n_ancilla = max([1, oracle.n_ancilla, state_preparation.n_ancilla])
    trickbits = list(range(m))
    indices = list(range(m, m + n))
    ancilla = list(range(m + n, m + n + n_ancilla))

    cgate = CompositeGate()
    # state prepare
    state_preparation.A(n) | cgate(indices + ancilla)
    # Walsh-Hadamard transform
    for i in range(0, m):
        H | cgate(i)
    # controlled-Q^{2^j}
    Q_gate = CompositeGate()
    if oracle.custom_grover_operator is not None:
        Q_gate = oracle.custom_grover_operator
    else:
        oracle.S_chi(n, controlled=True) | Q_gate
        state_preparation.A_dagger(n, controlled=True) | Q_gate
        state_preparation.S_0(n, controlled=True) | Q_gate
        state_preparation.A(n, controlled=True) | Q_gate
    for j in range(m):
        for _ in range(1 << (m - 1 - j)):
            Q_gate | cgate([j] + list(range(m, m + n + n_ancilla)))
    # IQFT
    for k in range(len(trickbits) // 2):
        Swap | cgate([trickbits[k], trickbits[len(trickbits) - 1 - k]])
    IQFT.build_gate(m) | cgate(trickbits)
    for k in range(len(trickbits) // 2):
        Swap | cgate([trickbits[k], trickbits[len(trickbits) - 1 - k]])

    return cgate, {"trickbits": trickbits, "m": m, "n": n, "n_ancilla": n_ancilla}


def amplitude_estimate(
    eps,
    oracle: OracleInfo,
    state_preparation: StatePreparationInfo,
    simulator,
):
    """canonical Quantum Amplitude Estimation \
    in "Quantum Amplitude Amplification and Estimation"
    see arXiv:quant-ph/0005055

    Args:
        eps (float, optional): error allowed.
        oracle (OracleInfo): oracle information.
        state_preparation (StatePreparationInfo, optional): state preparation infomations.
        simulator (Simulator): Simulation backend.

    Returns:
        float: the amplitude of good states
    """
    cgate, info = construct_circuit(eps, oracle, state_preparation)
    circ = Circuit(info["m"] + info["n"] + info["n_ancilla"])
    cgate | circ
    for idx in info["trickbits"]:
        Measure | circ(idx)
    simulator.run(circ)
    y = int(circ[info["trickbits"]])
    return np.sin(np.pi * y / (1 << info["m"])) ** 2
