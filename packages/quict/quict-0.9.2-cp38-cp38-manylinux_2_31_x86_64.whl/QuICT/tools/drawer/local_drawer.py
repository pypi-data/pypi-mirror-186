#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/3/30 6:24
# @Author  : Han Yu
# @File    : _localDrawer.py

import collections
import math
import re

import numpy as np
from matplotlib import patches
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from QuICT.core.gate import *

from .ibmq_style import DefaultStyle

LINE_WIDTH = 1.5
FOLD = 26
cir_len = 0
FONT_SIZE = 13
SUB_FONT_SIZE = 8

WID = 0.65
HIG = 0.65
DEFAULT_SCALE = 4.3
PORDER_GATE = 5
PORDER_LINE = 3
PORDER_REGLINE = 2
PORDER_GRAY = 3
PORDER_TEXT = 6
PORDER_SUBP = 4


def pi_check(p, eps=1e-6, ndigits=3):
    p = float(p)
    if abs(p) < 1e-14:
        return '0'
    tp = p / np.pi
    if abs(tp) >= 1:
        if abs(tp % 1) < eps:
            val = int(round(tp))
            if val == 1:
                str_out = '$\\pi$'
            elif val == -1:
                str_out = '$-$$\\pi$'
            else:
                str_out = '{}$\\pi$'.format(val)
            return str_out

    tp = np.pi / p
    if abs(abs(tp) - abs(round(tp))) < eps:
        val = int(round(tp))
        if val > 0:
            str_out = '$\\pi$/{}'.format(val)
        else:
            str_out = '$-$$\\pi$/{}'.format(abs(val))
        return str_out

    abs_p = abs(p)
    N, D = np.meshgrid(np.arange(1, 64), np.arange(1, 64))
    frac = np.where(np.abs(abs_p - N / D * np.pi) < 1e-8)
    if frac[0].shape[0]:
        numer = int(frac[1][0]) + 1
        denom = int(frac[0][0]) + 1
        if p < 0:
            numer *= -1

        if numer == 1 and denom == 1:
            str_out = '$\\pi$'
        elif numer == -1 and denom == 1:
            str_out = '$-$$\\pi$'
        elif numer == 1:
            str_out = '$\\pi$/{}'.format(denom)
        elif numer == -1:
            str_out = '$-$$\\pi$/{}'.format(denom)
        elif denom == 1:
            str_out = '{}/$\\pi$'.format(numer)
        else:
            str_out = '{}$\\pi$/{}'.format(numer, denom)

        return str_out

    str_out = '%.{}g'.format(ndigits) % p
    return str_out


class circuit_layer(object):
    def __init__(self):
        self.pic = set()
        self.occupy = set()
        self.gates = []

    def addGate(self, gate: BasicGate) -> bool:
        Q_set = set(gate.cargs) | set(gate.targs)
        for element in range(min(Q_set), max(Q_set) + 1):
            if element in self.pic:
                return False
        for element in range(min(Q_set), max(Q_set) + 1):
            self.pic.add(element)
        self.occupy |= Q_set
        self.gates.append(gate)
        return True

    def checkGate(self, gate: BasicGate) -> bool:
        Q_set = set(gate.cargs) | set(gate.targs)
        for element in range(min(Q_set), max(Q_set) + 1):
            if element in self.pic:
                return False
        return True


