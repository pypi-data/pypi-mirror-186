#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2020/3/30 11:13
# @Author  : Han Yu
# @File    : _IBMQStyle.py

from copy import copy
from warnings import warn


class DefaultStyle:
    """IBM Design Style colors
    """

    def __init__(self):
        # Set colors
        basis_color = '#FA74A6'
        clifford_color = '#6FA4FF'
        non_gate_color = '#000000'
        other_color = '#BB8BFF'
        pauli_color = '#05BAB6'
        iden_color = '#05BAB6'

        self.name = 'iqx'
        self.tc = '#000000'
        self.sc = '#000000'
        self.lc = '#000000'
        self.not_gate_lc = '#ffffff'
        self.cc = '#778899'
        self.gc = other_color
        self.gt = '#000000'
        self.bc = '#bdbdbd'
        self.bg = '#ffffff'
        self.edge_color = None
        self.math_fs = 15
        self.fs = 13
        self.sfs = 8
        self.colored_add_width = 0.2
        self.disptex = {
            'id': 'Id',
            'u0': 'U_0',
            'u1': 'U_1',
            'u2': 'U_2',
            'u3': 'U_3',
            'x': 'X',
            'y': 'Y',
            'z': 'Z',
            'h': 'H',
            's': 'S',
            'sdg': 'S^\\dagger',
            't': 'T',
            'tdg': 'T^\\dagger',
            'rx': 'R_x',
            'ry': 'R_y',
            'rz': 'R_z',
            'reset': '\\left|0\\right\\rangle',
            'barrier': 'barrier',
            'Permutation gate': 'perm',
            'Unitary gate': 'unitary',
            'phase': 'phase',
            'Custom gate': 'custom'
        }
        self.dispcol = {
            'u0': basis_color,
            'u1': basis_color,
            'u2': basis_color,
            'u3': basis_color,
            'id': iden_color,
            'x': pauli_color,
            'y': pauli_color,
            'z': pauli_color,
            'h': clifford_color,
            'cx': clifford_color,
            's': clifford_color,
            'sdg': clifford_color,
            't': other_color,
            'tdg': other_color,
            'rx': other_color,
            'ry': other_color,
            'rz': other_color,
            'reset': non_gate_color,
            'barrier': other_color,
            'target': '#ffffff',
            'swap': other_color,
            'multi': other_color,
            'meas': non_gate_color,
            'Permutation gate': other_color,
            'Unitary gate': other_color,
            'phase': other_color,
            'Custom gate': other_color
        }
        self.latexmode = False
        self.fold = None  # To be removed after 0.10 is released
        self.bundle = True
        self.index = False
        self.figwidth = -1
        self.dpi = 150
        self.margin = [2.0, 0.1, 0.1, 0.3]
        self.cline = 'doublet'

    def set_style(self, style_dic):
        dic = copy(style_dic)
        self.tc = dic.pop('textcolor', self.tc)
        self.sc = dic.pop('subtextcolor', self.sc)
        self.lc = dic.pop('linecolor', self.lc)
        self.cc = dic.pop('creglinecolor', self.cc)
        self.gt = dic.pop('gatetextcolor', self.tc)
        self.gc = dic.pop('gatefacecolor', self.gc)
        self.bc = dic.pop('barrierfacecolor', self.bc)
        self.bg = dic.pop('backgroundcolor', self.bg)
        self.fs = dic.pop('fontsize', self.fs)
        self.sfs = dic.pop('subfontsize', self.sfs)
        self.disptex = dic.pop('displaytext', self.disptex)
        self.dispcol = dic.pop('displaycolor', self.dispcol)
        self.latexmode = dic.pop('latexdrawerstyle', self.latexmode)
        self.bundle = dic.pop('cregbundle', self.bundle)
        self.index = dic.pop('showindex', self.index)
        self.figwidth = dic.pop('figwidth', self.figwidth)
        self.dpi = dic.pop('dpi', self.dpi)
        self.margin = dic.pop('margin', self.margin)
        self.cline = dic.pop('creglinestyle', self.cline)
        if 'fold' in dic:
            warn('The key "fold" in the argument "style" is being replaced by the argument "fold"',
                 DeprecationWarning, 5)
            self.fold = dic.pop('fold', self.fold)
            if self.fold < 2:
                self.fold = -1

        if dic:
            warn('style option/s ({}) is/are not supported'.format(', '.join(dic.keys())),
                 DeprecationWarning, 2)
