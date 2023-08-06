from __future__ import annotations

import os.path as osp
from collections import deque
from random import randint, sample
from typing import List, Optional, Tuple, Union

import networkx as nx
import torch
from torch_geometric.data import Batch as PygBatch
from torch_geometric.data import Data as PygData

from QuICT.core import *
from QuICT.core.gate import CompositeGate, GateType
from QuICT.qcda.mapping.common.circuit_info import CircuitInfo as CircuitInfoBase
from QuICT.qcda.mapping.common.data_factory import DataFactory as DataFactoryBase
from QuICT.qcda.mapping.common.layout_info import LayoutInfo as LayoutInfoBase


class DataFactory(DataFactoryBase):
    """DataFactory is used to create random data for training."""

    def __init__(
        self, topo: Union[str, Layout], max_gate_num: int, data_dir: str = None
    ) -> None:
        if data_dir is None:
            data_dir = osp.abspath(osp.dirname(__file__))
            data_dir = osp.join(data_dir, "data")
        super().__init__(topo, max_gate_num, data_dir)

    def get_one(self) -> "State":
        topo = self._cur_topo
        qubit_num = self.topo_qubit_num_map[topo.name]
        topo_graph = self.topo_graph_map[topo.name]

        min_gn = self._max_gate_num // 3
        gate_num = randint(min_gn, max(self._max_gate_num, min_gn))
        success = False
        while not success:
            circ = Circuit(qubit_num)
            circ.random_append(
                gate_num,
                typelist=[
                    GateType.crz,
                ],
            )
            circ_state = CircuitInfo(circ=circ, max_gate_num=self._max_gate_num)
            logic2phy = [i for i in range(self.topo_qubit_num_map[topo.name])]
            circ_state.eager_exec(logic2phy=logic2phy, topo_graph=topo_graph)
            success = circ_state.count_gate() > 0

        state = State(
            circ_info=circ_state,
            layout=topo,
            logic2phy=logic2phy,
        )
        return state


class CircuitInfo(CircuitInfoBase):
    """DAG Representation of a quantum circuit. A virtual node will be
    added with label 0.
    """

    def layered_gate_matrices(self, logic2phy: List[int]) -> torch.Tensor:
        layers: List[List[Tuple[int, int]]] = []
        occupied = [-1 for _ in range(self._qubit_num)]
        for gid in sorted(self._graph.nodes):
            gate = self._gates[gid]
            a, b = gate.cargs + gate.targs
            layer_id = 1 + max(occupied[a], occupied[b])
            while len(layers) <= layer_id:
                layers.append([])
            occupied[a] = layer_id
            occupied[b] = layer_id
            _a, _b = logic2phy[a], logic2phy[b]
            layers[layer_id].append((_a, _b))
        q = self._qubit_num
        ans = torch.zeros(len(layers), q, q)
        for idx, layer in enumerate(layers):
            for u, v in layer:
                ans[idx][u][v] = 1
                ans[idx][v][u] = 1
        ans = ans.view(-1, q * q)
        return ans

    def remained_circ(self, logic2phy: List[int]) -> CompositeGate:
        gates = {}
        for bit_stick in self._bit2gid:
            for gid in bit_stick:
                if gid not in gates:
                    gates[gid] = self._gates[gid]
        cg = CompositeGate()
        for gate in gates.values():
            a, b = gate.cargs + gate.targs
            a, b = logic2phy[a], logic2phy[b]
            with cg:
                gate & [a, b]
        return cg

    def to_pyg(self, logic2phy: List[int]) -> PygData:
        """Convert current data into PyG Data according to current mapping.

        Arg:
            logic2phy (List[int]): Logical to physical qubit mapping.
            max_qubit_num (int): Padding size.

        Returns:
            PygData: PyG data.
        """
        x = torch.zeros(self._max_gate_num, 2, dtype=torch.long)
        edge_index = []
        g: nx.DiGraph = nx.convert_node_labels_to_integers(self._graph)
        assert g.number_of_nodes() > 0
        # g = self._graph
        for node in g.nodes:
            gid = g.nodes[node]["gid"]
            gate = self._gates[gid]
            args = gate.cargs + gate.targs
            if len(args) == 1:
                continue
            a, b = args
            x[node][0] = logic2phy[a] + 1
            x[node][1] = logic2phy[b] + 1
            # Add self loops
            edge_index.append([gid, gid])
        for u, v in g.edges:
            edge_index.append([u, v])
        edge_index = torch.tensor(edge_index, dtype=torch.long).T.contiguous()
        data = PygData(x=x, edge_index=edge_index)
        return data


