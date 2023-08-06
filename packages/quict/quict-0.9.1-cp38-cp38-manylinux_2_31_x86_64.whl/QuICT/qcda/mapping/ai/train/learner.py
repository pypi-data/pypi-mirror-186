import os
import os.path as osp
import re
from typing import Dict, List, Tuple, Union

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

from QuICT.core import *
from QuICT.core.gate.composite_gate import CompositeGate
from QuICT.qcda.mapping.ai.data_def import CircuitInfo, ReplayMemory, State, StateSlim, TrainConfig, ValidationData
from QuICT.qcda.mapping.ai.net.nn_mapping import NnMapping
from QuICT.qcda.mapping.ai.net.rl_agent import Agent
from QuICT.tools.interface import OPENQASMInterface
from QuICT.tools.logger import Logger

logger = Logger("rl-mapping-learner")


def _wrap2circ(cg_or_circ: Union[Circuit, CompositeGate] = None):
    if cg_or_circ is None:
        return None
    elif isinstance(cg_or_circ, Circuit):
        return cg_or_circ
    elif isinstance(cg_or_circ, CompositeGate):
        circ = Circuit(cg_or_circ.width())
        circ.extend(cg_or_circ.gates)
        return circ
    else:
        raise TypeError("Only supports Circuit/CompositeGate")


