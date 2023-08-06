from QuICT.tools.exception import QuICTException


class TypeError(QuICTException):
    """ Type Error in Core Module, including Layout, Fidelity, Qureg, ... """
    def __init__(self, locate: str, require: str, given: str):
        msg = f"{locate}'s type should be {require}, but given {given}."
        super().__init__(1001, msg)


class ValueError(QuICTException):
    def __init__(self, locate: str, require: str, given: str):
        msg = f"{locate}'s value should be {require}, but given {given}."
        super().__init__(1002, msg)


class IndexExceedError(QuICTException):
    def __init__(self, locate: str, require: str, given: str):
        msg = f"The index of {locate} should be {require}, but given {given}."
        super().__init__(1003, msg)


class QubitMeasureError(QuICTException):
    """ Qubit's Measure Error. """
    def __init__(self, msg: str = None):
        super().__init__(1010, msg)


class CheckPointNoChildError(QuICTException):
    """ The CheckPointChildren not found Error. """
    def __init__(self, msg: str = None):
        super().__init__(1011, msg)
