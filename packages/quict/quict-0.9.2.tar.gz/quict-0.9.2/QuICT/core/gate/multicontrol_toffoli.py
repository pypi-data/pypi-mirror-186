from .backend.mct import *
from QuICT.core.gate import CompositeGate, X, CX, CCX
from QuICT.tools.exception.core import TypeError, ValueError


class MultiControlToffoli(object):
    """
    Divided by the usages of auxiliary qubits, here are 4 implementations of multi-control Toffoli gates.
    """
    __AUX_USAGES = ['no_aux', 'one_clean_aux', 'one_dirty_aux', 'half_dirty_aux']

    def __init__(self, aux_usage='no_aux'):
        """
        Args:
            aux_usage(str): 4 different usages of auxiliary qubits could be chosen, as listed
                'no_aux': No auxiliary qubits are used
                'one_clean_aux': 1 clean auxiliary qubit is used
                'one_dirty_aux': 1 dirty auxiliary qubit is used
                'half_dirty_aux': more than half of all qubits are used as auxiliary qubits, which could be dirty
        """
        assert aux_usage in self.__AUX_USAGES, TypeError("MultiControlToffoli.aux_usage", self.__AUX_USAGES, aux_usage)

        self.aux_usage = aux_usage

    def __call__(self, control, aux=0):
        """
        By default, the qubit arrangement would be control qubits, target qubit, auxiliary qubits (if exists)

        Args:
            control(int): the number of control qubits
            aux(int, optional): only works when 'half_dirty_aux' is chosen, the number of auxiliary qubits

        Returns:
            CompositeGate: the mct gates
        """
        # Special cases, no MCT would be executed.
        if control == 0:
            gates = CompositeGate()
            X & 0 | gates
            return gates
        if control == 1:
            gates = CompositeGate()
            CX & [0, 1] | gates
            return gates
        if control == 2:
            gates = CompositeGate()
            CCX & [0, 1, 2] | gates
            return gates

        # Otherwise
        if self.aux_usage == 'no_aux':
            return MCTWithoutAux().execute(control + 1)
        elif self.aux_usage == 'one_clean_aux':
            return MCTOneAux().execute(control + 2)
        elif self.aux_usage == 'one_dirty_aux':
            return MCTLinearOneDirtyAux().execute(control + 2)
        else:
            qubit = control + aux + 1
            if control > (qubit // 2) + (1 if qubit % 2 == 1 else 0):
                raise ValueError("MultiControlToffoli.control", f"<= ceil({qubit}/2)", control)
            controls = [i for i in range(control)]
            auxs = [i for i in range(control + 1, qubit)]
            return MCTLinearHalfDirtyAux.assign_qubits(qubit, control, controls, auxs, control)