class Anchor(object):
    def __init__(self, pos):
        self.pos = pos
        self.position = []
        self.anchor = 0

    def set_index(self, index, layer_width):
        h_pos = index % FOLD + 1
        if h_pos + (layer_width - 1) > FOLD:
            index = index + FOLD - (h_pos - 1)
        for i in range(layer_width):
            if index + i not in self.position:
                self.position.append(index + i)
        self.position.sort()

    def get_index(self):
        if len(self.position) > 0:
            return self.position[-1] + 1
        return 0

    def coord(self, position, layer_width, offset_x):
        h_pos = position % FOLD + 1
        if h_pos + (layer_width - 1) > FOLD:
            position = position + FOLD - (h_pos - 1)
        x = position % FOLD + 1 + 0.5 * (layer_width - 1)
        y = self.pos - (position // FOLD) * (cir_len + 1)
        self.anchor = position
        return x + offset_x, y


class PhotoDrawer(object):

    def __init__(self):
        self.style = DefaultStyle()
        # plt.figure() will always trigger interactive mode eagerly. Use matplotlib.figure.Figure's full OO interface.
        # refer:
        # https://stackoverflow.com/questions/18207563/using-interactive-and-non-interactive-backends-within-one-program
        self.figure = Figure()
        self.figure.patch.set_facecolor(color='#ffffff')
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.scale = 1
        self.lwidth15 = 1.5 * self.scale
        self.lwidth2 = 2.0 * self.scale
        self.char_list = {' ': (0.0958, 0.0583), '!': (0.1208, 0.0729), '"': (0.1396, 0.0875),
                          '#': (0.2521, 0.1562), '$': (0.1917, 0.1167), '%': (0.2854, 0.1771),
                          '&': (0.2333, 0.1458), "'": (0.0833, 0.0521), '(': (0.1167, 0.0729),
                          ')': (0.1167, 0.0729), '*': (0.15, 0.0938), '+': (0.25, 0.1562),
                          ',': (0.0958, 0.0583), '-': (0.1083, 0.0667), '.': (0.0958, 0.0604),
                          '/': (0.1021, 0.0625), '0': (0.1875, 0.1167), '1': (0.1896, 0.1167),
                          '2': (0.1917, 0.1188), '3': (0.1917, 0.1167), '4': (0.1917, 0.1188),
                          '5': (0.1917, 0.1167), '6': (0.1896, 0.1167), '7': (0.1917, 0.1188),
                          '8': (0.1896, 0.1188), '9': (0.1917, 0.1188), ':': (0.1021, 0.0604),
                          ';': (0.1021, 0.0604), '<': (0.25, 0.1542), '=': (0.25, 0.1562),
                          '>': (0.25, 0.1542), '?': (0.1583, 0.0979), '@': (0.2979, 0.1854),
                          'A': (0.2062, 0.1271), 'B': (0.2042, 0.1271), 'C': (0.2083, 0.1292),
                          'D': (0.2312, 0.1417), 'E': (0.1875, 0.1167), 'F': (0.1708, 0.1062),
                          'G': (0.2312, 0.1438), 'H': (0.225, 0.1396), 'I': (0.0875, 0.0542),
                          'J': (0.0875, 0.0542), 'K': (0.1958, 0.1208), 'L': (0.1667, 0.1042),
                          'M': (0.2583, 0.1604), 'N': (0.225, 0.1396), 'O': (0.2354, 0.1458),
                          'P': (0.1812, 0.1125), 'Q': (0.2354, 0.1458), 'R': (0.2083, 0.1292),
                          'S': (0.1896, 0.1188), 'T': (0.1854, 0.1125), 'U': (0.2208, 0.1354),
                          'V': (0.2062, 0.1271), 'W': (0.2958, 0.1833), 'X': (0.2062, 0.1271),
                          'Y': (0.1833, 0.1125), 'Z': (0.2042, 0.1271), '[': (0.1167, 0.075),
                          '\\': (0.1021, 0.0625), ']': (0.1167, 0.0729), '^': (0.2521, 0.1562),
                          '_': (0.1521, 0.0938), '`': (0.15, 0.0938), 'a': (0.1854, 0.1146),
                          'b': (0.1917, 0.1167), 'c': (0.1646, 0.1021), 'd': (0.1896, 0.1188),
                          'e': (0.1854, 0.1146), 'f': (0.1042, 0.0667), 'g': (0.1896, 0.1188),
                          'h': (0.1896, 0.1188), 'i': (0.0854, 0.0521), 'j': (0.0854, 0.0521),
                          'k': (0.1729, 0.1083), 'l': (0.0854, 0.0521), 'm': (0.2917, 0.1812),
                          'n': (0.1896, 0.1188), 'o': (0.1833, 0.1125), 'p': (0.1917, 0.1167),
                          'q': (0.1896, 0.1188), 'r': (0.125, 0.0771), 's': (0.1562, 0.0958),
                          't': (0.1167, 0.0729), 'u': (0.1896, 0.1188), 'v': (0.1771, 0.1104),
                          'w': (0.2458, 0.1521), 'x': (0.1771, 0.1104), 'y': (0.1771, 0.1104),
                          'z': (0.1562, 0.0979), '{': (0.1917, 0.1188), '|': (0.1, 0.0604),
                          '}': (0.1896, 0.1188)}
        pass

    @staticmethod
    def resolution_layers(circuit):
        layers = [circuit_layer()]
        for gate in circuit.gates:
            for i in range(len(layers) - 1, -2, -1):
                if i == -1 or not layers[i].checkGate(gate):
                    if i + 1 >= len(layers):
                        layers.append(circuit_layer())
                    layers[i + 1].addGate(gate)
                    break
        return layers

    @staticmethod
    def get_parameter_str(params):
        strings = []
        for p in params:
            strings.append(pi_check(p))
        return ', '.join(strings)

    def draw_gate(self, point, text=None, p_string=None, fc=None):
        xpos, ypos = point

        c_len = False

        if p_string:
            if '$\\pi$' in p_string:
                pi_count = p_string.count('pi')
                subtext_len = len(p_string) - (4 * pi_count)
                if subtext_len > 10:
                    c_len = True
            else:
                c_len = len(p_string) > 10

        if c_len:
            subtext_len = len(p_string)
            if '$\\pi$' in p_string:
                pi_count = p_string.count('pi')
                subtext_len = subtext_len - (4 * pi_count)

            boxes_wide = round(max(subtext_len, len(text)) / 10, 1) or 1
            wid = WID * 1.5 * boxes_wide
            if wid < WID:
                wid = WID
        else:
            wid = WID

        if fc:
            _fc = fc
        elif text and text in self.style.dispcol:
            _fc = self.style.dispcol[text]
        else:
            _fc = self.style.gc
        box = patches.Rectangle(
            xy=(xpos - 0.5 * wid, ypos - 0.5 * HIG), width=wid, height=HIG,
            fc=_fc, ec=self.style.edge_color, linewidth=1.5, zorder=PORDER_GATE)
        self.ax.add_patch(box)

        if text:
            font_size = self.style.fs
            sub_font_size = self.style.sfs
            if text in ['reset']:
                disp_color = self.style.not_gate_lc
                sub_color = self.style.not_gate_lc
                font_size = self.style.math_fs

            else:
                disp_color = self.style.gt
                sub_color = self.style.sc

            if text in self.style.dispcol:
                disp_text = "${}$".format(self.style.disptex[text])
            else:
                disp_text = text

            if p_string:
                self.ax.text(xpos, ypos + 0.15 * HIG, disp_text, ha='center',
                             va='center', fontsize=font_size,
                             color=disp_color, clip_on=True,
                             zorder=PORDER_TEXT)
                self.ax.text(xpos, ypos - 0.3 * HIG, p_string, ha='center',
                             va='center', fontsize=sub_font_size,
                             color=sub_color, clip_on=True,
                             zorder=PORDER_TEXT)
            else:
                self.ax.text(xpos, ypos, disp_text, ha='center', va='center',
                             fontsize=font_size,
                             color=disp_color,
                             clip_on=True,
                             zorder=PORDER_TEXT)

    def draw_depth(self, start, end):
        start_pos = start % FOLD + 0.14
        end_pos = end % FOLD + 0.14
        if end_pos == 0:
            end_pos = FOLD

        start_layer = start // FOLD
        end_layer = end // FOLD

        if start_layer == end_layer:
            box = patches.Rectangle(
                xy=(start_pos - 0.75 * WID, - (start_layer + 1) * (cir_len + 1) + 1.5),
                width=end_pos - start_pos - 1 + 1.5 * WID, height=cir_len,
                fc='#FF0000', ec='#FF0000', linewidth=1.5, zorder=PORDER_GATE, fill=False, linestyle='dashed')
            self.ax.add_patch(box)
        else:
            self.ax.plot([start_pos - 0.75 * WID, start_pos - 0.75 * WID],
                         [- (start_layer + 1) * (cir_len + 1) + 1.5,
                          - (start_layer + 1) * (cir_len + 1) + 1.5 + cir_len],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)
            self.ax.plot([start_pos - 0.75 * WID, FOLD + 0.14],
                         [- (start_layer + 1) * (cir_len + 1) + 1.5, - (start_layer + 1) * (cir_len + 1) + 1.5],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)
            self.ax.plot([start_pos - 0.75 * WID, FOLD + 0.14],
                         [- (start_layer + 1) * (cir_len + 1) + 1.5 + cir_len,
                          - (start_layer + 1) * (cir_len + 1) + 1.5 + cir_len],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)

            self.ax.plot([end_pos - 1 + 0.75 * WID, end_pos - 1 + 0.75 * WID],
                         [- (end_layer + 1) * (cir_len + 1) + 1.5,
                          - (end_layer + 1) * (cir_len + 1) + 1.5 + cir_len],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)
            self.ax.plot([-0.75 * WID, end_pos - 1 + 0.75 * WID],
                         [- (end_layer + 1) * (cir_len + 1) + 1.5,
                          - (end_layer + 1) * (cir_len + 1) + 1.5],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)
            self.ax.plot([-0.75 * WID, end_pos - 1 + 0.75 * WID],
                         [- (end_layer + 1) * (cir_len + 1) + 1.5 + cir_len,
                          - (end_layer + 1) * (cir_len + 1) + 1.5 + cir_len],
                         color='#FF0000',
                         linewidth=1.5,
                         linestyle='dashed',
                         zorder=PORDER_GATE)
            for i in range(start_layer + 1, end_layer):
                self.ax.plot([-0.75 * WID, FOLD + 0.14],
                             [- (i + 1) * (cir_len + 1) + 1.5 + cir_len,
                              - (i + 1) * (cir_len + 1) + 1.5 + cir_len],
                             color='#FF0000',
                             linewidth=1.5,
                             linestyle='dashed',
                             zorder=PORDER_GATE)
                self.ax.plot([-0.75 * WID, FOLD + 0.14],
                             [- (i + 2) * (cir_len + 1) + 1.5 + 1 + cir_len,
                              - (i + 2) * (cir_len + 1) + 1.5 + 1 + cir_len],
                             color='#FF0000',
                             linewidth=1.5,
                             linestyle='dashed',
                             zorder=PORDER_GATE)

    def draw_line(self, xy0, xy1, lc=None, ls=None, zorder=PORDER_LINE):
        x0, y0 = xy0
        x1, y1 = xy1
        if lc is None:
            linecolor = self.style.lc
        else:
            linecolor = lc
        if ls is None:
            linestyle = 'solid'
        else:
            linestyle = ls

        if linestyle == 'doublet':
            theta = np.arctan2(np.abs(x1 - x0), np.abs(y1 - y0))
            dx = 0.05 * WID * np.cos(theta)
            dy = 0.05 * WID * np.sin(theta)
            self.ax.plot([x0 + dx, x1 + dx], [y0 + dy, y1 + dy],
                         color=linecolor,
                         linewidth=2,
                         linestyle='solid',
                         zorder=zorder)
            self.ax.plot([x0 - dx, x1 - dx], [y0 - dy, y1 - dy],
                         color=linecolor,
                         linewidth=2,
                         linestyle='solid',
                         zorder=zorder)
        else:
            self.ax.plot([x0, x1], [y0, y1],
                         color=linecolor,
                         linewidth=2,
                         linestyle=linestyle,
                         zorder=zorder)

    def draw_custom_gate(self, xy, cxy=None, fc=None, wide=True, text=None,
                         subtext=None):
        xpos = min([x[0] for x in xy])
        ypos = min([y[1] for y in xy])
        ypos_max = max([y[1] for y in xy])

        if cxy:
            ypos = min([y[1] for y in cxy])
        if wide:
            if subtext:
                boxes_length = round(max([len(text), len(subtext)]) / 6) or 1
            else:
                boxes_length = math.ceil(len(text) / 6) or 1
            wid = WID * 2.5 * boxes_length
        else:
            wid = WID

        if fc:
            _fc = fc
        else:
            if self.style.name != 'bw':
                if self.style.gc != DefaultStyle().gc:
                    _fc = self.style.gc
                else:
                    _fc = self.style.dispcol['multi']
            else:
                _fc = self.style.gc

        qubit_span = abs(ypos) - abs(ypos_max) + 1
        height = HIG + (qubit_span - 1)
        box = patches.Rectangle(
            xy=(xpos - 0.5 * wid, ypos - .5 * HIG),
            width=wid, height=height,
            fc=_fc,
            ec=self.style.dispcol['multi'],
            linewidth=1.5, zorder=PORDER_GATE)
        self.ax.add_patch(box)
        # Annotate inputs
        for bit, y in enumerate([x[1] for x in xy]):
            self.ax.text(xpos - 0.45 * wid, y, str(bit), ha='left', va='center',
                         fontsize=self.style.fs, color=self.style.gt,
                         clip_on=True, zorder=PORDER_TEXT)

        if text:
            disp_text = text
            if subtext:
                self.ax.text(xpos, ypos + 0.5 * height, disp_text, ha='center',
                             va='center', fontsize=self.style.fs,
                             color=self.style.gt, clip_on=True,
                             zorder=PORDER_TEXT)
                self.ax.text(xpos, ypos + 0.3 * height, subtext, ha='center',
                             va='center', fontsize=self.style.sfs,
                             color=self.style.sc, clip_on=True,
                             zorder=PORDER_TEXT)
            else:
                self.ax.text(xpos, ypos + .5 * (qubit_span - 1), disp_text,
                             ha='center',
                             va='center',
                             fontsize=self.style.fs,
                             color=self.style.gt,
                             clip_on=True,
                             zorder=PORDER_TEXT,
                             wrap=True)

    def draw_measure(self, xy):
        x, y = xy
        self.draw_gate(xy, fc=self.style.dispcol['meas'])

        arc = patches.Arc(xy=(x, y - 0.15 * HIG), width=WID * 0.7,
                          height=HIG * 0.7, theta1=0, theta2=180, fill=False,
                          ec=self.style.not_gate_lc, linewidth=2,
                          zorder=PORDER_GATE)
        self.ax.add_patch(arc)
        self.ax.plot([x, x + 0.35 * WID],
                     [y - 0.15 * HIG, y + 0.20 * HIG],
                     color=self.style.not_gate_lc, linewidth=2, zorder=PORDER_GATE)

    def draw_ctrl_qubit(self, xy, fc=None, ec=None):
        if self.style.gc != DefaultStyle().gc:
            fc = self.style.gc
            ec = self.style.gc
        if fc is None:
            fc = self.style.lc
        if ec is None:
            ec = self.style.lc
        xpos, ypos = xy
        box = patches.Circle(xy=(xpos, ypos), radius=WID * 0.15,
                             fc=fc, ec=ec,
                             linewidth=1.5, zorder=PORDER_GATE)
        self.ax.add_patch(box)

    def draw_tgt_qubit(self, xy, fc=None, ec=None, ac=None, add_width=None):
        if self.style.gc != DefaultStyle().gc:
            fc = self.style.gc
            ec = self.style.gc
        if fc is None:
            fc = self.style.dispcol['target']
        if ec is None:
            ec = self.style.lc
        if ac is None:
            ac = self.style.lc
        if add_width is None:
            add_width = 0.35

        linewidth = 2

        if self.style.dispcol['target'] == '#ffffff':
            add_width = self.style.colored_add_width

        xpos, ypos = xy

        box = patches.Circle(xy=(xpos, ypos), radius=HIG * 0.35,
                             fc=fc, ec=ec, linewidth=linewidth,
                             zorder=PORDER_GATE)
        self.ax.add_patch(box)
        # add '+' symbol
        self.ax.plot([xpos, xpos], [ypos - add_width * HIG,
                                    ypos + add_width * HIG],
                     color=ac, linewidth=linewidth, zorder=PORDER_GATE + 1)

        self.ax.plot([xpos - add_width * HIG, xpos + add_width * HIG],
                     [ypos, ypos], color=ac, linewidth=linewidth,
                     zorder=PORDER_GATE + 1)

    def _get_text_width(self, text, fontsize, param=False):
        if not text:
            return 0.0

        math_mode_match = re.compile(r"(?<!\\)\$(.*)(?<!\\)\$").search(text)
        num_underscores = 0
        num_carets = 0
        if math_mode_match:
            math_mode_text = math_mode_match.group(1)
            num_underscores = math_mode_text.count('_')
            num_carets = math_mode_text.count('^')

        # If there are subscripts or superscripts in mathtext string
        # we need to account for that spacing by manually removing
        # from text string for text length
        if num_underscores:
            text = text.replace('_', '', num_underscores)
        if num_carets:
            text = text.replace('^', '', num_carets)

        # This changes hyphen to + to match width of math mode minus sign.
        if param:
            text = text.replace('-', '+')

        f = 0 if fontsize == self.style else 1
        sum_text = 0.0
        for c in text:
            try:
                if c not in ["$", "\\"]:
                    sum_text += self.char_list[c][f]
            except KeyError:
                # if non-ASCII char, use width of 'c', an average size
                sum_text += self.char_list['c'][f]

        return sum_text

    def draw_multiqubit_gate(self, xy, fc=None, ec=None, gt=None, sc=None, text='', subtext=''):
        xpos = min([x[0] for x in xy])
        ypos = min([y[1] for y in xy])
        ypos_max = max([y[1] for y in xy])
        fs = self.style.fs
        sfs = self.style.sfs

        # added .21 is for qubit numbers on the left side
        text_width = self._get_text_width(text, fs) + .21 * 2
        sub_width = self._get_text_width(subtext, sfs, param=True) + .21 * 2
        wid = max((text_width, sub_width, WID))

        qubit_span = abs(ypos) - abs(ypos_max) + 1
        height = HIG + (qubit_span - 1)
        box = patches.Rectangle(
            xy=(xpos - 0.5 * wid, ypos - 0.5 * HIG), width=wid, height=height,
            fc=fc, ec=ec, linewidth=self.lwidth15, zorder=PORDER_GATE)
        self.ax.add_patch(box)

        # annotate inputs
        for bit, y in enumerate([x[1] for x in xy]):
            self.ax.text(xpos + .07 - 0.5 * wid, y, str(bit), ha='left', va='center',
                         fontsize=fs, color=gt,
                         clip_on=True, zorder=PORDER_TEXT)
        if text:
            if subtext:
                self.ax.text(xpos + .11, ypos + 0.4 * height, text, ha='center',
                             va='center', fontsize=fs,
                             color=gt, clip_on=True,
                             zorder=PORDER_TEXT)
                self.ax.text(xpos + .11, ypos + 0.2 * height, subtext, ha='center',
                             va='center', fontsize=sfs,
                             color=sc, clip_on=True,
                             zorder=PORDER_TEXT)
            else:
                self.ax.text(xpos + .11, ypos + .5 * (qubit_span - 1), text,
                             ha='center', va='center', fontsize=fs,
                             color=gt, clip_on=True,
                             zorder=PORDER_TEXT, wrap=True)

    def draw_swap(self, xy):
        xpos, ypos = xy
        color = self.style.dispcol['swap']
        self.ax.plot([xpos - 0.20 * WID, xpos + 0.20 * WID],
                     [ypos - 0.20 * WID, ypos + 0.20 * WID],
                     color=color, linewidth=2, zorder=PORDER_LINE + 1)
        self.ax.plot([xpos - 0.20 * WID, xpos + 0.20 * WID],
                     [ypos + 0.20 * WID, ypos - 0.20 * WID],
                     color=color, linewidth=2, zorder=PORDER_LINE + 1)

    def draw_linefeed_mark(self, xy):
        xpos, ypos = xy

        self.ax.plot([xpos - .1, xpos - .1],
                     [ypos, ypos - cir_len + 1],
                     color=self.style.lc, zorder=PORDER_LINE)
        self.ax.plot([xpos + .1, xpos + .1],
                     [ypos, ypos - cir_len + 1],
                     color=self.style.lc, zorder=PORDER_LINE)

    def draw_regs_sub(self, n_fold, offset_x=None, now=None, name_dict=None):
        for qreg in name_dict.values():
            if n_fold == 0:
                label = qreg['text']
            else:
                label = qreg['text']
            y = qreg['y'] - n_fold * (cir_len + 1)
            self.ax.text(offset_x, y, label, ha='right', va='center',
                         fontsize=1.25 * self.style.fs,
                         color=self.style.tc,
                         clip_on=True,
                         zorder=PORDER_TEXT)
            self.draw_line([offset_x + 0.5, y], [now['max_x'], y], zorder=PORDER_REGLINE)

    def run(self, circuit, filename=None, show_depth=False, save_file=False):
        global cir_len
        cir_len = circuit.width()
        name_dict = collections.OrderedDict()
        now = {
            'max_x': 0,
            'max_y': 0,
        }
        anchors = {}
        max_name = 0
        for i in range(cir_len):
            name = f'$q_{{{i}}}$'
            max_name = max(max_name, len(name))
            name_dict[i] = {
                'y': -i,
                'text': name,
                'index': i
            }
            anchors[i] = Anchor(-i)
        offset_x = 0.18 * (max_name - 7) - 0.5

        layers = self.resolution_layers(circuit)
        layer_position = []
        position = 0
        for layer in layers:
            layer_width = 1

            for gate in layer.gates:
                if gate.type == GateType.perm or gate.type == GateType.unitary:
                    continue
                elif gate.params > 1:
                    param = self.get_parameter_str(gate.pargs)
                    if '$\\pi$' in param:
                        pi_count = param.count('pi')
                        len_param = len(param) - (4 * pi_count)
                    else:
                        len_param = len(param)
                    if len_param > len(gate.qasm_name):
                        box_width = math.floor(len(param) / 10)
                        if box_width <= 1:
                            box_width = 1

                        if layer_width <= box_width:
                            layer_width = box_width + 1

            for gate in layer.gates:
                coord = []
                for index in gate.cargs:
                    anchors[index].set_index(position, layer_width)
                    coord.append(anchors[index].coord(position, layer_width, offset_x))
                for index in gate.targs:
                    anchors[index].set_index(position, layer_width)
                    coord.append(anchors[index].coord(position, layer_width, offset_x))

                bottom = min(coord, key=lambda c: c[1])
                top = max(coord, key=lambda c: c[1])

                position = anchors[gate.targ].anchor

                param = None
                if gate.params > 0:
                    param = self.get_parameter_str(gate.pargs)

                if gate.type == GateType.perm:
                    name = gate.type.value
                    for coor in coord:
                        self.draw_gate(coor, name, '')
                    self.draw_line(bottom, top, lc=self.style.dispcol[name])
                elif gate.type == GateType.measure:
                    self.draw_measure(coord[0])
                elif gate.type == GateType.barrier:
                    self.draw_gate(coord[0], gate.qasm_name)
                elif len(coord) == 1:
                    name = gate.qasm_name
                    if param is not None:
                        p_string = '({})'.format(param)
                        self.draw_gate(coord[0], name, p_string)
                    else:
                        self.draw_gate(coord[0], name, '')
                elif len(coord) == 2:
                    if gate.type == GateType.cx:
                        if self.style.dispcol['cx'] != '#ffffff':
                            add_width = self.style.colored_add_width
                        else:
                            add_width = None
                        self.draw_ctrl_qubit(coord[0], fc=self.style.dispcol['cx'], ec=self.style.dispcol['cx'])

                        self.draw_tgt_qubit(coord[1], fc=self.style.dispcol['cx'], ec=self.style.dispcol['cx'],
                                            ac=self.style.dispcol['target'], add_width=add_width)
                        self.draw_line(coord[0], coord[1], lc=self.style.dispcol['cx'])
                    elif gate.type == GateType.swap:
                        self.draw_swap(coord[0])
                        self.draw_swap(coord[1])
                        self.draw_line(bottom, top, lc=self.style.dispcol['swap'])
                    elif gate.controls == 1:
                        disp = gate.qasm_name.replace('c', '')

                        color = None
                        if self.style.name != 'bw':
                            color = self.style.dispcol['multi']

                        self.draw_ctrl_qubit(coord[0], fc=color, ec=color)
                        if param:
                            self.draw_gate(coord[1],
                                           text=disp,
                                           fc=color,
                                           p_string='{}'.format(param))
                        else:
                            self.draw_gate(coord[1], text=disp,
                                           fc=color)
                        # add qubit-qubit wiring
                        self.draw_line(bottom, top, lc=color)
                    else:
                        if param:
                            subtext = '{}'.format(param)
                        else:
                            subtext = ''
                        self.draw_multiqubit_gate(coord, fc=self.style.dispcol['multi'], ec=self.style.dispcol['multi'],
                                                  gt=self.style.gt, sc=self.style.sc,
                                                  text=gate.qasm_name, subtext=subtext)
                elif len(coord) == 3:
                    if gate.type == GateType.ccx:
                        self.draw_ctrl_qubit(coord[0], fc=self.style.dispcol['multi'],
                                             ec=self.style.dispcol['multi'])
                        self.draw_ctrl_qubit(coord[1], fc=self.style.dispcol['multi'],
                                             ec=self.style.dispcol['multi'])
                        if self.style.name != 'bw':
                            self.draw_tgt_qubit(coord[2], fc=self.style.dispcol['multi'],
                                                ec=self.style.dispcol['multi'],
                                                ac=self.style.dispcol['target'])
                        else:
                            self.draw_tgt_qubit(coord[2], fc=self.style.dispcol['target'],
                                                ec=self.style.dispcol['multi'],
                                                ac=self.style.dispcol['multi'])
                        # add qubit-qubit wiring
                        self.draw_line(bottom, top, lc=self.style.dispcol['multi'])
                    elif gate.type == GateType.cswap:
                        self.draw_ctrl_qubit(coord[0], fc=self.style.dispcol['multi'],
                                             ec=self.style.dispcol['multi'])
                        self.draw_swap(coord[1])
                        self.draw_swap(coord[2])
                        self.draw_line(bottom, top, lc=self.style.dispcol['swap'])
                    elif gate.controls > 0:
                        for i in range(gate.controls):
                            self.draw_ctrl_qubit(coord[i], fc=self.style.dispcol['multi'],
                                                 ec=self.style.dispcol['multi'])
                        if param:
                            subtext = '{}'.format(param)
                        else:
                            subtext = ''
                        if gate.targets >= 2:
                            self.draw_multiqubit_gate(coord[gate.controls:], fc=self.style.dispcol['multi'],
                                                      ec=self.style.dispcol['multi'],
                                                      gt=self.style.gt, sc=self.style.sc,
                                                      text=gate.qasm_name, subtext=subtext)
                        else:
                            self.draw_gate(coord[-1],
                                           text=gate.qasm_name[gate.controls:],
                                           fc=self.style.dispcol['multi'],
                                           p_string=subtext)
                        self.draw_line(bottom, top, lc=self.style.dispcol['swap'])
                    else:
                        if param:
                            subtext = '{}'.format(param)
                        else:
                            subtext = ''
                        self.draw_multiqubit_gate(coord, fc=self.style.dispcol['multi'],
                                                  ec=self.style.dispcol['multi'],
                                                  gt=self.style.gt, sc=self.style.sc,
                                                  text=gate.qasm_name, subtext=subtext)
                elif len(coord) > 3:
                    self.draw_multiqubit_gate(
                        coord, fc=self.style.dispcol['multi'],
                        ec=self.style.dispcol['multi'],
                        gt=self.style.gt, sc=self.style.sc,
                        text=gate.qasm_name, subtext=""
                    )

            layer_position.append(position)
            position = position + layer_width
        layer_position.append(position)

        temp_ac = [anchors[i].get_index() for i in range(cir_len)]
        max_anc = max(temp_ac)
        n_fold = max(0, max_anc - 1) // FOLD
        # window size
        if max_anc > FOLD > 0:
            now['max_x'] = FOLD + 1 + offset_x
            now['max_y'] = (n_fold + 1) * (cir_len + 1) - 1
        else:
            now['max_x'] = max_anc + 1 + offset_x
            now['max_y'] = cir_len
        # add horizontal lines

        now['max_x'] = max(5, now['max_x'])

        for ii in range(n_fold + 1):
            self.draw_regs_sub(ii, offset_x, now, name_dict)
        # draw gate number
        if self.style.index:
            for ii in range(max_anc):
                if FOLD > 0:
                    x_coord = ii % FOLD + 1
                    y_coord = - (ii // FOLD) * (cir_len + 1) + 0.7
                else:
                    x_coord = ii + 1
                    y_coord = 0.7
                self.ax.text(x_coord, y_coord, str(ii + 1), ha='center',
                             va='center', fontsize=self.style.sfs,
                             color=self.style.tc, clip_on=True,
                             zorder=PORDER_TEXT)
        if show_depth and len(layers) >= 2:
            depth_origin = []
            last_i = 0
            last_occupy = layers[0].occupy
            for i in range(1, len(layers)):
                if len(layers[i].occupy & last_occupy) == 0:
                    last_occupy |= layers[i].occupy
                else:
                    if i - last_i >= 2:
                        depth_origin.append((last_i, i - 1))
                    last_i = i
                    last_occupy = layers[i].occupy
            for depth in depth_origin:
                start, end = depth
                self.draw_depth(layer_position[start], layer_position[end + 1])

        _xl = - self.style.margin[0]
        _xr = now['max_x'] + self.style.margin[1]
        _yb = - now['max_y'] - self.style.margin[2] + 1 - 0.5
        _yt = self.style.margin[3] + 0.5
        self.ax.set_xlim(_xl, _xr)
        self.ax.set_ylim(_yb, _yt)
        fig_w = _xr - _xl
        fig_h = _yt - _yb
        if self.style.figwidth < 0.0:
            self.style.figwidth = fig_w * 4.3 * self.style.fs / 72 / WID
        self.figure.set_size_inches(self.style.figwidth, self.style.figwidth * fig_h / fig_w)

        if save_file:
            filename = f"{circuit.name}.jpg" if filename is None else filename

        if filename is not None:
            self.figure.savefig(filename, dpi=self.style.dpi,
                                bbox_inches='tight')
