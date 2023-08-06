from QuICT.core.gate import CompositeGate, CX, CH, X, H
from QuICT.core.gate.backend import MCTOneAux


class OracleInfo:
    def __init__(
        self,
        n: int,
        n_ancilla: int,
        S_chi,
        is_good_state,
        custom_grover_operator=None,
    ) -> None:
        """Oracle information.

        Args:
            n (int): oracle space width.
            n_ancilla (int, optional): ancilla width.
            S_chi (function, optional): a function,\
                input of which is (n:int),\
                output of which is the target phase-flip circuit of width n.
            is_good_state (function, optional): a function,\
                input of which is (s:String),\
                output of which is whether the bit string s is a good state.
            custom_grover_operator (CompositeGate, optional): user-defined Grover operator. Defaults to None.
        """
        self.n = n
        self.n_ancilla = n_ancilla
        self.S_chi = S_chi
        self.is_good_state = is_good_state
        self.custom_grover_operator = custom_grover_operator


def default_A(n, controlled=False):
    # control on 0
    cgate = CompositeGate()
    if controlled:
        for i in range(1, 1 + n):
            CH | cgate([0, i])
    else:
        for i in range(n):
            H | cgate(i)
    return cgate


def default_A_dagger(n, controlled=False):
    return default_A(n, controlled)


def default_S_0(n, controlled=False):
    # control on 0
    cgate = CompositeGate()
    if controlled:
        indices = list(range(1, 1 + n))
        for i in indices:
            CX | cgate([0, i])
        CH | cgate([0, indices[n - 1]])
        MCTOneAux().execute(n + 2) | cgate
        CH | cgate([0, indices[n - 1]])
        for i in indices:
            CX | cgate([0, i])
    else:
        for i in range(n):
            X | cgate(i)
        H | cgate(n - 1)
        MCTOneAux().execute(n + 1) | cgate
        H | cgate(n - 1)
        for i in range(n):
            X | cgate(i)
    return cgate


class StatePreparationInfo:
    def __init__(self, n: int, n_ancilla=0, A=default_A, A_dagger=default_A_dagger) -> None:
        """state preparation information.

        Args:
            n (int): state preparation circuit width.
            n_ancilla (int, optional): ancilla width. Defaults to 0.
            A (function, optional): a function that has same input/output as default_A. Defaults to default_A.
            A_dagger (function, optional): a function that has same input/output as default_A_dagger,\
                and it should be consistent with A. Defaults to default_A_dagger.
        """
        self.n = n
        self.n_ancilla = n_ancilla
        self.A = A
        self.A_dagger = A_dagger
        self.S_0 = default_S_0
