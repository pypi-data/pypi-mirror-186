from typing import List

from ._operator import Operator
from QuICT.core.utils import unique_id_generator
from QuICT.tools.exception.core import TypeError, CheckPointNoChildError


class CheckPoint(Operator):
    """ The CheckPoint is a sign of the circuit, the Composite Gate with the related
    CheckPointChild will be add into the sign indexes of the circuit.

    Example:
        Use the syntax "CheckPoint | Circuit" to add a CheckPointChild into the Circuit.
        A circuit may have more than one CheckPoints.
    """
    @property
    def uid(self):
        """ Unique Identity Number. Used for mapping CheckPoint and CheckPointChild. """
        return self._uid

    @property
    def position(self):
        """ The related index in the circuit. """
        return self._pos

    @position.setter
    def position(self, shift: int):
        """ Set the related index of the circuit. """
        assert isinstance(shift, int), TypeError("CheckPoint.position.shift", "int", type(shift))
        self._pos += shift

    def __init__(self):
        super().__init__(targets=1)
        self._uid = unique_id_generator()
        self._pos = -1

    def get_child(self, shift: int = 0):
        """ Generate its CheckPointChild, which has the same uid. """
        assert isinstance(shift, int), TypeError("CheckPoint.get_child.shift", "int", type(shift))
        return CheckPointChild(self.uid, shift)

    def match(self, uid: str) -> bool:
        """ Comparsion the uid with self. """
        return uid == self._uid

    def __or__(self, targets):
        """ Add CheckPoint into circuit, and set position to be the end of current circuit. """
        super().__or__(targets)
        self._pos = targets.size()


class CheckPointChild(Operator):
    """ The child for CheckPoint, used with the CompositGate. The purpose of the CheckPointChild is
    to add CompositeGate into the target index of the circuit.

    Example:
        Use the syntax "CheckPointChild | CompositeGate" to add a CheckPointChild into the CompositeGate.
    """
    @property
    def uid(self):
        """ Unique identity number. Used for mapping CheckPoint and CheckPointChild. """
        return self._uid

    @property
    def shift(self) -> int:
        """ The shift distance of the CheckPoint position. """
        return self._shift

    def __init__(self, uid: str, shift: int = 0):
        """ Initial a CheckPointChild.

        Args:
            uid (str): The unique identity number, same with its CheckPoint.
            shift (int, optional): The shift distance of the CheckPoint position. Defaults to 0.
        """
        super().__init__(targets=1)
        self._uid = uid
        self._shift = shift

    def find_position(self, checkpoints: List[CheckPoint]) -> int:
        """ return the position of the mappin CheckPoint. """
        pos = -1
        for cp in checkpoints:
            if cp.match(self._uid):
                pos = cp.position
                cp.position = self._shift

        if pos == -1:
            raise CheckPointNoChildError("Cannot find parent checkpoint for current checkpointchild.")

        return pos
