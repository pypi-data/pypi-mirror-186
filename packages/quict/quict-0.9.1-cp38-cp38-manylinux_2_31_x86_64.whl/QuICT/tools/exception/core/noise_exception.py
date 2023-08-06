from QuICT.tools.exception import QuICTException


class KrausError(QuICTException):
    """ Not Kraus Matrix Error. """
    def __init__(self, msg: str = None):
        super().__init__(1012, msg)


class NoiseApplyError(QuICTException):
    """ Noise Apply Error. """
    def __init__(self, msg: str = None):
        super().__init__(1013, msg)


class PauliNoiseUnmatchedError(QuICTException):
    """ Pauli Noise operators and number qubits unmatched error. """
    def __init__(self, msg: str = None):
        super().__init__(1014, msg)


class DamplingNoiseMixedProbExceedError(QuICTException):
    """ Dampling Noise' amplitude prob and phase prob sum exceed 1. """
    def __init__(self, msg: str = None):
        super().__init__(1015, msg)
