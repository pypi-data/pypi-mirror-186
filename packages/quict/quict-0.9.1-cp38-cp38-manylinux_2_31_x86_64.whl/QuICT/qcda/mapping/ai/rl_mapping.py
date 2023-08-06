from typing import Union

from .data_def import TrainConfig
from train.learner import Learner

from QuICT.core import *
from QuICT.core.gate import CompositeGate
from QuICT.qcda.utility import OutputAligner


class RlMapping:
    def __init__(self, layout: Layout, inference_model_path: str = "./model") -> None:
        self._config = TrainConfig(
            topo=layout, inference=True, inference_model_dir=inference_model_path
        )
        self._learner = Learner(config=self._config)

    @OutputAligner()
    def execute(
        self, circuit_like: Union[Circuit, CompositeGate]
    ) -> Union[Circuit, CompositeGate]:
        assert (
            circuit_like.width() == self._config.topo.qubit_number
        ), "Circuit and Layout must have the same qubit number!"
        cutoff = circuit_like.width() * len(circuit_like.gates)
        mapped, remained = self._learner.map_all(
            circ=circuit_like,
            layout=self._config.topo,
            policy_net=self._learner._policy_net,
            policy_net_device=self._config.device,
            cutoff=cutoff,
        )
        if len(remained.gates) > 0:
            raise Exception("Failed to map this circuit")
        return mapped