class LayoutInfo(LayoutInfoBase):
    def __init__(self, layout: Layout) -> None:
        super().__init__(layout)


class StateSlim:
    """Intermediate state for an actor, remained only core information."""

    def __init__(
        self,
        circ_info: PygData,
        logic2phy: List[int],
        phy2logic: Optional[List[int]] = None,
    ) -> None:
        self.circ_info = circ_info
        self.logic2phy = logic2phy
        """Logical to physical mapping
        """
        q = len(logic2phy)
        self.phy2logic = phy2logic
        if self.phy2logic is None:
            self.phy2logic = [0 for _ in range(q)]
            for i in range(q):
                self.phy2logic[self.logic2phy[i]] = i

        self.logic2phy = torch.tensor(self.logic2phy)
        self.phy2logic = torch.tensor(self.phy2logic)

    def to_nn_data(self):
        return self.circ_info

    @staticmethod
    def batch_from_list(data_list: list, device: str):
        return PygBatch.from_data_list(data_list=data_list).to(device=device)

    def to_tensor_list(self) -> List[torch.Tensor]:
        return [
            self.circ_info.x,
            self.circ_info.edge_index,
            self.logic2phy,
            self.phy2logic,
        ]

    @staticmethod
    def from_tensor_list(t_list: List[torch.Tensor]) -> StateSlim:
        return StateSlim(
            circ_info=PygData(x=t_list[0], edge_index=t_list[1]),
            logic2phy=t_list[2],
            phy2logic=t_list[3],
        )


class State:
    """Intermediate state for an actor."""

    def __init__(
        self,
        circ_info: CircuitInfo,
        layout: Layout,
        logic2phy: List[int],
        phy2logic: Optional[List[int]] = None,
    ) -> None:
        self.circ_info = circ_info
        self.layout_info = LayoutInfo(layout)
        self.logic2phy = logic2phy
        """Logical to physical mapping
        """
        q = layout.qubit_number
        self.phy2logic = phy2logic
        if self.phy2logic is None:
            self.phy2logic = [0 for _ in range(q)]
            for i in range(q):
                self.phy2logic[self.logic2phy[i]] = i

        self._circ_layered_matrices = None
        self._slim = None

    @property
    def circ_layered_matrices(self) -> torch.Tensor:
        if self._circ_layered_matrices is None:
            self._circ_layered_matrices = self.circ_info.layered_gate_matrices(
                self.logic2phy
            )
        return self._circ_layered_matrices

    def remained_circ(self) -> CompositeGate:
        return self.circ_info.remained_circ(self.logic2phy)

    def biased_random_swap(self, exclude: tuple) -> Tuple[int, int]:
        return self.circ_info.biased_random_swap(
            self.layout_info.topo_dist, self.logic2phy, exclude
        )

    def eager_exec(
        self,
        physical_circ: Optional[CompositeGate] = None,
    ) -> int:
        self._slim = None
        return self.circ_info.eager_exec(
            self.logic2phy,
            self.layout_info.topo_graph,
            physical_circ,
        )

    def to_slim(self) -> StateSlim:
        if self._slim is None:
            self._slim = StateSlim(
                circ_info=self.circ_info.to_pyg(self.logic2phy),
                logic2phy=self.logic2phy,
                phy2logic=self.phy2logic,
            )
        return self._slim


