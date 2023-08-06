from QuICT.tools.exception import QuICTException


class CircuitAppendError(QuICTException):
    """ Circuit Append Operator Error. """
    def __init__(self, msg: str = None):
        super().__init__(1004, msg)


class CircuitReplaceError(QuICTException):
    """ Circuit Replace Gate Error. """
    def __init__(self, msg: str = None):
        super().__init__(1005, msg)


class CircuitSpecialAppendError(QuICTException):
    """ Circuit special append including Random Append and Supremacy Append. """
    def __init__(self, msg: str = None):
        super().__init__(1006, msg)


class CircuitDAGError(QuICTException):
    """ DAG Circuit Error. """
    def __init__(self, msg: str = None):
        super().__init__(1007, msg)


class CircuitDrawError(QuICTException):
    """ Circuit Draw Error. """
    def __init__(self, msg: str = None):
        super().__init__(1008, msg)


class QASMError(QuICTException):
    """ QASM Error. """
    def __init__(self, other: str = None, line: str = None, file: str = None):
        msg = "Qasm error:{} \n in line:{} \n error file:{}".format(other, line, file)
        super().__init__(1009, msg)
