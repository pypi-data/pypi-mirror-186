from typing import Union, List


class Operator:
    """ The SuperClass of all the operator. """
    @property
    def targets(self):
        return self._targets

    @property
    def targs(self):
        return self._targs

    @property
    def cargs(self):
        return []

    @targs.setter
    def targs(self, targets: Union[List, int]):
        assert isinstance(targets, (int, list))
        if isinstance(targets, int):
            self._targs = [targets]
        else:
            self._targs = targets

    @property
    def targ(self):
        return self._targs[0]

    def __init__(
        self,
        targets: int
    ):
        """
        Args:
            targets (int): the number of the target bits of the gate
        """
        assert targets >= 0 and isinstance(targets, int), f"targets must be a positive integer, not {type(targets)}"
        self._targets = targets
        self._targs = []

    def __and__(self, targets: Union[List[int], int],):
        """ Assigned the trigger's target qubits.

        Args:
            targets (Union[List[int], int]): The indexes of target qubits.
        """
        if isinstance(targets, int):
            assert targets >= 0 and self.targets == 1
            self._targs = [targets]
        elif isinstance(targets, list):
            assert len(targets) == self.targets
            for q in targets:
                assert q >= 0 and isinstance(q, int), f"targets must be a positive integer, not {q}"

            self._targs = targets
        else:
            raise TypeError(f"qubits must be one of [List[int], int], not {type(targets)}")

        return self

    def __or__(self, targets):
        """ Append the trigger to the circuit.

        Args:
            targets (Circuit): The circuit which contains the trigger.
        """
        try:
            targets.append(self)
        except Exception as e:
            raise TypeError(f"Failure to append Trigger to targets, due to {e}")
