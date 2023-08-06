from itertools import chain
from math import log2

from QuICT.core import *
from QuICT.core.gate import *


class PhasePolynomial:
    """
    Phase polynomial representation of a quantum circuit that only contains
    X, CX and Rz gates.
    """
    def __init__(self, gates):
        """
        Create a phase polynomial from given circuit. The circuit can only contain
        Controlled-X and Rz gates.

        Args:
            gates(DAG): Circuit represented by this polynomial
        """

        self.phases = {}
        self.gates = []
        self.size = gates.width()
        self._build_poly(gates)

    def _build_poly(self, gates):
        monomials = {}
        for gate_ in gates:
            gate_: BasicGate
            for qubit_ in chain(gate_.cargs, gate_.targs):
                if qubit_ not in monomials:
                    monomials[qubit_] = 1 << (qubit_ + 1)

            if gate_.qasm_name == 'cx':
                monomials[gate_.targ] = monomials[gate_.targ] ^ monomials[gate_.carg]
                self.gates.append(gate_)
            elif gate_.qasm_name == 'x':
                monomials[gate_.targ] = monomials[gate_.targ] ^ 1
                self.gates.append(gate_)
            elif gate_.qasm_name == 'rz':
                sign = -1 if monomials[gate_.targ] & 1 else 1
                mono = (monomials[gate_.targ] >> 1)
                self.phases[mono] = sign * gate_.parg + (self.phases[mono] if mono in self.phases else 0)
            else:
                raise Exception("PhasePolynomial only accepts cx, x and rz gates.")

    def get_circuit(self, epsilon=1e-10):
        """
        Generate a circuit of minimal size that implements the phase polynomial

        Returns:
            Circuit: Circuit equivalent to this polynomial
        """
        max_monomial = max(self.phases.keys()) if len(self.phases.keys()) > 0 else 1
        circ = Circuit(self.size)
        visited = set()
        for qubit_ in range(int(np.ceil(log2(max_monomial + 1))) + 1):
            if (1 << qubit_) in self.phases:
                if abs(self.phases[1 << qubit_]) > epsilon:
                    Rz(self.phases[1 << qubit_]) | circ(qubit_)
                visited.add(1 << qubit_)

        monomials = {}
        for gate_ in self.gates:
            gate_: BasicGate
            for qubit_ in chain(gate_.cargs, gate_.targs):
                if qubit_ not in monomials:
                    monomials[qubit_] = 1 << (qubit_ + 1)

            if gate_.qasm_name == 'cx':
                monomials[gate_.targ] = monomials[gate_.targ] ^ monomials[gate_.carg]
            elif gate_.qasm_name == 'x':
                monomials[gate_.targ] = monomials[gate_.targ] ^ 1

            gate_.copy() | circ(list(chain(gate_.cargs, gate_.targs)))
            cur_phase = monomials[gate_.targ] >> 1
            cur_sign = -1 if (monomials[gate_.targ] & 1) else 1

            if cur_phase in self.phases and cur_phase not in visited:
                if abs(self.phases[cur_phase]) > epsilon:
                    Rz(cur_sign * self.phases[cur_phase]) | circ(gate_.targ)
                visited.add(cur_phase)

        return circ
