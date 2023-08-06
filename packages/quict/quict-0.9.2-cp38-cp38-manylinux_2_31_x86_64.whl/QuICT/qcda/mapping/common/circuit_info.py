import copy
import random
from typing import Dict, List, Tuple, Union

import networkx as nx
import numpy as np
from QuICT.core import *
from QuICT.core.gate import BasicGate, CompositeGate


class CircuitInfo:
    """DAG Representation of a quantum circuit."""

    def __init__(self, circ: Union[Circuit, CompositeGate], max_gate_num: int) -> None:
        self._qubit_num = circ.width()
        self._max_gate_num = max_gate_num
        q = circ.width()
        if isinstance(circ, (Circuit, CompositeGate)):
            self._gates: List[BasicGate] = copy.deepcopy(circ.gates)
        else:
            raise TypeError(
                "circ argument only supports Circuit/CompositeGate/List[BasicGate]"
            )

        self._graph = nx.DiGraph()
        for gid in range(len(self._gates)):
            self._graph.add_node(gid)

        self._first_layer_gates = None

        occupied = [-1 for _ in range(q)]
        self._bit2gid: List[List[int]] = [[] for _ in range(q)]
        """Qubit to all gates on it."""
        for gid, gate in enumerate(self._gates):
            bit_num = gate.controls + gate.targets
            assert bit_num <= 2, "Only 1 or 2 bit gates are supported."
            self._reset_cache()
            if bit_num == 1:
                a = gate.targ
                self._bit2gid[a].append(gid)
                if occupied[a] != -1:
                    self._graph.add_edge(occupied[a], gid)
                nx.set_node_attributes(self._graph, {gid: {"gid": gid}})
                occupied[a] = gid
            elif bit_num == 2:
                a, b = gate.cargs + gate.targs
                assert a != b
                # Position to Gate ID
                self._bit2gid[a].append(gid)
                self._bit2gid[b].append(gid)
                # DAG edges
                if occupied[a] != -1:
                    self._graph.add_edge(occupied[a], gid)
                if occupied[b] != -1:
                    self._graph.add_edge(occupied[b], gid)
                nx.set_node_attributes(self._graph, {gid: {"gid": gid}})
                occupied[a] = gid
                occupied[b] = gid

        self._removed_cnt = 0

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    def copy(self):
        return copy.deepcopy(self)

    def count_gate(self) -> int:
        return nx.number_of_nodes(self._graph)

    def _reset_cache(self):
        self._first_layer_gates = None

    @property
    def first_layer_gates(self) -> Dict[int, BasicGate]:
        if self._first_layer_gates is not None:
            return self._first_layer_gates
        answer = self._get_first_layer_gates()
        self._first_layer_gates = answer
        return answer

    def _get_first_layer_gates(self) -> Dict[int, BasicGate]:
        answer = {}
        for bit_stick in self._bit2gid:
            if not bit_stick:
                # Skip if empty
                continue
            gid = bit_stick[0]
            gate = self._gates[gid]
            bit_num = gate.controls + gate.targets
            if bit_num == 2:
                a, b = gate.cargs + gate.targs
                if self._bit2gid[a][0] == self._bit2gid[b][0] and (gid not in answer):
                    answer[gid] = self._gates[gid]
            elif bit_num == 1:
                a = gate.targ
                answer[gid] = self._gates[gid]
        return answer

    def eager_exec(
        self,
        logic2phy: List[int],
        topo_graph: nx.Graph,
        physical_circ: CompositeGate = None,
    ) -> int:
        """Eagerly remove all executable gates for now.

        Args:
            logic2phy (List[int]): Current logical to physical qubit mapping.
            topo_graph (nx.Graph): Physical topology graph.
            physical_circ (CompositeGate, optional): If set, executed gates are appended to it.

        Returns:
            int: Removed (2-bit) gate number.
        """
        remove_cnt = 0
        remove_any = True
        self._reset_cache()
        while remove_any:
            remove_any = False
            for gid, gate in self._get_first_layer_gates().items():
                if gate.controls + gate.targets == 1:
                    a = gate.targ
                    _a = logic2phy[a]
                    self._bit2gid[a].pop(0)
                    remove_any = True
                    self._graph.remove_node(gid)
                    if physical_circ is not None:
                        with physical_circ:
                            gate & [_a]
                elif gate.controls + gate.targets == 2:
                    a, b = gate.cargs + gate.targs
                    assert self._bit2gid[a][0] == self._bit2gid[b][0]
                    _a, _b = logic2phy[a], logic2phy[b]
                    if topo_graph.has_edge(_a, _b):
                        self._bit2gid[a].pop(0)
                        self._bit2gid[b].pop(0)
                        remove_cnt += 1
                        remove_any = True
                        self._graph.remove_node(gid)
                        if physical_circ is not None:
                            with physical_circ:
                                gate & [_a, _b]
        self._removed_cnt += remove_cnt
        return remove_cnt

    def remained_circ(self, logic2phy: List[int]) -> CompositeGate:
        gates = {}
        for bit_stick in self._bit2gid:
            for gid in bit_stick:
                if gid not in gates:
                    gates[gid] = self._gates[gid]
        cg = CompositeGate()
        for gate in gates.values():
            args = gate.cargs + gate.targs
            args = [logic2phy[arg] for arg in args]
            with cg:
                gate & args
        return cg

    def biased_random_swap(
        self,
        topo_dist: np.ndarray,
        logic2phy: List[int],
        exclude=tuple(),
        zero_shift: float = 0.1,
    ) -> Tuple[int, int]:
        candidates = []
        weights = []

        for i in range(self._qubit_num):
            for j in range(i + 1, self._qubit_num):
                if abs(topo_dist[i][j] - 1) > 1e-6:
                    continue
                if (i, j) in exclude or (j, i) in exclude:
                    continue
                candidates.append((i, j))
                next_logic2phy = copy.copy(logic2phy)
                next_logic2phy[i], next_logic2phy[j] = (
                    next_logic2phy[j],
                    next_logic2phy[i],
                )
                bias = 0
                for gate in self.first_layer_gates.values():
                    if gate.controls + gate.targets != 2:
                        continue
                    a, b = gate.cargs + gate.targs
                    _a, _b = logic2phy[a], logic2phy[b]
                    prev_d = topo_dist[_a][_b]
                    _a, _b = next_logic2phy[a], next_logic2phy[b]
                    next_d = topo_dist[_a][_b]
                    bias += prev_d - next_d
                if abs(bias) < 1e-6:
                    bias = zero_shift
                bias = max(0, bias)
                weights.append(bias)
        assert len(candidates) > 0
        if random.random() < 0.5:
            action = random.choices(population=candidates, weights=weights, k=1)[0]
        else:
            action = random.choices(population=candidates, k=1)[0]
        return action
