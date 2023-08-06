from typing import Tuple

from QuICT.core import *
from QuICT.core.gate import CompositeGate
from QuICT.core.gate.gate import BasicGate

from ..common import LayoutInfo
from ..common.circuit_info import CircuitInfo
from .mcts_tree_node import MCTSTreeNode


class MCTSTree:
    def __init__(
        self,
        circuit_info: CircuitInfo,
        layout_info: LayoutInfo,
        bp_num: int,
        sim_cnt: int,
        sim_gate_num: int,
        gamma: float,
        epsilon: float,
        c: float,
    ) -> None:
        self._root = MCTSTreeNode(
            circuit_info=circuit_info,
            layout_info=layout_info,
        )
        self._layout_info = layout_info

        self._bp_num = bp_num
        self._sim_cnt = sim_cnt
        self._sim_gate_num = sim_gate_num
        self._c = c
        self._gamma = gamma
        self._epsilon = epsilon

    def step(self) -> Tuple[Tuple[int, int], CompositeGate, bool]:
        """Execute multiple search rounds.
        Return a swap selection and update current search tree root.

        Returns:
            Tuple[Tuple[int, int], bool]: Selected swap action, whether mapping ends.
        """
        for _ in range(self._bp_num):
            cur = self._root
            while len(cur.children) > 0:
                cur = cur.select_child(self._c)
            if cur.is_terminated_node():
                break
            cur.expand()
            for leaf in cur.children.values():
                leaf.simulate(
                    sim_cnt=self._sim_cnt,
                    sim_gate_num=self._sim_gate_num,
                    gamma=self._gamma,
                    epsilon=self._epsilon,
                )
                leaf.back_propagate(self._gamma)
        action, self._root, terminated = self._root.best_child()
        assert self._layout_info.topo_graph.has_edge(*action), "Illegal action!"
        for gate in self._root.executed_circ.gates:
            gate: BasicGate
            if gate.controls + gate.targets == 1:
                continue
            a, b = gate.cargs + gate.targs
            assert self._layout_info.topo_graph.has_edge(
                a, b
            ), "Wrong executed circuit!"
        return action, self._root.executed_circ, terminated
