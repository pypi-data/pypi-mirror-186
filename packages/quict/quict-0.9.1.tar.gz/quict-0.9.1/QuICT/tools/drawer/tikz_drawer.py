# -*- coding:utf8 -*-

from copy import copy
import numpy as np
from typing import *

from QuICT.core import Circuit
from QuICT.core.gate import *


class TikzDrawer:
    wire_gap = 0.8
    level_gap = 1.0
    rectangle_size = level_gap / 2

    @classmethod
    def circuit_layers(cls, circuit: Circuit) -> Iterable[List[BasicGate]]:
        ret = []
        cur_level = []
        cur_level_occ = set([])

        for gate in circuit.gates:
            gate: BasicGate

            gate_min = np.min(gate.affectArgs)
            gate_max = np.max(gate.affectArgs)
            is_not_occupied = True
            for bit in range(gate_min, gate_max + 1):
                if bit in cur_level_occ:
                    is_not_occupied = False
                cur_level_occ.add(bit)

            if is_not_occupied:
                cur_level.append(gate)
            else:
                ret.append(copy(cur_level))
                cur_level = [gate]
                cur_level_occ = set(list(range(gate_min, gate_max + 1)))

        ret.append(cur_level)
        return ret

    @classmethod
    def layer_print(cls, circuit: Circuit):
        layers = cls.circuit_layers(circuit)
        for idx, layer in enumerate(layers):
            print("=" * 40)
            print(f"[Layer {idx}]")
            for gate in layer:
                gate.print_info()

    @classmethod
    def get_center_pos(cls, qubit: int, level: int) -> Tuple[float, float]:

        y = 0 - cls.wire_gap * (qubit - 1)
        x = level * cls.level_gap + cls.level_gap / 2
        return x, y

    @classmethod
    def draw_1_qubit_gate(cls, gate: BasicGate, level: int) -> str:
        x, y = cls.get_center_pos(gate.targ, level)
        rectangle_size = cls.rectangle_size

        if isinstance(gate, XGate):
            name = "X"
        elif isinstance(gate, YGate):
            name = "Y"
        elif isinstance(gate, ZGate):
            name = "Z"
        elif isinstance(gate, HGate):
            name = "H"
        elif isinstance(gate, RxGate):
            name = "Rx"
        elif isinstance(gate, RyGate):
            name = "Ry"
        elif isinstance(gate, RzGate):
            name = "Rz"
        elif isinstance(gate, IDGate):
            name = "Id"
        else:
            name = "*"

        gate_specification = f" node[pos=.5] {{{name}}}"
        tikz_command = "% begin of single qubit rectangle\n"
        tikz_command += f"\\draw " \
                        f"({x - rectangle_size / 2},{y + rectangle_size / 2})" \
                        " rectangle " \
                        f"({x + rectangle_size / 2},{y - rectangle_size / 2})" + \
                        gate_specification + \
                        ";\n"

        tikz_command += "% end of single qubit rectangle\n\n"

        tikz_command += "% begin of single qubit wire next to rectangle\n"

        tikz_command += f"\\draw " \
                        f"({x - cls.level_gap / 2},{y}) " \
                        f"-- " \
                        f"({x - cls.rectangle_size / 2},{y})" \
                        f";\n" \
                        f"\\draw " \
                        f"({x + cls.rectangle_size / 2},{y}) " \
                        f"-- " \
                        f"({x + cls.level_gap / 2},{y}) " \
                        f";\n"
        tikz_command += "% end of single qubit wire next to rectangle\n\n"
        return tikz_command

    @classmethod
    def draw_2_qubit_gate(cls, gate: BasicGate, level: int) -> str:
        if isinstance(gate, CXGate):
            t_name = "X"
        elif isinstance(gate, CYGate):
            t_name = "Y"
        elif isinstance(gate, CZGate):
            t_name = "Z"
        elif isinstance(gate, CRzGate):
            t_name = "Rz"
        elif isinstance(gate, CHGate):
            t_name = "H"
        else:
            t_name = "*"

        t_x, t_y = cls.get_center_pos(gate.targ, level)
        rectangle_size = cls.rectangle_size

        gate_specification = f" node[pos=.5] {{{t_name}}}"

        tikz_command = "% begin of 2 qubit gate target rectangle\n"

        tikz_command += f"\\draw " \
                        f"({t_x - rectangle_size / 2},{t_y + rectangle_size / 2})" \
                        " rectangle " \
                        f"({t_x + rectangle_size / 2},{t_y - rectangle_size / 2})" + \
                        gate_specification + \
                        ";\n"

        tikz_command += "% end of 2 qubit gate target rectangle\n\n"

        tikz_command += "% begin of 2 qubit gate wire next to target rectangle\n"

        tikz_command += f"\\draw " \
                        f"({t_x - cls.level_gap / 2},{t_y}) " \
                        f"-- " \
                        f"({t_x - cls.rectangle_size / 2},{t_y}) " \
                        f";\n" \
                        f"\\draw " \
                        f"({t_x + cls.rectangle_size / 2},{t_y}) " \
                        f"-- " \
                        f"({t_x + cls.level_gap / 2},{t_y}) " \
                        f";\n"

        tikz_command += "% end of 2 qubit gate wire next to target rectangle\n\n"

        tikz_command += "% begin of 2 qubit gate control bit wire\n"

        c_x, c_y = cls.get_center_pos(gate.carg, level)
        tikz_command += f"\\draw " \
                        f"({c_x - cls.level_gap / 2},{c_y}) " \
                        f"-- " \
                        f"({c_x + cls.level_gap / 2},{c_y}) " \
                        f";\n" \
                        f"\\filldraw " \
                        f"({c_x},{c_y}) circle ({cls.level_gap / 20}) " \
                        f";\n"

        tikz_command += "% end of 2 qubit gate control bit wire\n\n"

        tikz_command += "% begin of 2 qubit gate connect wire\n"

        if t_y > c_y:
            t_y_offset = t_y - cls.rectangle_size / 2
        else:
            t_y_offset = t_y + cls.rectangle_size / 2

        tikz_command += f"\\draw " \
                        f"({c_x},{c_y}) " \
                        f"-- " \
                        f"({t_x},{t_y_offset}) " \
                        f";\n"

        tikz_command += "% end of 2 qubit gate connect wire\n"

        return tikz_command

    @classmethod
    def draw_gate(cls, gate: BasicGate, level: int) -> str:
        ret = []
        rg = len(gate.affectArgs)
        if rg == 1:
            ret.append(cls.draw_1_qubit_gate(gate, level))
        elif rg == 2:
            ret.append(cls.draw_2_qubit_gate(gate, level))
        else:
            raise NotImplementedError("Can only draw 1 or 2 qubit gate!!!")

        return "".join(ret)

    @classmethod
    def draw_layer_line(cls, layer_bit: List[int], level: int) -> str:
        ret = []
        for i, b_type in enumerate(layer_bit):
            x, y = cls.get_center_pos(i, level)
            tikz_command = "% begin of non occupied qubit wire\n"
            if b_type == 1:
                tikz_command += ""
            elif b_type == 2:
                tikz_command += ""
            else:
                tikz_command += f"\\draw " \
                                f"({x - cls.level_gap / 2},{y}) " \
                                f"-- " \
                                f"({x + cls.level_gap / 2},{y}) " \
                                f";\n"
            tikz_command += "% end of non occupied qubit wire\n\n"
            ret.append(tikz_command)
        return "".join(ret)

    @classmethod
    def draw_layer(cls, layer: List[BasicGate], level: int, qubit_num: int) -> str:
        layer_bit = [0 for _ in range(qubit_num)]
        ret = []
        for gate in layer:
            k = len(gate.affectArgs)
            for b in gate.affectArgs:
                layer_bit[b] = k
            ret.append(cls.draw_gate(gate, level))
        line_command = cls.draw_layer_line(layer_bit, level)
        ret.append(line_command)
        return "".join(ret)

    @classmethod
    def draw_empty_head_n_tail_wire(cls, level_max: int, qubit_num: int) -> str:
        ret = []
        for bit in range(qubit_num):
            x, y = cls.get_center_pos(bit, 0)
            tikz_command = "% begin of leading emtpy wires\n"
            tikz_command += f"\\draw " \
                            f"({x - cls.level_gap * 1.5 / 2},{y}) " \
                            f"-- " \
                            f"({x - cls.level_gap / 2},{y}) " \
                            f";\n"
            tikz_command += "% end of leading emtpy wires\n\n"

            x, y = cls.get_center_pos(bit, level_max)
            tikz_command += "% begin of tailing empty wires\n"
            tikz_command += f"\\draw " \
                            f"({x + cls.level_gap / 2},{y}) " \
                            f"-- " \
                            f"({x + cls.level_gap * 1.5 / 2},{y}) " \
                            f";\n"
            tikz_command += "% end of tailing empty wires\n\n"

            ret.append(tikz_command)

        return "".join(ret)

    @classmethod
    def run(cls, circuit: Circuit):
        ans = ["\\begin{tikzpicture}\n"]
        circuit_width = circuit.circuit_width()

        layer_cnt = 0
        for idx, layer in enumerate(cls.circuit_layers(circuit)):
            cmds = cls.draw_layer(layer, idx, circuit_width)
            ans.append(cmds)
            layer_cnt += 1

        ans.append(cls.draw_empty_head_n_tail_wire(layer_cnt - 1, circuit_width))

        ans.append("\\end{tikzpicture}")

        tikz_command = "".join(ans)
        # print()
        # print(tikz_command)
        return tikz_command
