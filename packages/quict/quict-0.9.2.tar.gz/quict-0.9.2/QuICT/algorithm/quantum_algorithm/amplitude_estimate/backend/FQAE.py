import logging
import numpy as np
from math import floor, ceil, pi, acos, asin, log, log2, sqrt, cos, sin

from QuICT.core import Circuit
from QuICT.core.gate import Ry

from ..utility import OracleInfo, StatePreparationInfo


DELTA = 0.05
N_1_SHOT_CONST = 216    # TODO: optimization
N_2_SHOT_CONST = 216    # TODO: optimization


def _cos_estimate(
    m,
    N_shot,
    oracle: OracleInfo,
    state_preparation: StatePreparationInfo,
    simulator=None,
):
    """estimate cos(2(2**m+1)θ) in modified oracle A×R
    """
    n = oracle.n
    n_ancilla = max([1, oracle.n_ancilla, state_preparation.n_ancilla])
    # Q'^m where A'=A×R
    if oracle.custom_grover_operator is not None:
        raise ValueError("custom grover operator not supported")
    good_count = 0
    circ = Circuit(n + n_ancilla + 1)
    state_preparation.A(n) | circ(list(range(n + n_ancilla)))
    Ry(asin(1 / 4) * 2) | circ(n + n_ancilla)
    for _ in range(m):
        oracle.S_chi(n, controlled=True) | circ(
            [n + n_ancilla] + list(range(n + n_ancilla))
        )  # assert default control bit on 0
        state_preparation.A_dagger(n) | circ(list(range(n + n_ancilla)))
        Ry(-asin(1 / 4) * 2) | circ([n + n_ancilla])
        state_preparation.S_0(n + 1) | circ(
            [n + n_ancilla] + list(range(n + n_ancilla))
        )
        state_preparation.A(n) | circ(list(range(n + n_ancilla)))
        Ry(asin(1 / 4) * 2) | circ([n + n_ancilla])
    simulator.run(circ)
    sample_result = simulator.sample(N_shot)
    for i in range(2 ** (n + n_ancilla + 1)):
        res = bin(i)[2:].rjust(n + n_ancilla + 1, "0")
        if oracle.is_good_state(res[:n]) and res[n + n_ancilla] == "1":
            good_count += sample_result[i]

    logging.info(f"sample:{good_count:8}/{N_shot:8} with {n+n_ancilla+1:2} qubits")
    return 1 - 2 * good_count / N_shot


def _chernoff(c, N_shot, delta):
    c_max = min(1, c + sqrt(log(2 / delta) * 12 / N_shot))
    c_min = max(-1, c - sqrt(log(2 / delta) * 12 / N_shot))
    return c_min, c_max


def _atan(s, c):
    # assert np.isclose(s**2+c**2,1)
    if np.isclose(c, 0):
        if np.isclose(s, 0):
            return 0
        elif s > 0:
            return pi / 2
        else:
            return -pi / 2
    elif c > 0:
        return np.arctan(s / c)
    else:
        if s >= 0:
            return pi + np.arctan(s / c)
        else:
            return -pi + np.arctan(s / c)


def amplitude_estimate(
    eps,
    oracle: OracleInfo,
    state_preparation: StatePreparationInfo,
    simulator,
):
    """implementation of the paper "Faster Amplitude Estimation".\
    see arXiv:2003.02417[quant-ph]

    Args:
        eps (float): Error allowed.
        oracle (OracleInfo): Oracle information.
        state_preparation (StatePreparationInfo): State preparation information.
        simulator (Simulator): Simulation backend.
    """
    # algorithm parameters
    true_eps = eps / 2  # (4*a+true_eps)**2-(4*a)**2<eps and a<1/4
    l = ceil(1 + log2(pi / (3 * true_eps)))  # by formula 27
    delta = DELTA  # fixed
    delta_c = delta / (2 * l)  # success rate of $1-2l\delta_c$
    N_1_shot = ceil(N_1_SHOT_CONST * log(2 / delta_c))
    N_2_shot = ceil(N_2_SHOT_CONST * log(2 / delta_c))
    logging.info(f"using (l,N1,N2)=({l:2},{N_1_shot:5},{N_2_shot:5})")
    theta_min, theta_max = 0, 0.252
    j0 = l
    mu = None
    is_first_stage = True

    for j in range(1, l + 1):
        if is_first_stage:
            c_estimate = _cos_estimate(
                2 ** (j - 1), N_1_shot, oracle, state_preparation, simulator
            )
            c_min, c_max = _chernoff(c_estimate, N_1_shot, delta_c)
            theta_min, theta_max = (
                acos(c_max) / (2 ** (j + 1) + 2),
                acos(c_min) / (2 ** (j + 1) + 2),
            )  # update
            if (2 ** (j + 1)) * theta_max >= 3 * pi / 8 and j < l:
                j0 = j
                mu = (2 ** j0) * (theta_min + theta_max)
                is_first_stage = False
        else:
            c_estimate = _cos_estimate(
                2 ** (j - 1), N_2_shot, oracle, state_preparation, simulator
            )
            s_estimate = (
                c_estimate * cos(mu) - _cos_estimate(
                    2 ** (j - 1) + 2 ** (j0 - 1),
                    N_2_shot,
                    oracle,
                    state_preparation,
                    simulator,
                )
            ) / sin(mu)
            rmd_by_2pi = _atan(s_estimate, c_estimate)
            quo_by_2pi = floor(
                ((2**(j + 1) + 2) * theta_max - rmd_by_2pi + pi / 3) / (2 * pi)
            )
            theta_min, theta_max = (
                (2 * pi * quo_by_2pi + rmd_by_2pi - pi / 3) / (2**(j + 1) + 2),
                (2 * pi * quo_by_2pi + rmd_by_2pi + pi / 3) / (2**(j + 1) + 2),
            )  # update
    theta_estimate = (theta_max + theta_max) / 2
    return (sin(theta_estimate) * 4) ** 2
