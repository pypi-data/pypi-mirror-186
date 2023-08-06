#!/usr/bin/env python3

import asyncio as aio
from threading import Thread
from time import time

from torch.utils.tensorboard import SummaryWriter

from QuICT.qcda.mapping.ai.data_def import TrainConfig
from QuICT.qcda.mapping.ai.train.actor import Actor
from QuICT.qcda.mapping.ai.train.learner import Learner
from QuICT.tools.logger import Logger


logger = Logger("rl-mapping-trainer")


class Trainer:
    def __init__(self, config: TrainConfig) -> None:
        logger.info("Initializing trainer...")

        # Copy values in.
        self.config = config
        self.learner = Learner(config=config)
        self.actor = Actor(rank=1, config=config)
        self.actor.policy_net = self.learner._policy_net

        self._writer = SummaryWriter(log_dir=config.log_dir)

        self._loop = aio.new_event_loop()
        self._t = Thread(target=self.side_thread, daemon=True)
        self._t.start()

    def side_thread(self):
        aio.set_event_loop(self._loop)
        self._loop.run_forever()

    async def write_stat(self, running_loss: float, running_reward: float, g_step: int):
        self._writer.add_scalar(
            tag="loss",
            scalar_value=running_loss,
            global_step=g_step,
        )
        self._writer.add_scalar(
            tag="reward",
            scalar_value=running_reward,
            global_step=g_step,
        )

    def train(self):
        running_loss = 0.0
        running_reward = 0.0
        last_obs_time = time()
        observe_period = 100
        logger.info(f"Training on {self.config.device}...\n")
        g_step = 0
        for epoch_id in range(self.config.total_epoch):
            logger.info(f"Epoch {epoch_id}")

            self.actor.agent.reset_explore_state()
            for it in range(self.config.explore_period):
                reward = self.actor.explore()

                loss = self.learner.optimize_model()

                if loss is not None:
                    running_loss += loss
                    running_reward += reward

                    aio.run_coroutine_threadsafe(
                        self.write_stat(loss, reward, g_step),
                        self._loop,
                    )

                    if (it + 1) % observe_period == 0:
                        running_loss /= observe_period
                        running_reward /= observe_period
                        act_rate = observe_period / (time() - last_obs_time)
                        learn_rate = self.config.batch_size * act_rate

                        logger.info(
                            f"[{str(it+1):4s}] loss: {running_loss:0.4f}, reward: {running_reward:0.2f}\n"
                            + f"       actor : {act_rate:0.2f} action/s, learner: {learn_rate:0.2f} transition/s"
                        )

                        running_loss = 0.0
                        running_reward = 0.0
                        last_obs_time = time()

                # transfer replay buffer
                for transition in self.actor.replay:
                    self.learner.replay.push(transition)
                self.actor.replay.clear()

                # sync policy net
                self.actor.policy_net = self.learner._policy_net

                if g_step % self.config.target_update_period == 0:
                    self.learner._target_net.load_state_dict(
                        self.learner._policy_net.state_dict()
                    )
                g_step += 1

            # validate
            v_results = self.learner.validate_model()
            self.learner.show_validation_results(v_results, epoch_id)


if __name__ == "__main__":
    import sys

    assert len(sys.argv) > 1
    topo = sys.argv[1]
    device = "cuda" if len(sys.argv) == 2 else sys.argv[2]
    config = TrainConfig(topo=topo, device=device)
    trainer = Trainer(config=config)
    trainer.train()
