from .. import InstructionSet
from ..transform_rule import ibmq_rule

from QuICT.core.gate import *

IBMQSet = InstructionSet(
    GateType.cx,
    [GateType.rz, GateType.sx, GateType.x]
)
IBMQSet.register_one_qubit_rule(ibmq_rule)
