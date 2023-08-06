import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import CompositeGate, GateType, GPhase, X, CX, Ry, Rz
from QuICT.core.gate.backend import MCTWithoutAux, UniformlyRotation
from QuICT.qcda.synthesis.unitary_decomposition import UnitaryDecomposition
from QuICT.simulation.state_vector import ConstantStateVectorSimulator


class QuantumStatePreparation(object):
    """
    For a given quantum state |psi>, create a CompositeGate C that |psi> = C |0>
    """
    def __init__(self, method='unitary_decomposition'):
        """
        Choose the method between reference [1] and [2], designing circuit of
        quantum state preparation with uniformly gates and unitary decomposition respectively

        Args:
            method(str, optional): chosen method in ['uniformly_gates', 'unitary_decomposition']

        Reference:
            [1] https://arxiv.org/abs/quant-ph/0407010v1
            [2] https://arxiv.org/abs/1003.5760
        """
        assert method in ['uniformly_gates', 'unitary_decomposition'],\
            ValueError('Invalid quantum state preparation method')
        self.method = method

    def execute(self, state_vector):
        """
        Args:
            state_vector(np.ndarray): the statevector to be prapared

        Returns:
            CompositeGate: the preparation CompositeGate
        """
        if self.method == 'uniformly_gates':
            return self._with_uniformly_gates(state_vector)
        if self.method == 'unitary_decomposition':
            return self._with_unitary_decomposition(state_vector)

    def _with_uniformly_gates(self, state_vector):
        """
        Quantum state preparation with uniformly gates

        Args:
            state_vector(np.ndarray): the statevector to be prapared

        Returns:
            CompositeGate: the preparation CompositeGate

        Reference:
            https://arxiv.org/abs/quant-ph/0407010v1
        """
        state_vector = np.array(state_vector)
        num_qubits = int(round(np.log2(state_vector.size)))
        assert state_vector.ndim == 1 and 1 << num_qubits == state_vector.size,\
            ValueError('Quantum state should be an array with length 2^n')

        gates = CompositeGate()
        omega = np.angle(state_vector)
        state_vector = np.abs(state_vector)
        # Now for the non-negative real state_vector
        URy = UniformlyRotation(GateType.ry)
        denominator = np.linalg.norm(state_vector)
        for k in range(num_qubits - 1, -1, -1):
            numerator = np.linalg.norm(state_vector.reshape(1 << num_qubits - k, 1 << k), axis=1)
            alpha = np.where(np.isclose(denominator, 0), 0, 2 * np.arcsin(numerator[1::2] / denominator))
            gates.extend(URy.execute(alpha))
            denominator = numerator
        # If state_vector is real and non-negative, no UniformlyRz will be needed.
        URz = UniformlyRotation(GateType.rz)
        if not np.allclose(omega, 0):
            for k in range(num_qubits):
                alpha = np.sum(omega.reshape(1 << num_qubits - k, 1 << k), axis=1)
                alpha = (alpha[1::2] - alpha[0::2]) / (1 << k)
                gates.extend(URz.execute(alpha))
            gates.append(GPhase(np.average(omega)) & 0)

        return gates

    def _with_unitary_decomposition(self, state_vector):
        """
        Quantum state preparation with unitary decomposition

        Args:
            state_vector(np.ndarray): the statevector to be prapared

        Returns:
            CompositeGate: the preparation CompositeGate

        Reference:
            https://arxiv.org/abs/1003.5760
        """
        state_vector = np.array(state_vector)
        num_qubits = int(round(np.log2(state_vector.size)))
        assert state_vector.ndim == 1 and 1 << num_qubits == state_vector.size,\
            ValueError('Quantum state should be an array with length 2^n')

        first_half = num_qubits // 2 if np.mod(num_qubits, 2) == 0 else (num_qubits - 1) // 2
        last_half = num_qubits - first_half
        state_vector = state_vector.reshape(1 << first_half, 1 << last_half)
        # Schmidt decomposition
        U, d, V = np.linalg.svd(state_vector)

        gates = CompositeGate()
        # Phase 1
        gates.extend(self._with_uniformly_gates(d))
        # Phase 2
        with gates:
            for i in range(first_half):
                CX & [i, i + first_half]
        UD = UnitaryDecomposition()
        # Phase 3
        U_gates, _ = UD.execute(U)
        gates.extend(U_gates)
        # Phase 4
        if np.mod(num_qubits, 2) != 0:
            V = V[np.arange(1 << last_half).reshape(2, 1 << last_half - 1).T.flatten()]
        V_gates, _ = UD.execute(V.T)
        V_gates & list(range(first_half, num_qubits))
        gates.extend(V_gates)

        return gates


