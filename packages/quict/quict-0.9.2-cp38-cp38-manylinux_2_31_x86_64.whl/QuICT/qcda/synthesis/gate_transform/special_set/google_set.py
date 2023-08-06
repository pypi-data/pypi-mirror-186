from .. import InstructionSet
from ..transform_rule import xyx_rule

from QuICT.core.gate import *

GoogleSet = InstructionSet(
    GateType.fsim,
    [GateType.sx, GateType.sy, GateType.sw, GateType.rx, GateType.ry]
)
GoogleSet.register_one_qubit_rule(xyx_rule)
