from .. import InstructionSet
from ..transform_rule import u3_rule

from QuICT.core.gate import *

OriginSet = InstructionSet(
    GateType.cx,
    [GateType.u3]
)
OriginSet.register_one_qubit_rule(u3_rule)
