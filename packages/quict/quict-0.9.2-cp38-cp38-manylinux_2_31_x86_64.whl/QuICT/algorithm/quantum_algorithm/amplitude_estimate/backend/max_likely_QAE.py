import numpy as np
from scipy.optimize import brute

from QuICT.core import Circuit
from QuICT.core.gate import CompositeGate
from ..utility import OracleInfo, StatePreparationInfo


def amplitude_estimate(
    eps,
    oracle: OracleInfo,
    state_preparation: StatePreparationInfo,
    simulator,
):
    """implementation of maximum likelyhood estimation in "Amplitude estimation without phase estimation"\
    see arXiv:1904.10246[quant-ph]
    The list of (N,m) is \
    constructed from eps in EIS style where N_shot=100

    Args:
        eps (float): Error allowed.
        oracle (OracleInfo): Oracle information.
        state_preparation (StatePreparationInfo): State preparation information.
        simulator (Simulator): Simulation backend.
    """
    n = oracle.n
    n_ancilla = max([1, oracle.n_ancilla, state_preparation.n_ancilla])

    # list (N,m): N=100, m=[2**0...2**(M-1)]
    N_shot = 100
    M = max(3, np.log2((1 / eps) / N_shot))
    list_m = np.array([2 ** i for i in range(int(M))])

    # Q^{m[i]}
    Q_gate = CompositeGate()
    if oracle.custom_grover_operator is not None:
        Q_gate = oracle.custom_grover_operator
    else:
        oracle.S_chi(n) | Q_gate
        state_preparation.A_dagger(n) | Q_gate
        state_preparation.S_0(n) | Q_gate
        state_preparation.A(n) | Q_gate

    good_counts = np.zeros(shape=(len(list_m),))
    all_counts = np.ones(shape=(len(list_m),)) * N_shot
    for i, m in enumerate(list_m):
        circ = Circuit(n + n_ancilla)
        state_preparation.A(n) | circ
        for _ in range(m):
            Q_gate | circ

        simulator.run(circ)
        sample_result = simulator.sample(N_shot)
        for j in range(2 ** (n + n_ancilla)):
            res = bin(j)[2:].rjust(n + n_ancilla, "0")
            if oracle.is_good_state(res[:n]):
                good_counts[i] += sample_result[j]

    # MLE
    search_eps = 1e-10
    nevals = max(10000, int(np.pi / 2 * 1000 * 2 * (2 ** M)))

    def _loglikelyhood(theta):
        fst_half = good_counts * np.log(np.sin((list_m * 2 + 1) * theta) ** 2)
        sec_half = (all_counts - good_counts) * np.log(
            np.cos((list_m * 2 + 1) * theta) ** 2
        )
        return -(np.sum(fst_half + sec_half))

    est_theta = brute(
        _loglikelyhood,
        ranges=[[0 + search_eps, np.pi / 2 - search_eps]],
        Ns=nevals)[0]
    return np.sin(est_theta) ** 2
