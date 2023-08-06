from .. import InstructionSet
from ..transform_rule import hrz_rule

from QuICT.core.gate import *

NamSet = InstructionSet(
    GateType.cx,
    [GateType.h, GateType.rz]
)
NamSet.register_one_qubit_rule(hrz_rule)