class Transition:
    """States before and after certain action, together with corresponding reward."""

    def __init__(
        self,
        state: StateSlim,
        action: Tuple[int, int],
        next_state: StateSlim,
        reward: float,
    ) -> None:
        self.state = state
        self.action = action
        self.next_state = next_state
        self.reward = reward

    def __iter__(self):
        return iter((self.state, self.action, self.next_state, self.reward))


class ReplayMemory:
    """Bounded buffer of transitions."""

    def __init__(self, capacity: int) -> None:
        self._memory = deque([], maxlen=capacity)

    def push(self, transition: Transition):
        self._memory.append(transition)

    def sample(self, batch_size: int) -> List[Transition]:
        return sample(self._memory, batch_size)

    def __len__(self) -> int:
        return len(self._memory)

    def __iter__(self):
        return iter(self._memory)

    def clear(self):
        self._memory.clear()


class ValidationData:
    """Container of some circuit generated by other algorithms. Used for validation during training."""

    def __init__(
        self,
        circ: Circuit,
        topo: Layout,
        rl_mapped_circ: Union[Circuit, CompositeGate] = None,
        remained_circ: Union[Circuit, CompositeGate] = None,
    ) -> None:
        self.circ = circ
        self.rl_mapped_circ = rl_mapped_circ
        self.topo = topo
        self.remained_circ = remained_circ


class TrainConfig:
    def __init__(
        self,
        topo: Union[str, Layout],
        max_gate_num: int = 300,
        feat_dim: int = 150,
        gamma: float = 0.95,
        replay_pool_size: int = 10_000_000,
        lr: float = 0.0001,
        batch_size: int = 64,
        total_epoch: int = 2000,
        explore_period: int = 10000,
        target_update_period: int = 20,
        actor_num: int = 2,
        world_size: int = 3,
        model_sync_period: int = 10,
        memory_sync_period: int = 10,
        device: str = "cuda" if torch.cuda.is_available() else "cpu",
        model_path: str = None,
        log_dir: str = None,
        epsilon_start: float = 0.95,
        epsilon_end: float = 0.05,
        epsilon_decay: float = 5_000_000.0,
        reward_scale: float = 15.0,
        inference: bool = False,
        inference_model_dir: str = "./model",
    ) -> None:
        self.factory = DataFactory(topo=topo, max_gate_num=max_gate_num)

        self.topo = self.factory._cur_topo

        swaps = [(edge.u, edge.v) for edge in self.topo]
        swaps.sort()
        self.action_id_by_swap = {}
        self.swap_by_action_id = {}
        for idx, swap in enumerate(swaps):
            self.action_id_by_swap[swap] = idx
            self.swap_by_action_id[idx] = swap
        self.action_num = len(self.action_id_by_swap)

        self.distributed_backend = "nccl" if "cuda" in device else "gloo"

        self.max_gate_num = max_gate_num
        self.feat_dim = feat_dim
        self.gamma = gamma
        self.replay_pool_size = replay_pool_size
        self.lr = lr
        self.batch_size = batch_size
        self.total_epoch = total_epoch
        self.explore_period = explore_period
        self.target_update_period = target_update_period
        self.model_sync_period = model_sync_period
        self.memory_sync_period = memory_sync_period
        self.actor_num = actor_num
        self.world_size = world_size
        self.device = device
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.reward_scale = reward_scale
        self.inference = inference
        self.inference_model_dir = inference_model_dir

        if model_path is None:
            model_path = osp.dirname(osp.abspath(__file__))
            model_path = osp.join(model_path, f"{self.topo.name}-model_rl_mapping")
        self.model_path = model_path

        if log_dir is None:
            log_dir = osp.dirname(osp.abspath(__file__))
            log_dir = osp.join(log_dir, "torch_runs")
            log_dir = osp.join(log_dir, "rl_mapping")
        self.log_dir = log_dir
