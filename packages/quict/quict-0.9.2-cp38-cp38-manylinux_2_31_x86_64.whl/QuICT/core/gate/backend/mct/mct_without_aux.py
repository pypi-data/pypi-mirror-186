import numpy as np

from QuICT.core.gate import CompositeGate, H, X, CX, CU1


class MCTWithoutAux(object):
    """
    Decomposition of n-qubit Toffoli gates with no ancillary qubit

    Reference:
        https://arxiv.org/abs/1303.3557
    """
    def execute(self, n):
        """
        Args:
            n(int): the number of qubits, be aware that n means (n-1)-control NOT

        Returns:
            CompositeGate: the n-qubit Toffoli gate
        """
        gates = CompositeGate()
        if n == 1:
            X & 0 | gates
            return gates

        if n == 2:
            CX & [0, 1] | gates
            return gates

        for control in range(n - 2, 0, -1):
            for target in range(control + 1, n):
                if target == control + 1:
                    H & target | gates
                angle = np.pi / (2 ** (target - control))
                CU1(angle) & [control, target] | gates

        H & 1 | gates
        for target in range(1, n):
            angle = np.pi / (2 ** (target - 1))
            CU1(angle) & [0, target] | gates
        H & 1 | gates

        for control in range(1, n - 1, 1):
            for target in range(control + 1, n):
                angle = -np.pi / (2 ** (target - control))
                CU1(angle) & [control, target] | gates
                if target == control + 1:
                    H & target | gates

        for control in range(n - 3, 0, -1):
            for target in range(control + 1, n - 1):
                if target == control + 1:
                    H & target | gates
                angle = np.pi / (2 ** (target - control))
                CU1(angle) & [control, target] | gates

        H & 1 | gates
        for target in range(1, n - 1):
            angle = -np.pi / (2 ** (target - 1))
            CU1(angle) & [0, target] | gates
        H & 1 | gates

        for control in range(1, n - 2, 1):
            for target in range(control + 1, n - 1):
                angle = -np.pi / (2 ** (target - control))
                CU1(angle) & [control, target] | gates
                if target == control + 1:
                    H & target | gates

        return gates