class SparseQuantumStatePreparation(object):
    """
    For a sparse quantum state |psi>, i.e. only a few of entries in the statevector is not zero,
    create a circuit C that |psi> = C |0>
    """
    def __init__(self, input_format='state_vector'):
        """
        Despite the original state vector, we could also use a 'state array' to describe a sparse quantum state.
        That is, each element [basis, amplitude] in the state array gives the amplitude on the computational basis,
        where the bases are boolean strings and not shown amplitudes are zeros.
        Be careful that no duplicated basis is allowed.

        Args:
            input_mode(str, optional): chosen input in ['state_array', 'state_vector']

        Reference:
            https://ieeexplore.ieee.org/abstract/document/9586240/metrics
        """
        assert input_format in ['state_array', 'state_vector'],\
            ValueError('Invalid sparse quantum state preparation input format')
        self.input_format = input_format

    def execute(self, state_array) -> CompositeGate:
        """
        Quantum state preparation for sparse state

        Args:
            state_array: input quantum state, whose format is decided by the input_format

        Returns:
            CompositeGate: the preparation CompositeGate
        """
        if self.input_format == 'state_array':
            # By the dict rule, only the last value of duplicated key works.
            state = dict(state_array)
            width = len(list(state.keys())[0])
            for basis in state.keys():
                assert len(basis) == width, ValueError('Bases must have the same length.')
            state_vector = self.dict_to_statevector(state, width)
        if self.input_format == 'state_vector':
            state, width = self.statevector_to_dict(state_array)
            state_vector = np.array(state_array)

        gates = CompositeGate()
        simulator = ConstantStateVectorSimulator()
        while len(state) > 1:
            gates_last = self.reduce_state(state, width)
            state_vector = self.dict_to_statevector(state, width)
            cir = Circuit(width)
            cir.extend(gates_last)
            state_vector = simulator.run(cir, state_vector).get()
            state, width = self.statevector_to_dict(state_vector)
            gates.extend(gates_last)

        x = list(state.keys())[0]
        for b in range(width):
            if x[b] == '1':
                X & b | gates
        phase = -np.angle(state[x])
        GPhase(phase) & 0 | gates
        return gates.inverse()

    def reduce_state(self, state: dict, width: int) -> CompositeGate:
        """
        Algorithm 1 in the reference, to reduce the non-zero entries in the state vector.

        Args:
            state(dict): a sparse state dict
            width(int): the width of the state

        Returns:
            CompositeGate: a CompositeGate that reduce the state dict
        """
        gates = CompositeGate()
        self.dif_qubits = []
        self.dif_values = []

        x1 = self.dif_qubits_values(state.keys(), width)
        dif = self.dif_qubits.pop()
        self.dif_values.pop()

        T_prime = []
        for x in state.keys():
            tp = True
            for b, v in zip(self.dif_qubits, self.dif_values):
                if x[b] != str(v):
                    tp = False
                    break
            if tp:
                T_prime.append(x)
        T_prime.remove(x1)
        x2 = self.dif_qubits_values(T_prime, width)

        if x1[dif] != '1':
            X & dif | gates
        for b in range(width):
            if b == dif:
                continue
            if x1[b] != x2[b]:
                CX & [dif, b] | gates
        for b in self.dif_qubits:
            if x2[b] != '1':
                X & b | gates

        mcg, _ = self.multicontrol_G(len(self.dif_qubits), state[x2], state[x1])
        mcg & (self.dif_qubits + [dif])
        mcg | gates
        return gates

    def dif_qubits_values(self, basis_list: list, width: int):
        while len(basis_list) > 1:
            dif_b = None
            dif_T0 = []
            dif_T1 = []
            for b in range(width):
                T0 = []
                T1 = []
                for x in basis_list:
                    if x[b] == '0':
                        T0.append(x)
                    else:
                        T1.append(x)
                if T0 and T1 and np.abs(len(dif_T0) - len(dif_T1)) <= np.abs(len(T0) - len(T1)):
                    dif_b = b
                    dif_T0 = T0
                    dif_T1 = T1
            self.dif_qubits.append(dif_b)
            if len(dif_T0) <= len(dif_T1):
                self.dif_values.append(0)
                basis_list = dif_T0
            else:
                self.dif_values.append(1)
                basis_list = dif_T1
        return basis_list[0]

    @staticmethod
    def multicontrol_G(control: int, alpha: complex, beta: complex) -> CompositeGate:
        """
        Create a CompositeGate that maps alpha|0> + beta|1> to e^{i phase} |0> with some control qubits

        Args:
            control(int): the number of control qubits
            alpha(complex): alpha in the initial state
            beta(complex): beta in the initial stats

        Returns:
            CompositeGate: the required CompositeGate

        References:
            https://arxiv.org/abs/quant-ph/9503016
        """
        arr = np.array([alpha, beta])
        arr /= np.linalg.norm(arr)
        alpha, beta = arr
        omega = 2 * np.arcsin(np.abs(alpha))
        gamma = np.angle(alpha) - np.angle(beta)

        gates = CompositeGate()
        Rz(gamma) & control | gates
        Ry(omega / 2) & control | gates
        MCTWithoutAux().execute(control + 1) | gates
        Ry(-omega / 2) & control | gates
        Rz(-gamma) & control | gates

        return gates, np.angle(alpha)

    @staticmethod
    def statevector_to_dict(state_vector):
        state = dict()
        width = int(round(np.log2(state_vector.size)))
        for basis, amp in enumerate(state_vector):
            if not np.isclose(amp, 0):
                state[bin(basis)[2:].zfill(width)] = amp
        return state, width

    @staticmethod
    def dict_to_statevector(state: dict, width):
        state_vector = np.zeros(1 << width, dtype=complex)
        for basis, amp in state.items():
            if not np.isclose(amp, 0):
                basis = int(basis, base=2)
                state_vector[basis] = amp
        return state_vector
