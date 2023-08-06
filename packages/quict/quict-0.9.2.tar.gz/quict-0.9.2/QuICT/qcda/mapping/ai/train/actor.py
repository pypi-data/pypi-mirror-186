from ..data_def import ReplayMemory, TrainConfig, Transition
from ..net.rl_agent import Agent


class Actor:
    def __init__(self, rank: int, config: TrainConfig):
        self.rank = rank
        self.config = config
        self.agent = Agent(config=config)
        self.policy_net = None
        self.replay = ReplayMemory(capacity=config.memory_sync_period)

    def explore(self):
        action = self.agent.select_action(
            policy_net=self.policy_net,
            policy_net_device=self.config.device,
            epsilon_random=True,
        )

        prev_state, next_state, reward, terminated = self.agent.take_action(
            action=action
        )

        if terminated:
            next_state = None
            self.agent.reset_explore_state()

        self.replay.push(
            Transition(
                state=prev_state,
                action=action,
                next_state=next_state,
                reward=reward,
            )
        )

        return reward
