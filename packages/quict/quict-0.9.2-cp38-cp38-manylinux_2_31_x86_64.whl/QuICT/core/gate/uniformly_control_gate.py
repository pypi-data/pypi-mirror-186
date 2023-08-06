from .backend.uniformly_gate import *
from QuICT.core.gate import GateType
from QuICT.tools.exception.core import TypeError


class UniformlyControlGate(object):
    """
    Uniformly Ry, Rz or one-qubit Unitary gate
    """
    def __init__(self, target_gate: GateType = GateType.unitary):
        """
        Args:
            target_gate(GateType): type of target gate, could be Ry, Rz or Unitary
        """
        assert target_gate in [GateType.ry, GateType.rz, GateType.unitary], \
            TypeError("UniformlyControlGate.target_gate", [GateType.ry, GateType.rz, GateType.unitary], target_gate)
        self.target_gate = target_gate

    def __call__(self, arg_list):
        """
        Args:
            arg_list(list): a list of angles for Ry and Rz or a list of 2*2 unitaries for Unitary

        Returns:
            CompositeGate: uniformly control target gate
        """
        if self.target_gate in [GateType.ry, GateType.rz]:
            return UniformlyRotation(self.target_gate).execute(arg_list)
        else:
            return UniformlyUnitary().execute(arg_list)
