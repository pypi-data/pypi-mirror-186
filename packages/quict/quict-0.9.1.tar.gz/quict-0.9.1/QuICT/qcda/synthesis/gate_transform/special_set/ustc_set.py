from .. import InstructionSet
from ..transform_rule import xyx_rule

from QuICT.core.gate import *

USTCSet = InstructionSet(
    GateType.cx,
    [GateType.rx, GateType.ry, GateType.rz, GateType.h, GateType.x]
)
USTCSet.register_one_qubit_rule(xyx_rule)