class Learner:
    def __init__(self, config: TrainConfig) -> None:
        self.config = config

        if config.inference:
            logger.info("Preparing policy network...")
            try:
                model_path = config.inference_model_dir
                model_path = osp.join(model_path, f"{config.topo.name}.pt")
                self._policy_net = NnMapping(
                    qubit_num=config.topo.qubit_number,
                    max_gate_num=config.max_gate_num,
                    feat_dim=config.feat_dim,
                    action_num=config.action_num,
                    device=config.device,
                )
                states = torch.load(model_path)
                self._policy_net.load_state_dict(states)
                self._policy_net = self._policy_net.to(device=config.device)
                self._policy_net.train(not config.inference)
            except:
                raise Exception("Cannot load model for " + model_path)
        elif not config.inference:
            logger.info("Preparing policy network...")
            self._policy_net = NnMapping(
                qubit_num=config.topo.qubit_number,
                max_gate_num=config.max_gate_num,
                feat_dim=config.feat_dim,
                action_num=config.action_num,
                device=config.device,
            ).to(device=config.device)
            self._policy_net.train(not config.inference)
            logger.info("Preparing target network...")
            self._target_net = NnMapping(
                qubit_num=config.topo.qubit_number,
                max_gate_num=config.max_gate_num,
                feat_dim=config.feat_dim,
                action_num=config.action_num,
                device=config.device,
            ).to(device=config.device)
            self._target_net.train(config.inference)
            # Guarantee they have the same parameter values.
            self._target_net.load_state_dict(self._policy_net.state_dict())

            logger.info("Preparing experience pool...")
            self.replay = ReplayMemory(config.replay_pool_size)

            # Loss function & optimizer
            self._smooth_l1 = nn.SmoothL1Loss()
            self._optimizer = optim.RMSprop(
                self._policy_net.parameters(),
                lr=self.config.lr,
            )

            # Prepare path to save model files during training
            logger.info("Preparing model saving directory...")
            if not osp.exists(config.model_path):
                os.makedirs(config.model_path)
            self._model_path = config.model_path

            # Prepare summary writer and its logging directory
            if not osp.exists(config.log_dir):
                os.makedirs(config.log_dir)
            self._writer = SummaryWriter(log_dir=config.log_dir)

            # Validation circuits
            logger.info("Preparing validation data...")
            self._v_data: List[ValidationData] = []
            self._mcts_num: Dict[str, int] = {}
            self._load_v_data()

            # best so far
            self._v_best_score = 1e9

    def _load_v_data(self):
        v_data_dir = osp.join(self.config.factory._data_dir, "v_data")
        pattern = re.compile(r"(\w+)_(\d+).qasm")
        for _, _, file_names in os.walk(v_data_dir):
            for file_name in file_names:
                if file_name.startswith("mapped"):
                    continue

                file_path = osp.join(v_data_dir, file_name)
                # mapped_file_path = osp.join(v_data_dir, f"mapped_{file_name}")
                groups = pattern.match(file_name)
                topo_name = groups[1]
                if topo_name != self.config.topo.name:
                    continue
                topo = self.config.factory.topo_map[topo_name]
                circ = OPENQASMInterface.load_file(file_path).circuit
                # mcts_mapped_circ = OPENQASMInterface.load_file(mapped_file_path).circuit
                self._v_data.append(
                    ValidationData(
                        circ=circ,
                        topo=topo,
                    )
                )
        self._v_data.sort(key=lambda x: len(x.circ.gates))

    def map_all(
        self,
        circ: Union[Circuit, CompositeGate],
        layout: Layout,
        policy_net: NnMapping,
        policy_net_device: str,
        cutoff: int = None,
    ) -> Tuple[CompositeGate, CompositeGate]:
        """Map given circuit to topology layout. Note that this methods will change internal exploration state.

        Args:
            circ (CircuitBased): Circuit to be mapped.
            layout (Layout): Topology layout.
            policy_net (GnnMapping): Policy network.
            policy_net_device (str): Policy network device.
            cutoff (int, optional): The maximal steps of execution. If the policy network cannot
                stop with in `cutoff` steps, force it to early stop. Defaults to None.

        Returns:
            Tuple[CompositeGate, CompositeGate]: Mapped circuit, remained circuit.
        """
        logic2phy = [i for i in range(layout.qubit_number)]
        agent = Agent(config=self.config)
        topo_graph = self.config.factory.get_topo_graph(topo=layout)
        circ_state = CircuitInfo(circ=circ, max_gate_num=policy_net._max_gate_num)

        circ_state.eager_exec(
            logic2phy=logic2phy, topo_graph=topo_graph, physical_circ=agent.mapped_circ
        )
        agent.state = State(
            circ_info=circ_state,
            layout=layout,
            logic2phy=logic2phy,
        )

        terminated = circ_state.count_gate() == 0
        step = 0
        with torch.no_grad():
            while not terminated:
                action = agent.select_action(
                    policy_net=policy_net,
                    policy_net_device=policy_net_device,
                )
                _, _, _, terminated = agent.take_action(action=action)
                step += 1
                if cutoff is not None and step >= cutoff:
                    break
            return agent.mapped_circ, agent.state.remained_circ()

    def validate_model(self) -> List[ValidationData]:
        """Map all validation circuits to corresponding topologies.

        Returns:
            List[ValidationData]: Multiple instances.
        """
        for v_datum in self._v_data:
            cutoff = len(v_datum.circ.gates) * v_datum.circ.width()
            result_circ, remained_circ = self.map_all(
                max_gate_num=self.config.max_gate_num,
                circ=v_datum.circ,
                layout=v_datum.topo,
                policy_net=self._target_net,
                policy_net_device=self.config.device,
                cutoff=cutoff,
            )
            v_datum.rl_mapped_circ = _wrap2circ(result_circ)
            v_datum.remained_circ = _wrap2circ(remained_circ)
        return self._v_data

    def optimize_model(self) -> Union[None, float]:
        if len(self.replay) < self.config.batch_size:
            print(
                f"Experience pool is too small({len(self.replay):2}). Keep exploring..."
            )
            return None
        transitions = self.replay.sample(self.config.batch_size)
        states, actions, next_states, rewards = zip(*transitions)

        actions = torch.tensor(
            [[self.config.action_id_by_swap[action]] for action in actions],
            dtype=torch.long,
            device=self.config.device,
        )  # [B, 1]

        rewards = torch.tensor(rewards, device=self.config.device)

        data_list = [state.to_nn_data() for state in states]
        data_batch = StateSlim.batch_from_list(
            data_list=data_list, device=self.config.device
        )

        # Current Q estimation
        q_vec = self._policy_net(
            data_batch.x,
            data_batch.edge_index,
            data_batch.batch,
        )  # [b, a_gn + a_gs]
        state_action_values = q_vec.gather(1, actions).squeeze()

        # Q* by Bellman Equation
        non_final_mask = torch.tensor(
            tuple(map(lambda s: s is not None, next_states)),
            device=self.config.device,
            dtype=torch.bool,
        )
        non_final_data_list = [
            state.to_nn_data() for state in next_states if state is not None
        ]
        non_final_data_batch = StateSlim.batch_from_list(
            data_list=non_final_data_list, device=self.config.device
        )

        #
        # Use normal DQN
        #
        next_state_values = torch.zeros(
            self.config.batch_size, device=self.config.device
        )
        next_state_values[non_final_mask] = (
            self._target_net(
                non_final_data_batch.x,
                non_final_data_batch.edge_index,
                non_final_data_batch.batch,
            )  # [b, a]
            .clone()
            .detach()
            .max(1)[0]
        )

        expected_state_action_values = (next_state_values * self.config.gamma) + rewards

        loss = self._smooth_l1(state_action_values, expected_state_action_values)

        self._optimizer.zero_grad()
        loss.backward()
        loss_val = loss.item()
        self._optimizer.step()
        return loss_val

    def show_validation_results(self, results: List[ValidationData], epoch_id: int):
        logger.info("[Validation Summary]")
        rl_num = {}
        original_num = {}
        for v_datum in results:
            topo_name = v_datum.topo.name
            rl_num[topo_name] = 0
            original_num[topo_name] = 0
        for idx, v_datum in enumerate(results):
            topo_name = v_datum.topo.name
            _rl_num = len(v_datum.rl_mapped_circ.gates)
            _original_num = len(v_datum.circ.gates)
            rl_num[topo_name] += _rl_num
            original_num[topo_name] += _original_num
            print(
                f"    #Gate in circuit: {_original_num}, #Gate by RL: {_rl_num} ({topo_name})"
            )
        if rl_num[topo_name] < self._v_best_score:
            self._v_best_score = rl_num[topo_name]
            if epoch_id > 5:
                torch.save(
                    self._target_net.state_dict(),
                    osp.join(self._model_path, f"model_epoch_{epoch_id}.pt"),
                )
        self._writer.add_scalars(
            f"Validation Performance ({topo_name})",
            {
                "#Gate in circuit": original_num[topo_name],
                "#Gate by RL": rl_num[topo_name],
                "#Gate by RL (best)": self._v_best_score,
            },
            epoch_id + 1,
        )
        logger.info()
