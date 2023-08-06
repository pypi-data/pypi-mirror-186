from ._operator import Operator


class Multiply(Operator):
    def __init__(self, value):
        super().__init__(targets=1)
        self._value = value

    @property
    def value(self):
        return self._value

    def qasm(self):
        return f"{self._value}"


class SpecialGate(Operator):
    @property
    def proxy_idx(self):
        return self._proxy_idx

    @property
    def type(self):
        return self._type

    def __init__(self, type, targ: list, proxy_idx: int = -1):
        super().__init__(targets=1)
        self._type = type
        self._proxy_idx = proxy_idx
        self.targs = targ

    def qasm(self):
        return f"{self._type}, {self.targs}, {self._proxy_idx}."

    def __str__(self):
        return f"{self._type}, {self.targs}, {self._proxy_idx}."
