from typing import Tuple, Union, List, Dict
from types import FunctionType

from ._operator import Operator
from QuICT.core.gate import CompositeGate, BasicGate
from QuICT.tools.exception.core import TypeError, ValueError


class Trigger(Operator):
    """
    The trigger for switch the dynamic circuit; contains the target qubits and
    related circuits with different state.
    """
    def __init__(
        self,
        targets: int,
        state_gate_mapping: Union[Dict[int, CompositeGate], List[CompositeGate], Tuple[CompositeGate], FunctionType]
    ):
        """
        Args:
            targets (int): The number of target qubits.
            state_gate_mapping: The mapping of state and related composite gates.
                (Union[Dict[int, CompositeGate], List[CompositeGate], Tuple[CompositeGate], FunctionType])

        Raises:
            TypeError: Error input parameters.
        """
        super().__init__(targets=targets)

        # Deal with state - compositegate mapping
        self._state_gate_mapping = {}
        if isinstance(state_gate_mapping, (list, tuple)):
            for idx, cgate in enumerate(state_gate_mapping):
                assert isinstance(cgate, (CompositeGate, BasicGate, type(None))), TypeError(
                    "Trigger.state_gate_mapping:list", "list/tuple<CompositeGate, BasicGate>", type(cgate)
                )
                self._state_gate_mapping[idx] = cgate
        elif isinstance(state_gate_mapping, dict):
            for key, value in state_gate_mapping.items():
                assert isinstance(key, int) and isinstance(value, (CompositeGate, BasicGate, type(None))), \
                    TypeError(
                        "Trigger.state_gate_mapping:dict",
                        "dict<int, CompositeGate/BasicGate/None>",
                        f"{type(key)}, {type(value)}")

            self._state_gate_mapping = state_gate_mapping
        elif isinstance(state_gate_mapping, FunctionType):
            self._check_function_validation(state_gate_mapping)
            self._state_gate_mapping = state_gate_mapping
        else:
            raise TypeError("Trigger.state_gate_mapping", "[list, dict, Function]", {type(state_gate_mapping)})

    def mapping(self, state: int) -> CompositeGate:
        """ Return the related composite gate with given qubits' measured state.

        Args:
            state (int): The qubits' measured state.

        Returns:
            CompositeGate: The related composite gate.
        """
        assert state >= 0 and state < 2 ** self.targets, ValueError(
            "Trigger.mapping.state", f"[0, {2**self.targets}]", state
        )

        if isinstance(self._state_gate_mapping, FunctionType):
            return self._state_gate_mapping(state)
        else:
            return self._state_gate_mapping[state]

    def _check_function_validation(self, state_gate_mapping):
        """ Validation the correctness of given state-composite mapping function. """
        for i in range(2 ** self.targets):
            if not isinstance(state_gate_mapping(i), (CompositeGate, BasicGate, type(None))):
                raise TypeError(
                    "Trigger.state_gate_mapping:callable",
                    "Return(CompositeGate/BasicGate/None)",
                    type(state_gate_mapping(i))
                )
