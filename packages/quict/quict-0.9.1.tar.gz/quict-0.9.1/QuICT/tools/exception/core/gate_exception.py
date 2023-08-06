from QuICT.tools.exception import QuICTException


class GateQubitAssignedError(QuICTException):
    """ Gate's qubit assign Error. """
    def __init__(self, msg: str = None):
        super().__init__(1016, msg)


class GateParametersAssignedError(QuICTException):
    """ Gate's Parameter Error. """
    def __init__(self, msg: str = None):
        super().__init__(1017, msg)


class GateAppendError(QuICTException):
    """ BasicGate append error. """
    def __init__(self, msg: str = None):
        super().__init__(1018, msg)


class GateMatrixError(QuICTException):
    """ BasicGate matrix error. """
    def __init__(self, msg: str = None):
        super().__init__(1019, msg)


class CompositeGateAppendError(QuICTException):
    """ CompositeGate append error. """
    def __init__(self, msg: str = None):
        super().__init__(1020, msg)
