import numpy as np

from QuICT.algorithm import Algorithm
from QuICT.core import Circuit
from QuICT.core.gate import X, H, Measure
from QuICT.core.gate.backend import MCTOneAux
from QuICT.qcda.synthesis.quantum_state_preparation import QuantumStatePreparation
from QuICT.simulation.state_vector import ConstantStateVectorSimulator


def weight_decison_para(n, k, l):
    kap = k / n
    lam = l / n
    for d in range(n + 2):
        for gamma in range(2 * d - 2):
            s = (1 - np.cos(gamma * np.pi / (2 * d - 1))) / 2
            t = (1 - np.cos((gamma + 1) * np.pi / (2 * d - 1))) / 2
            if lam * s >= kap * t and (1 - kap) * (1 - t) >= (1 - lam) * (1 - s):
                a = np.sqrt((l - k) / (t - s) - (l * s - k * t) / (t - s) - n)
                b = np.sqrt(abs(l * s - k * t) / (t - s))
                return d, gamma, a, b


class WeightDecision(Algorithm):
    @classmethod
    def run(cls, n, k, l, oracle):
        """ decide function f by k-l algorithm by custom oracle
        https://arxiv.org/abs/1801.05717

        Args:
            f(list<int>): the function to be decided
            n(int): the length of function
            k(int): the smaller weight
            l(int): the bigger weight
            oracle(Gate/CompositeGate): the oracle
        Returns:
            int: the ans, k or l
        """
        num = int(np.ceil(np.log2(n + 2))) + 2

        # Determine number of qreg
        circuit = Circuit(num)
        d, gamma, a, b = weight_decison_para(n, k, l)

        # start the eng and allocate qubits
        qreg = circuit[[i for i in range(num - 2)]]
        ancilla = circuit[num - 2]

        # Start with qreg in equal superposition and ancilla in |->
        N = np.power(2, num - 2)
        value = [0 for _ in range(N)]
        for i in range(n):
            value[i] = 1 / np.sqrt(n + a ** 2 + b ** 2)

        value[N - 2] = a / np.sqrt(n + a ** 2 + b ** 2)
        value[N - 1] = b / np.sqrt(n + a ** 2 + b ** 2)

        # Apply oracle U_f which flips the phase of every state |x> with f(x) = 1
        QSP = QuantumStatePreparation('uniformly_gates')
        gates_preparation = QSP.execute(value)
        gates_preparation | circuit(qreg)
        X | circuit(ancilla)
        H | circuit(ancilla)

        MCTOA = MCTOneAux()
        gates_mct = MCTOA.execute(num)

        for i in range(d - 1):
            oracle | circuit([i for i in range(num - 1)])
            gates_mct | circuit
            gates_preparation ^ circuit(qreg)
            for q in qreg:
                X | circuit(q)

            gates_mct | circuit
            for q in qreg:
                X | circuit(q)

            gates_preparation | circuit(qreg)

        # Apply H,X to recover ancilla
        H | circuit(ancilla)
        X | circuit(ancilla)
        oracle | circuit(list(range(num - 1)))
        gates_mct | circuit

        # Measure
        for i in range(num - 1):
            Measure | circuit(i)

        simulator = ConstantStateVectorSimulator()
        _ = simulator.run(circuit)

        if int(ancilla) == gamma % 2:
            return k
        else:
            return l
