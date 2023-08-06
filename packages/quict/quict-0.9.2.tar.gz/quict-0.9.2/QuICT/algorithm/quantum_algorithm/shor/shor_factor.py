import random
from math import gcd
import numpy as np
from fractions import Fraction
from typing import List, Tuple

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.simulation.state_vector import CircuitSimulator
from .utility import *

from .BEA_zip import construct_circuit as BEA_zip_circuit
from .BEA_zip import order_finding as BEA_zip_run
from .BEA import construct_circuit as BEA_circuit
from .BEA import order_finding as BEA_run

from .HRS_zip import construct_circuit as HRS_zip_circuit
from .HRS_zip import order_finding as HRS_zip_run
from .HRS import construct_circuit as HRS_circuit
from .HRS import order_finding as HRS_run

from QuICT.tools import Logger
from QuICT.tools.exception.core import *

logger = Logger("Shor")


class ShorFactor:

    _ALLOWED_MODES = {"BEA", "HRS", "BEA_zip", "HRS_zip"}
    _RUN_METHOD_OF_MODE = {
        "BEA": reinforced_order_finding_constructor(BEA_run),
        "HRS": reinforced_order_finding_constructor(HRS_run),
        "BEA_zip": reinforced_order_finding_constructor(BEA_zip_run),
        "HRS_zip": reinforced_order_finding_constructor(HRS_zip_run),
    }
    _CIRCUIT_METHOD_OF_MODE = {
        "BEA": BEA_circuit,
        "HRS": HRS_circuit,
        "BEA_zip": BEA_zip_circuit,
        "HRS_zip": HRS_zip_circuit,
    }

    # add a, N here
    def __init__(self, mode: str, eps: float = 1 / 10, max_rd: int = 2, simulator=CircuitSimulator()) -> None:
        if mode not in ShorFactor._ALLOWED_MODES:
            raise ValueError(
                f"{mode} mode is not valid. Consider {ShorFactor._ALLOWED_MODES}"
            )
        random.seed(2022)
        self.mode = mode
        self.eps = eps
        self.max_rd = max_rd
        self.simulator = simulator
        self._previous_N = None

    def circuit(self, N: int) -> Tuple[Circuit, List[int]]:
        """construct the quantum part of Shor algorithm, i.e. order finding circuit

        Args:
            N (int): number to be factored

        Returns:
            Circuit: order finding circuit that can be passed to ShorFactor::run method
            List[int]: the indices to be measured to get ~phi
        """
        if self._previous_N is not None and self._previous_N == N:
            self._circuit_cache[0].reset_qubits()
            return self._circuit_cache
        # without usable previous circuit
        a = N
        while gcd(a, N) != 1:
            a = random.randrange(0, N)
        self._circuit_cache = ShorFactor._CIRCUIT_METHOD_OF_MODE[self.mode](a, N, self.eps)
        return self._circuit_cache

    def run(
        self,
        N,
        circuit: Circuit = None,
        indices: List = None,
        forced_quantum_approach=False
    ) -> int:
        """run full factoring algorithm.

        Args:
            N (int): number to be factored
            circuit (Circuit, optional): if None, a circuit will be constructed for order finding purpose;
                else the given circuit is used as order finding circuit. Defaults to None.
            indices (List, optional): The indices of $\\ket{n}$. Only used when `circuit` is not None. Defaults to None.
            forced_quantum_approach (bool, optional): If true, only x that gcd(x,N)=1 will be used. Defaults to False.

        Returns:
            int: the factor
        """
        simulator = self.simulator
        # check if input is prime (using MillerRabin in klog(N), k is the number of rounds to run MillerRabin)
        if miller_rabin(N):
            logger.info("N does not pass miller rabin test, may be a prime number")
            return 0
        # 1. If n is even, return the factor 2
        if N % 2 == 0:
            logger.info("Shor succeed: N is even, found factor 2 classically")
            return 2
        # 2. Classically determine if N = p^q
        y, L = np.log2(N), int(np.ceil(np.log2(N)))
        for b in range(2, L):
            squeeze = np.power(2, y / b)
            u1, u2 = int(np.floor(squeeze)), int(np.ceil(squeeze))
            if pow(u1, b) == N:
                logger.info(
                    f"Shor succeed: N is exponential, found the only factor {u1} classically"
                )
                return u1
            if pow(u2, b) == N:
                logger.info(
                    f"Shor succeed: N is exponential, found the only factor {u2} classically"
                )
                return u2
        rd = 0
        while rd < self.max_rd:
            logger.info(f"round = {rd}")
            # 3. Choose a random number a (1<a<N)
            if forced_quantum_approach:
                logger.info("forced quantum approach, looking for coprime number...")
                while True:
                    a = random.randint(2, N - 1)
                    gcd = np.gcd(a, N)
                    if gcd == 1:
                        break
            else:
                a = random.randint(2, N - 1)
                gcd = np.gcd(a, N)
                if gcd > 1:
                    logger.info(
                        f"Shor succeed: randomly chosen a = {a}, who has common factor {gcd} with N classically"
                    )
                    return gcd
            rd += 1
            # 4. Use quantum order-finding algorithm to find the order of a
            logger.info(
                f"Quantumly determine the order of the randomly chosen a = {a}"
            )
            # check if any input circuit. if no, run according to `mode`; else run the input circuit
            if circuit is None:
                r = ShorFactor._RUN_METHOD_OF_MODE[self.mode](
                    a=a, N=N, simulator=simulator
                )
            else:
                circuit.reset_qubits()
                simulator.run(circuit)
                if len(indices) > 0 and self.mode in {"BEA", "HRS"}:
                    phi = int(circuit[indices]) / (1 << len(indices))
                elif len(indices) > 0 and self.mode in {"BEA_zip", "HRS_zip"}:
                    phi = eval(
                        "0b" + "".join([str(circuit[indices[0]].historical_measured[idx]) for idx in indices[1:]])
                    ) / (1 << len(indices))
                else:
                    raise ValueError("wrong indices")
                logger.info(f"phi: {phi:4.3f}")
                r = Fraction(phi).limit_denominator(N - 1).denominator

            if r == 0:  # no order found
                logger.info(
                    f"Shor failed: did not find the order of a = {a}"
                )  # add mode info here
            elif r % 2 == 1:  # odd order
                logger.info(f"Shor failed: found odd order r = {r} of a = {a}")
            else:  # N | h^2 - 1, h = a^(r/2)
                h = pow(a, int(r / 2), N)
                if h == N - 1:  # N | h + 1
                    logger.info(
                        f"Shor failed: found order r = {r} of a = {a} with negative square root"
                    )
                else:  # N !| h + 1, therefore N | h - 1
                    f1, f2 = np.gcd(h - 1, N), np.gcd(h + 1, N)
                    if f1 > 1 and f1 < N:
                        logger.info(
                            f"Shor succeed: found factor {f1}, with the help of a = {a}, r = {r}"
                        )
                        return f1
                    elif f2 > 1 and f2 < N:
                        logger.info(
                            f"Shor succeed: found factor {f2}, with the help of a = {a}, r = {r}"
                        )
                        return f2
                    else:
                        logger.info(f"Shor failed: can not find a factor with a = {a}")
        return 0
