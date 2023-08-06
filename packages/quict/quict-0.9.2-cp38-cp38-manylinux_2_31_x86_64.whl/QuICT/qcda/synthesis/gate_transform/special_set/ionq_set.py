from .. import InstructionSet
from ..transform_rule import xyx_rule

from QuICT.core.gate import *

IonQSet = InstructionSet(
    GateType.rxx,
    [GateType.rx, GateType.ry, GateType.rz]
)
IonQSet.register_one_qubit_rule(xyx_rule)
