from QuICT.tools.exception import QuICTException


class SampleBeforeRunError(QuICTException):
    """ Simulation sample before run error. """
    def __init__(self, msg: str):
        super().__init__(2001, msg)


class GateTypeNotImplementError(QuICTException):
    """ The given gate is not implemented in simulation. """
    def __init__(self, msg: str = None):
        super().__init__(2002, msg)


class SimulationMatrixError(QuICTException):
    """ Simulation Matrix Error"""
    def __init__(self, msg: str):
        super().__init__(2003, msg)


class StateVectorUnmatchedError(QuICTException):
    """ The State Vector is not matched the simulation. """
    def __init__(self, msg: str):
        super().__init__(2004, msg)


class GateAlgorithmNotImplementError(QuICTException):
    """ The algorithm of simulate quantum gate is not implemented. """
    def __init__(self, msg: str = None):
        super().__init__(2005, msg)


class UnitaryMatrixUnmatchedError(QuICTException):
    """ The State Vector is not matched the simulation. """
    def __init__(self, msg: str):
        super().__init__(2006, msg)


class SimulatorOptionsUnmatchedError(QuICTException):
    """ The backend and optional arguments is not matched in the simulation. """
    def __init__(self, msg: str):
        super().__init__(2007, msg)
