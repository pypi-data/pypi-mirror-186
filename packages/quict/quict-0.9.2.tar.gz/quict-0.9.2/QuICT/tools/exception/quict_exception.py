ERROR_CODE = {
    # Error code table for the QuICT system.
    1000: "QuICT Exception",
    # 1001-1999: QuICT Core Module Exception
    1001: "QuICT Core Module Type Exception",
    1002: "QuICT Core Module Value Exception",
    1003: "QuICT Core Module Index Exceed Exception",
    1004: "QuICT Circuit Append Operator Exception",
    1005: "QuICT Circuit Replace Operator Exception",
    1006: "QuICT Circuit Random or Supremacy Append Exception",
    1007: "QuICT DAG Circuit Exception",
    1008: "QuICT Circuit Draw Exception",
    1009: "QuICT QASM Exception",
    1010: "QuICT Qubit Measure Exception",
    1011: "QuICT CheckPointChildren no Find Exception",
    1012: "QuICT Noise Kraus Matrix Exception",
    1013: "QuICT Noise Apply Exception",
    1014: "QuICT Noise Pauli Operators Unmatched Exception",
    1015: "QuICT Noise Dampling Prob Exceed Exception",
    1016: "QuICT Gate Qubit Assigned Exception",
    1017: "QuICT Gate Parameter Exception",
    1018: "QuICT Gate Append Exception",
    1019: "QuICT Gate Matrix Exception",
    1020: "QuICT CompositeGate Append Exception",

    # 2000-2999: QuICT Simulation Module Exception
    2001: "QuICT Simulation Sample before Run Exception",
    2002: "QuICT Simulation Gate not Implement Exception",
    2003: "QuICT Simulation Matrix Exception",
    2004: "QuICT Simulation State Vector unmatched Exception",
    2005: "QuICT Simulation Gate Algorithm not Implement Exception",
    2006: "QuICT Simulation Unitary Matrix Unmatched Exception",
    2007: "QuICT Simulation Options Unmatched Exception",

    # 3000-3999: QuICT Algorithm Module Exception

    # 4000-4999: QuICT QCDA Module Exception

    # 9000-9999: QuICT Utility Module Exception

}


class QuICTException(Exception):
    """The base exception class for QuICT.

    Args:
        error_code (int): the predefined QuICT error code.
        msg (str): the description of the error. If is None, which will
        show the base error information.
    """

    def __init__(self, error_code: int = 1000, msg: str = None):
        self.ecode = error_code
        self.strerror = msg if msg else ERROR_CODE[self.ecode]
        if not isinstance(self.strerror, str):
            self.strerror = str(msg)

    def __str__(self):
        return self.strerror

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self)})"
