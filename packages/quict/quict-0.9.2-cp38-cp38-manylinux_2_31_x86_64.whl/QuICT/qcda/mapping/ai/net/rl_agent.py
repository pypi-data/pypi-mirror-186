import copy
import math
from random import random
from typing import Tuple, Union

import torch

from QuICT.core import *
from QuICT.core.gate import *
from QuICT.qcda.mapping.ai.data_def import State, StateSlim, TrainConfig
from QuICT.qcda.mapping.ai.net.nn_mapping import NnMapping


class Agent:
    def __init__(
        self,
        config: TrainConfig,
    ) -> None:
        # Copy values in.
        self.config = config

        # Exploration related.
        self.explore_step = 0
        self.state = None  # Reset during training

        self.mapped_circ = CompositeGate()
        self._last_exec_cnt = 0
        self._last_action = None

        # Initialize policy & target network
        assert config.topo is not None
        self._qubit_num = config.topo.qubit_number

    def reset_explore_state(self):
        self.state = self.config.factory.get_one()
        # Do we need to reset counter?
        # self.explore_step = 0

    def _select_action(
        self,
        policy_net: NnMapping,
        policy_net_device: str,
    ):
        config = self.config
        a = config.action_num

        # Choose an action based on policy_net
        data = self.state.to_slim().to_nn_data()
        data = StateSlim.batch_from_list([data], policy_net_device)
        # data = self.state.circ_layered_matrices.to(policy_net_device)
        q_vec = policy_net(data.x, data.edge_index, data.batch).detach().cpu()
        q_vec = q_vec.view(a)  # [a]
        if self._last_action is not None:
            bad_action = self._last_action
            if bad_action not in config.action_id_by_swap:
                bad_action = bad_action[1], bad_action[0]
            bad_id = config.action_id_by_swap[bad_action]
            q_vec[bad_id] = 1e-12

        # Query action swap using action id
        idx = int(torch.argmax(q_vec))
        action = config.swap_by_action_id[idx]
        return action

    def select_action(
        self,
        policy_net: NnMapping,
        policy_net_device: str,
        epsilon_random: bool = False,
    ) -> Tuple[int, int]:
        """Select action based on given policy net.

        Args:
            policy_net (GnnMapping): A policy network which gives an action as output.
            policy_net_device (str): Policy net model device.
            epsilon_random (bool, optional): Whether to use epsilon-greedy strategy.
                If set True, there will be epsilon probability that this methods randomly select a viable action.
                Defaults to False.

        Returns:
            Tuple[int, int]: Selected action.
        """
        config = self.config
        eps_threshold = config.epsilon_end + (
            config.epsilon_start - config.epsilon_end
        ) * math.exp(-1.0 * self.explore_step / config.epsilon_decay)
        if epsilon_random and random() <= eps_threshold:
            return self.state.biased_random_swap(exclude=(self._last_action,))
        else:
            return self._select_action(
                policy_net=policy_net,
                policy_net_device=policy_net_device,
            )

    def count_gate_num(self) -> int:
        return self.state.circ_info.count_gate()

    def take_action(
        self, action: Tuple[int, int]
    ) -> Tuple[StateSlim, Union[StateSlim, None], float, bool]:
        """Take given action on trainer's state.

        Args:
            action (Tuple[int, int]): Swap gate used on current topology.

        Returns:
            Tuple[StateSlim, Union[StateSlim, None], float, bool]: Tuple of
                (Previous State, Next State, Reward, Terminated).
        """
        assert self.state is not None

        config = self.config
        qubit_number = config.topo.qubit_number

        prev_state = self.state.to_slim()

        self.explore_step += 1

        u, v = action
        if u == -1 and v == -1:
            next_state = prev_state
            reward = -scale * 1000
            terminated = False
            return prev_state, next_state, reward, terminated

        topo_dist = self.state.layout_info.topo_dist
        scale = config.reward_scale
        if topo_dist[u][v] < 0.01:  # not connected
            assert False

        with self.mapped_circ:
            Swap & [u, v]

        next_logic2phy = self.state.logic2phy
        next_phy2logic = self.state.phy2logic

        # Current (u, v) are physical qubit labels
        next_phy2logic[u], next_phy2logic[v] = next_phy2logic[v], next_phy2logic[u]
        lu, lv = next_phy2logic[u], next_phy2logic[v]
        next_logic2phy[lu], next_logic2phy[lv] = next_logic2phy[lv], next_logic2phy[lu]

        self.state.logic2phy = next_logic2phy
        self.state.phy2logic = next_phy2logic

        # next_circ_state = self.state.circ_info.copy()
        action_penalty = -scale / qubit_number
        reward = action_penalty
        # Execute as many as possible
        cnt = self.state.eager_exec(
            physical_circ=self.mapped_circ,
        )
        if action == self._last_action:
            reward += -1 * scale
        # If no gate is executed, avoid the same selection next time.
        self._last_action = action if cnt == 0 else None
        self._last_exec_cnt = cnt
        reward += cnt * scale

        terminated = self.state.circ_info.count_gate() == 0

        next_state = None if terminated else self.state.to_slim()

        return prev_state, next_state, reward, terminated
