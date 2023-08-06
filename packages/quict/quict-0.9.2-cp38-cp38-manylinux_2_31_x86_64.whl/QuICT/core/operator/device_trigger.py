from typing import Dict

from QuICT.core.gate import CompositeGate
from ._operator import Operator


class DeviceTrigger(Operator):
    """ The mapping of Quantum gates and device id. """
    def __init__(
        self,
        device_gate_mapping: Dict[int, CompositeGate]
    ):
        """
        Args:
            targets (int): The number of target qubits.
            device_gate_mapping (Dict[int, CompositeGate]): The mapping of device and related composite gates.

        Raises:
            TypeError: Error input parameters.
        """
        super().__init__(targets=1)
        self._dev_to_gate = device_gate_mapping

    def __str__(self):
        totals = ""
        for k, v in self._dev_to_gate.items():
            string = str(k) + ": "
            for gate in v.gates:
                string += gate.qasm()

            totals += string + "\n"

        return totals

    def mapping(self, dev: int) -> CompositeGate:
        return self._dev_to_gate[dev]
