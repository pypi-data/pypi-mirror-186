import matplotlib.pyplot as plt
import numpy as np

from QuICT.algorithm.quantum_algorithm.quantum_walk import Graph, QuantumWalk
from QuICT.simulation.state_vector import ConstantStateVectorSimulator


class QuantumWalkSearch(QuantumWalk):
    """ Search algorithm on a hypercube based on quantum walk and Grover.

    https://arxiv.org/pdf/quant-ph/0210064.pdf
    http://dx.doi.org/10.4236/jqis.2015.51002
    """

    def __init__(self, simulator=ConstantStateVectorSimulator()):
        """ Initialize the simulator circuit of quantum random walk.

        Args:
            simulator (Union[ConstantStateVectorSimulator, CircuitSimulator], optional):
                The simulator for simulating quantum circuit. Defaults to ConstantStateVectorSimulator().
        """
        QuantumWalk.__init__(self, simulator)
        self._search = True

    def _is_unit_hamming_distance(self, x, y):
        """ Calculate the hamming distance of two nodes of the n-cube. """
        return str(bin(x ^ y))[2:].count("1") == 1

    def _get_hypercube_edges(self, position):
        """ Get the edges of the n-cube graph. """
        edge = []
        for i in range(position):
            e = list(np.zeros(self._position_qubits, dtype=np.int64))
            for j in range(position):
                if self._is_unit_hamming_distance(i, j):
                    e[int(np.ceil(np.log2(i ^ j)))] = j
            edge.append(e)
        return edge

    def _set_coins(self, r, a_r, a_nr):
        """ Set the coins for marked and unmarked nodes. """
        n = 2 ** self._action_qubits
        if r is None:
            r = self._action_qubits
        assert 0 <= r < n, "r should in the range of [0, n - 1]."
        assert a_r > a_nr, "a_r should larger than a_nr."

        # set C0 to G
        s_c = np.ones((n, n)) / n
        self._coin_unmarked = np.eye(n) - 2 * s_c

        # set C1
        a = np.sqrt(a_r * a_r + (n - 1) * (a_nr * a_nr))
        x = np.zeros((1, n))
        for i in range(n):
            x[0, i] = a_r / a if i == r else a_nr / a
        self._coin_marked = np.eye(n) - 2 * (x.T @ x)

    def run(
        self,
        index_qubits: int,
        targets: list = None,
        step: int = None,
        r: int = None,
        a_r: float = 1,
        a_nr: float = 0,
        switched_time: int = -1,
        shots: int = 1000,
    ):
        """ Execute the quantum walk search with given number of index qubits.

        Args:
            index_qubits (int): The size of the node register.
            targets (list, optional): The indexes of the target elements.
            step (int, optional): The steps of random walk, a step including a coin operator and a shift operator.
            r (int, optional): The 'direction' of inclination of an asymmetric coin. Defaults to action_qubits (c).
            a_r (float, optional): Parameter of the asymmetry degree of the coin. Defaults to 1.
            a_nr (float, optional): Parameter of the asymmetry degree of the coin. Defaults to 0.
            switched_time (int, optional): The number of steps of each coin operator in the vector.
                Defaults to -1, means not switch coin operator.
            shots (int, optional): The repeated times. Defaults to 1000.

        Returns:
            Union[np.ndarray, List]: The state vector or measured states.
        """

        self._position_qubits = index_qubits  # n
        self._action_qubits = int(np.ceil(np.log2(index_qubits)))  # c
        self._total_qubits = self._position_qubits + self._action_qubits
        position = 1 << index_qubits  # N
        self._step = (
            step
            if step is not None and step > 0
            else int(np.ceil(1.0 / np.sqrt(len(targets) / position))) + 1
        )
        self._step = 6
        self._set_coins(r, a_r, a_nr)
        edges = self._get_hypercube_edges(position)
        self._graph = Graph(position, edges, None, switched_time)

        # Validation graph
        assert self._graph.validation(), "The edge's number should be equal."
        # Validation coin operator
        assert (
            targets is not None and len(targets) > 0
        ), "Should provide target indexes."
        for target in targets:
            assert (
                0 <= target < position
            ), "Target should be within the range of values allowed by the index register. "
        self._targets = targets

        # Build random walk circuit
        self._circuit_construct()

        # Simulate the circuit
        _ = self._simulator.run(self._circuit)

        return self._simulator.sample(shots)
