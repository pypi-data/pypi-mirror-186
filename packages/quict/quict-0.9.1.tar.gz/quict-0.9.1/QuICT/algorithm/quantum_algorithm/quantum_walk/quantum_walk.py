import numpy as np
from typing import Dict, List, Union

from .graph import Graph
from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.simulation.state_vector import CircuitSimulator


class QuantumWalk:
    """ The Quantum Random Walk Algorithm. """

    @property
    def step(self):
        return self._step

    @property
    def graph(self):
        return str(self._graph)

    @property
    def circuit(self) -> Circuit:
        """ The quantum circuit of the random walk algorithm, including UnitaryGate. """
        return self._circuit

    def __init__(self, simulator=CircuitSimulator()):
        """ Initialize the simulator circuit of quantum random walk.

        Args:
            simulator (Union[ConstantStateVectorSimulator, CircuitSimulator], optional):
                The simulator for simulating quantum circuit. Defaults to CircuitSimulator().
        """
        self._simulator = simulator
        self._step = None
        self._graph = None
        self._shift_operator = None
        self._coin_operator = None
        self._position_qubits = None
        self._action_qubits = None
        self._total_qubits = None
        self._operator_by_position = False
        self._operator_by_time = False

        # parameters only for quantum walk search
        self._search = False
        self._target = None
        self._coin_marked = None
        self._coin_unmarked = None

    def _coin_operator_validation(self, coin_operator):
        """ Validate the operator. """
        if coin_operator is not None:
            assert self._graph.operator_validation(
                coin_operator
            ), "The coin operator should be an unitary matrix."
            if self._search:
                assert coin_operator.shape[0] == 1 << self._total_qubits, (
                    "The coin oracle should be a unitary matrix"
                    "with side length 2 ** totel_qubits. "
                )
            else:
                self._action_qubits = int(np.ceil(np.log2(coin_operator.shape[0])))
        else:
            self._coin_operator = self._graph.operators
            self._action_qubits = self._graph.action_qubits
            self._operator_by_position = True
            self._operator_by_time = self._graph.switched_time > 0

    def _circuit_construct(self):
        """ Construct random walk circuit. """
        # Build Circuit
        self._circuit = Circuit(self._total_qubits)
        if self._search:
            for idx in range(self._total_qubits):
                H | self.circuit(idx)
        for t in range(self.step):
            self._build_coin_operator(t) | self._circuit
            self._build_shift_operator() | self._circuit

    def _build_coin_operator(self, step: int) -> CompositeGate:
        """ Generator action operator. """
        if self._search:
            search_array = np.zeros((self._graph.position, self._graph.position))
            for target in self._targets:
                search_array[target][target] = 1
            coin_oracle = np.kron(
                np.eye(self._graph.position), self._coin_unmarked
            ) + np.kron(search_array, self._coin_marked - self._coin_unmarked)
            return Unitary(coin_oracle)

        action_qubits = [self._position_qubits + i for i in range(self._action_qubits)]
        if not (self._operator_by_position or self._operator_by_time):
            return Unitary(self._coin_operator) & action_qubits

        action_gate = CompositeGate()
        curr_op_idx = (
            (step // self._graph.switched_time) % len(self._graph.operators[0])
            if self._operator_by_time
            else 0
        )
        for i in range(self._graph.position):
            op = self._graph.operators[i][curr_op_idx]
            x_idx = [
                pidx for pidx in range(self._position_qubits) if not (i & 1 << pidx)
            ]
            for xi in x_idx:
                X | action_gate(xi)

            self._mct_generator(op) | action_gate
            for xi in x_idx:
                X | action_gate(xi)
        action_gate.gate_decomposition()
        return action_gate

    def _mct_generator(self, op: np.ndarray) -> UnitaryGate:
        """ Build multi-control-'op' gate. """
        mct_unitary = np.identity(1 << self._total_qubits, dtype=np.complex128)
        op_shape = op.shape
        mct_unitary[-op_shape[0]:, -op_shape[1]:] = op

        return Unitary(mct_unitary) & list(range(self._total_qubits))

    def _build_shift_operator(self):
        """ Generator shift operator. """
        unitary_matrix = np.zeros(
            (1 << self._total_qubits, 1 << self._total_qubits), dtype=np.complex128
        )
        record_idxes = list(range(1 << self._total_qubits))
        for i in range(self._graph.position):
            curr_idx = (1 << self._action_qubits) * i
            for action_state in range(self._graph.action_space):
                related_idx = self._graph.edges[i][action_state] * (
                    1 << self._action_qubits
                )
                unitary_matrix[related_idx + action_state, curr_idx + action_state] = 1
                if related_idx + action_state in record_idxes:
                    record_idxes.remove(related_idx + action_state)

        if len(record_idxes) > 0:
            unitary_matrix[record_idxes, record_idxes] = 1

        return Unitary(unitary_matrix)

    def run(
        self,
        step: int,
        position: int,
        edges: Union[List, Dict] = None,
        operators: Union[List, Dict] = None,
        coin_operator: np.ndarray = None,
        switched_time: int = -1,
        shots: int = 1000,
    ) -> Union[np.ndarray, List]:
        """ Execute the quantum random walk with given steps, graph and coin operator.

        Args:
            step (int): The steps of random walk, a step including a coin operator and a shift operator.
            position (int): The number of graph's vertex.
            edges (Union[List, Dict], optional): The edges of each vertex. Defaults to None.
            operators (Union[List, Dict], optional): The operators of each vertex. Defaults to None.
            switched_time (int, optional): The number of steps of each coin operator in the vector.
                Defaults to -1, means not switch coin operator.
            coin_operator (np.ndarray, optional): The coin operators, the unitary matrix. Defaults to None.
            shots (int, optional): The repeated times. Defaults to 1000.

        Returns:
            Union[np.ndarray, List]: The state vector or measured states.
        """
        self._step = step
        self._graph = Graph(position, edges, operators, switched_time)
        self._coin_operator = coin_operator

        # Validation graph and coin operator
        assert self._graph.validation(), "The edge's number should be equal."
        self._coin_operator_validation(self._coin_operator)
        self._position_qubits = self._graph.position_qubits
        self._total_qubits = self._position_qubits + self._action_qubits

        # Build random walk circuit
        self._circuit_construct()

        # Simulate the quantum walk's circuit
        _ = self._simulator.run(self._circuit)

        return self._simulator.sample(shots)
