from QuICT.simulation.state_vector import CircuitSimulator

from .backend.canonical_QAE import amplitude_estimate as canonical_run
from .backend.max_likely_QAE import amplitude_estimate as max_likely_run
from .backend.FQAE import amplitude_estimate as fast_run
from .backend.canonical_QAE import construct_circuit as canonical_circuit
from .utility import StatePreparationInfo, OracleInfo


class QAE:
    _ALLOWED_MODES = {"canonical", "fast", "max_likely"}
    _RUN_METHOD_OF_MODE = {
        "canonical": canonical_run,
        "fast": fast_run,
        "max_likely": max_likely_run,
    }
    _CIRCUIT_METHOD_OF_MODE = {"canonical": canonical_circuit}

    def __init__(self, mode, eps=0.1, simulator=CircuitSimulator(),) -> None:
        """set up QAE algorithm parameters. mode=="canonical" is not suggested for use\
        due to lower success rate than theoretical expectation

        Args:
            mode (string): _description_
            eps (float, optional): _description_. Defaults to 0.1.
            simulator (_type_, optional): _description_. Defaults to CircuitSimulator().
        """
        if mode not in QAE._ALLOWED_MODES:
            raise ValueError(f"allowed mode are {QAE._ALLOWED_MODES}.")
        self.mode = mode
        self.eps = eps
        self.simulator = simulator

    def run(
        self,
        oracle: OracleInfo,
        state_preparation: StatePreparationInfo = None,
    ):
        if self.mode not in QAE._RUN_METHOD_OF_MODE:
            raise ValueError(f"mode {self.mode} does not support run method.")
        if state_preparation is None:
            state_preparation = StatePreparationInfo(n=oracle.n)
        assert state_preparation.n == oracle.n
        return QAE._RUN_METHOD_OF_MODE[self.mode](
            eps=self.eps,
            oracle=oracle,
            state_preparation=state_preparation,
            simulator=self.simulator,
        )

    def circuit(
        self,
        oracle: OracleInfo,
        state_preparation: StatePreparationInfo = None,
    ):
        if self.mode not in QAE._CIRCUIT_METHOD_OF_MODE:
            raise ValueError(f"mode {self.mode} does not support circuit method.")
        if state_preparation is None:
            state_preparation = StatePreparationInfo(n=oracle.n)
        assert state_preparation.n == oracle.n
        return QAE._CIRCUIT_METHOD_OF_MODE[self.mode](
            eps=self.eps,
            oracle=oracle,
            state_preparation=state_preparation
        )
