# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
A module for drawing circuits in ascii art or some other text representation
"""

import sys
from shutil import get_terminal_size
from warnings import warn
import numpy as np

from QuICT.core.gate import *


MAX_FRAC = 16
N, D = np.meshgrid(np.arange(1, MAX_FRAC + 1), np.arange(1, MAX_FRAC + 1))
FRAC_MESH = N / D * np.pi
RECIP_MESH = N / D / np.pi
POW_LIST = np.pi ** np.arange(2, 5)


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


def pi_check(inpt, eps=1e-6, output='text', ndigits=5):
    """ Computes if a number is close to an integer
    fraction or multiple of PI and returns the
    corresponding string.

    Args:
        inpt (float): Number to check.
        eps (float): EPS to check against.
        output (str): Options are 'text' (default),
                      'latex', 'mpl', and 'qasm'.
        ndigits (int): Number of digits to print
                       if returning raw inpt.

    Returns:
        str: string representation of output.

    """

    def normalize(single_inpt):
        if abs(single_inpt) < 1e-14:
            return '0'

        if output == 'text':
            pi = 'π'
        elif output == 'qasm':
            pi = 'pi'
        elif output == 'latex':
            pi = '\\pi'
        elif output == 'mpl':
            pi = '$\\pi$'
        else:
            raise Exception('pi_check parameter output should be text, '
                            'latex, mpl, or qasm.')

        neg_str = '-' if single_inpt < 0 else ''

        # First check is for whole multiples of pi
        val = single_inpt / np.pi
        if abs(val) >= 1 - eps:
            if abs(abs(val) - abs(round(val))) < eps:
                val = int(abs(round(val)))
                if abs(val) == 1:
                    str_out = '{}{}'.format(neg_str, pi)
                else:
                    if output == 'qasm':
                        str_out = '{}{}*{}'.format(neg_str, val, pi)
                    else:
                        str_out = '{}{}{}'.format(neg_str, val, pi)
                return str_out

        # Second is a check for powers of pi
        if abs(single_inpt) > np.pi:
            power = np.where(abs(abs(single_inpt) - POW_LIST) < eps)
            if power[0].shape[0]:
                if output == 'qasm':
                    str_out = '{:.{}g}'.format(single_inpt, ndigits)
                elif output == 'latex':
                    str_out = '{}{}^{}'.format(neg_str, pi, power[0][0] + 2)
                elif output == 'mpl':
                    str_out = '{}{}$^{}$'.format(neg_str, pi, power[0][0] + 2)
                else:
                    str_out = '{}{}**{}'.format(neg_str, pi, power[0][0] + 2)
                return str_out

        # Third is a check for a number larger than MAX_FRAC * pi, not a
        # multiple or power of pi, since no fractions will exceed MAX_FRAC * pi
        if abs(single_inpt) >= (MAX_FRAC * np.pi):
            str_out = '{:.{}g}'.format(single_inpt, ndigits)
            return str_out

        # Fourth check is for fractions for 1*pi in the numer and any
        # number in the denom.
        val = np.pi / single_inpt
        if abs(abs(val) - abs(round(val))) < eps:
            val = int(abs(round(val)))
            if output == 'latex':
                str_out = '\\frac{%s%s}{%s}' % (neg_str, pi, val)
            else:
                str_out = '{}{}/{}'.format(neg_str, pi, val)
            return str_out

        # Fifth check is for fractions where the numer > 1*pi and numer
        # is up to MAX_FRAC*pi and denom is up to MAX_FRAC and all
        # fractions are reduced. Ex. 15pi/16, 2pi/5, 15pi/2, 16pi/9.
        frac = np.where(np.abs(abs(single_inpt) - FRAC_MESH) < eps)
        if frac[0].shape[0]:
            numer = int(frac[1][0]) + 1
            denom = int(frac[0][0]) + 1
            if output == 'latex':
                str_out = '\\frac{%s%s%s}{%s}' % (neg_str, numer, pi, denom)
            elif output == 'qasm':
                str_out = '{}{}*{}/{}'.format(neg_str, numer, pi, denom)
            else:
                str_out = '{}{}{}/{}'.format(neg_str, numer, pi, denom)
            return str_out

        # Sixth check is for fractions where the numer > 1 and numer
        # is up to MAX_FRAC and denom is up to MAX_FRAC*pi and all
        # fractions are reduced. Ex. 15/16pi, 2/5pi, 15/2pi, 16/9pi
        frac = np.where(np.abs(abs(single_inpt) - RECIP_MESH) < eps)
        if frac[0].shape[0]:
            numer = int(frac[1][0]) + 1
            denom = int(frac[0][0]) + 1
            if denom == 1 and output != 'qasm':
                denom = ''
            if output == 'latex':
                str_out = '\\frac{%s%s}{%s%s}' % (neg_str, numer, denom, pi)
            elif output == 'qasm':
                str_out = '{}{}/({}*{})'.format(neg_str, numer, denom, pi)
            else:
                str_out = '{}{}/{}{}'.format(neg_str, numer, denom, pi)
            return str_out

        # Nothing found
        str_out = '{:.{}g}'.format(single_inpt, ndigits)
        return str_out

    complex_inpt = complex(inpt)
    real, imag = map(normalize, [complex_inpt.real, complex_inpt.imag])

    jstr = '\\jmath' if output == 'latex' else 'j'
    if real == '0' and imag != '0':
        str_out = imag + jstr
    elif real != '0' and imag != '0':
        op_str = '+'
        # Remove + if imag negative except for latex fractions
        if complex_inpt.imag < 0 and (output != 'latex' or '\\frac' not in imag):
            op_str = ''
        str_out = '{}{}{}{}'.format(real, op_str, imag, jstr)
    else:
        str_out = real
    return str_out


class DrawElement:
    """ An element is an instruction or an operation that need to be drawn."""

    def __init__(self, label=None):
        self._width = None
        self.label = self.mid_content = label
        self.top_format = self.mid_format = self.bot_format = "%s"
        self.top_connect = self.bot_connect = " "
        self.top_pad = self._mid_padding = self.bot_pad = " "
        self.mid_bck = self.top_bck = self.bot_bck = " "
        self.bot_connector = {}
        self.top_connector = {}
        self.right_fill = self.left_fill = self.layer_width = 0
        self.wire_label = ""

    @property
    def top(self):
        """ Constructs the top line of the element"""
        if (self.width % 2) == 0 and len(self.top_format) % 2 == 1 and len(self.top_connect) == 1:
            ret = self.top_format % (self.top_pad + self.top_connect).center(self.width, self.top_pad)
        else:
            ret = self.top_format % self.top_connect.center(self.width, self.top_pad)
        if self.right_fill:
            ret = ret.ljust(self.right_fill, self.top_pad)
        if self.left_fill:
            ret = ret.rjust(self.left_fill, self.top_pad)
        ret = ret.center(self.layer_width, self.top_bck)
        return ret

    @property
    def mid(self):
        """ Constructs the middle line of the element"""
        ret = self.mid_format % self.mid_content.center(
            self.width, self._mid_padding)
        if self.right_fill:
            ret = ret.ljust(self.right_fill, self._mid_padding)
        if self.left_fill:
            ret = ret.rjust(self.left_fill, self._mid_padding)
        ret = ret.center(self.layer_width, self.mid_bck)
        return ret

    @property
    def bot(self):
        """ Constructs the bottom line of the element"""
        if (self.width % 2) == 0 and len(self.top_format) % 2 == 1:
            ret = self.bot_format % (self.bot_pad + self.bot_connect).center(self.width, self.bot_pad)
        else:
            ret = self.bot_format % self.bot_connect.center(self.width, self.bot_pad)
        if self.right_fill:
            ret = ret.ljust(self.right_fill, self.bot_pad)
        if self.left_fill:
            ret = ret.rjust(self.left_fill, self.bot_pad)
        ret = ret.center(self.layer_width, self.bot_bck)
        return ret

    @property
    def length(self):
        """ Returns the length of the element, including the box around."""
        return max(len(self.top), len(self.mid), len(self.bot))

    @property
    def width(self):
        """ Returns the width of the label, including padding"""
        if self._width:
            return self._width
        return len(self.mid_content)

    @width.setter
    def width(self, value):
        self._width = value

    def connect(self, wire_char, where, label=None):
        """Connects boxes and elements using wire_char and setting proper connectors.

        Args:
            wire_char (char): For example '║' or '│'.
            where (list["top", "bot"]): Where the connector should be set.
            label (string): Some connectors have a label (see cu1, for example).
        """

        if 'top' in where and self.top_connector:
            self.top_connect = self.top_connector[wire_char]

        if 'bot' in where and self.bot_connector:
            self.bot_connect = self.bot_connector[wire_char]

        if label:
            self.top_format = self.top_format[:-1] + (label if label else "")


class BoxOnClWire(DrawElement):
    """Draws a box on the classical wire.

    ::

        top: ┌───┐   ┌───┐
        mid: ╡ A ╞ ══╡ A ╞══
        bot: └───┘   └───┘
    """

    def __init__(self, label="", top_connect='─', bot_connect='─'):
        super().__init__(label)
        self.top_format = "┌─%s─┐"
        self.mid_format = "╡ %s ╞"
        self.bot_format = "└─%s─┘"
        self.top_pad = self.bot_pad = '─'
        self.mid_bck = '═'
        self.top_connect = top_connect
        self.bot_connect = bot_connect
        self.mid_content = label


class BoxOnQuWire(DrawElement):
    """Draws a box on the quantum wire.

    ::

        top: ┌───┐   ┌───┐
        mid: ┤ A ├ ──┤ A ├──
        bot: └───┘   └───┘
    """

    def __init__(self, label="", top_connect='─', conditional=False):
        super().__init__(label)
        self.top_format = "┌─%s─┐"
        self.mid_format = "┤ %s ├"
        self.bot_format = "└─%s─┘"
        self.top_pad = self.bot_pad = self.mid_bck = '─'
        self.top_connect = top_connect
        self.bot_connect = '╥' if conditional else '─'
        self.mid_content = label
        self.top_connector = {"│": '┴'}
        self.bot_connector = {"│": '┬'}


class MeasureTo(DrawElement):
    """The element on the classic wire to which the measure is performed.

    ::

        top:  ║     ║
        mid: ═╩═ ═══╩═══
        bot:
    """

    def __init__(self, label=''):
        super().__init__()
        self.top_connect = " ║ "
        self.mid_content = "═╩═"
        self.bot_connect = label
        self.mid_bck = "═"


class MeasureFrom(BoxOnQuWire):
    """The element on the quantum wire in which the measure is performed.

    ::

        top: ┌─┐    ┌─┐
        mid: ┤M├ ───┤M├───
        bot: └─┘    └─┘
    """

    def __init__(self):
        super().__init__()
        self.top_format = self.mid_format = self.bot_format = "%s"
        self.top_connect = "┌─┐"
        self.mid_content = "┤M├"
        self.bot_connect = "└─┘"

        self.top_pad = self.bot_pad = " "
        self._mid_padding = '─'


class MultiBox(DrawElement):
    """Elements that is draw on over multiple wires."""

    def center_label(self, input_length, order):
        """In multi-bit elements, the label is centered vertically.

        Args:
            input_length (int): Rhe amount of wires affected.
            order (int): Which middle element is this one?
        """
        if input_length == order == 0:
            self.top_connect = self.label
            return
        location_in_the_box = '*'.center(input_length * 2 - 1).index('*') + 1
        top_limit = order * 2 + 2
        bot_limit = top_limit + 2
        if top_limit <= location_in_the_box < bot_limit:
            if location_in_the_box == top_limit:
                self.top_connect = self.label
            elif location_in_the_box == top_limit + 1:
                self.mid_content = self.label
            else:
                self.bot_connect = self.label

    @property
    def width(self):
        """ Returns the width of the label, including padding"""
        if self._width:
            return self._width
        return len(self.label)


class BoxOnQuWireTop(MultiBox, BoxOnQuWire):
    """ Draws the top part of a box that affects more than one quantum wire"""

    def __init__(self, label="", top_connect=None, wire_label=''):
        super().__init__(label)
        self.wire_label = wire_label
        self.bot_connect = self.bot_pad = " "
        self.mid_content = ""  # The label will be put by some other part of the box.
        self.left_fill = len(self.wire_label)
        self.top_format = "┌─" + "s".center(self.left_fill + 1, '─') + "─┐"
        self.top_format = self.top_format.replace('s', '%s')
        self.mid_format = "┤{} %s ├".format(self.wire_label)
        self.bot_format = "│{} %s │".format(self.bot_pad * self.left_fill)
        self.top_connect = top_connect if top_connect else '─'


class BoxOnWireMid(MultiBox):
    """ A generic middle box"""

    def __init__(self, label, input_length, order, wire_label=''):
        super().__init__(label)
        self.top_pad = self.bot_pad = self.top_connect = self.bot_connect = " "
        self.wire_label = wire_label
        self.left_fill = len(self.wire_label)
        self.top_format = "│{} %s │".format(self.top_pad * self.left_fill)
        self.bot_format = "│{} %s │".format(self.bot_pad * self.left_fill)
        self.top_connect = self.bot_connect = self.mid_content = ''
        self.center_label(input_length, order)


class BoxOnQuWireMid(BoxOnWireMid, BoxOnQuWire):
    """ Draws the middle part of a box that affects more than one quantum wire"""

    def __init__(self, label, input_length, order, wire_label='', control_label=None):
        super().__init__(label, input_length, order, wire_label=wire_label)
        if control_label:
            self.mid_format = "{}{} %s ├".format(control_label, self.wire_label)
        else:
            self.mid_format = "┤{} %s ├".format(self.wire_label)


class BoxOnQuWireBot(MultiBox, BoxOnQuWire):
    """ Draws the bottom part of a box that affects more than one quantum wire"""

    def __init__(self, label, input_length, bot_connect=None, wire_label='', conditional=False):
        super().__init__(label)
        self.wire_label = wire_label
        self.top_pad = " "
        self.left_fill = len(self.wire_label)
        self.top_format = "│{} %s │".format(self.top_pad * self.left_fill)
        self.mid_format = "┤{} %s ├".format(self.wire_label)
        self.bot_format = "└─" + "s".center(self.left_fill + 1, '─') + "─┘"
        self.bot_format = self.bot_format.replace('s', '%s')
        bot_connect = bot_connect if bot_connect else '─'
        self.bot_connect = '╥' if conditional else bot_connect

        self.mid_content = self.top_connect = ""
        if input_length <= 2:
            self.top_connect = label


class BoxOnClWireTop(MultiBox, BoxOnClWire):
    """ Draws the top part of a conditional box that affects more than one classical wire"""

    def __init__(self, label="", top_connect=None, wire_label=''):
        super().__init__(label)
        self.wire_label = wire_label
        self.mid_content = ""  # The label will be put by some other part of the box.
        self.bot_format = "│ %s │"
        self.top_connect = top_connect if top_connect else '─'
        self.bot_connect = self.bot_pad = " "


class BoxOnClWireMid(BoxOnWireMid, BoxOnClWire):
    """ Draws the middle part of a conditional box that affects more than one classical wire"""

    def __init__(self, label, input_length, order, wire_label='', **_):
        super().__init__(label, input_length, order, wire_label=wire_label)
        self.mid_format = "╡{} %s ╞".format(self.wire_label)


class BoxOnClWireBot(MultiBox, BoxOnClWire):
    """ Draws the bottom part of a conditional box that affects more than one classical wire"""

    def __init__(self, label, input_length, bot_connect='─', wire_label='', **_):
        super().__init__(label)
        self.wire_label = wire_label
        self.left_fill = len(self.wire_label)
        self.top_pad = ' '
        self.bot_pad = '─'
        self.top_format = "│{} %s │".format(self.top_pad * self.left_fill)
        self.mid_format = "╡{} %s ╞".format(self.wire_label)
        self.bot_format = "└─" + "s".center(self.left_fill + 1, '─') + "─┘"
        self.bot_format = self.bot_format.replace('s', '%s')
        bot_connect = bot_connect if bot_connect else '─'
        self.bot_connect = bot_connect

        self.mid_content = self.top_connect = ""
        if input_length <= 2:
            self.top_connect = label


class DirectOnQuWire(DrawElement):
    """
    Element to the wire (without the box).
    """

    def __init__(self, label=""):
        super().__init__(label)
        self.top_format = ' %s '
        self.mid_format = '─%s─'
        self.bot_format = ' %s '
        self._mid_padding = self.mid_bck = '─'
        self.top_connector = {"│": '│'}
        self.bot_connector = {"│": '│'}


class Barrier(DirectOnQuWire):
    """Draws a barrier.

    ::

        top:  ░     ░
        mid: ─░─ ───░───
        bot:  ░     ░
    """

    def __init__(self, label=""):
        super().__init__("░")
        self.top_connect = "░"
        self.bot_connect = "░"
        self.top_connector = {}
        self.bot_connector = {}


class Ex(DirectOnQuWire):
    """Draws an X (usually with a connector). E.g. the top part of a swap gate.

    ::

        top:
        mid: ─X─ ───X───
        bot:  │     │
    """

    def __init__(self, bot_connect=" ", top_connect=" ", conditional=False):
        super().__init__("X")
        self.bot_connect = "║" if conditional else bot_connect
        self.top_connect = top_connect


class Reset(DirectOnQuWire):
    """ Draws a reset gate"""

    def __init__(self, conditional=False):
        super().__init__("|0>")
        if conditional:
            self.bot_connect = "║"


class Bullet(DirectOnQuWire):
    """ Draws a bullet (usually with a connector). E.g. the top part of a CX gate.

    ::

        top:
        mid: ─■─  ───■───
        bot:  │      │
    """

    def __init__(self, top_connect="", bot_connect="", conditional=False,
                 label=None, bottom=False):
        super().__init__('■')
        self.top_connect = top_connect
        self.bot_connect = '║' if conditional else bot_connect
        if label and bottom:
            self.bot_connect = label
        elif label:
            self.top_connect = label
        self.mid_bck = '─'


class OpenBullet(DirectOnQuWire):
    """Draws an open bullet (usually with a connector). E.g. the top part of a CX gate.

    ::

        top:
        mid: ─o─  ───o───
        bot:  │      │
    """

    def __init__(self, top_connect="", bot_connect="", conditional=False,
                 label=None, bottom=False):
        super().__init__('o')
        self.top_connect = top_connect
        self.bot_connect = '║' if conditional else bot_connect
        if label and bottom:
            self.bot_connect = label
        elif label:
            self.top_connect = label
        self.mid_bck = '─'


class EmptyWire(DrawElement):
    """This element is just the wire, with no instructions nor operations."""

    def __init__(self, wire):
        super().__init__(wire)
        self._mid_padding = self.mid_bck = wire

    @staticmethod
    def fillup_layer(layer, first_clbit):
        """Given a layer, replace the Nones in it with EmptyWire elements.

        Args:
            layer (list): The layer that contains Nones.
            first_clbit (int): The first wire that is classic.

        Returns:
            list: The new layer, with no Nones.
        """
        for nones in [i for i, x in enumerate(layer) if x is None]:
            layer[nones] = EmptyWire('═') if nones >= first_clbit else EmptyWire('─')
        return layer


class BreakWire(DrawElement):
    """ This element is used to break the drawing in several pages."""

    def __init__(self, arrow_char):
        super().__init__()
        self.top_format = self.mid_format = self.bot_format = "%s"
        self.top_connect = arrow_char
        self.mid_content = arrow_char
        self.bot_connect = arrow_char

    @staticmethod
    def fillup_layer(layer_length, arrow_char):
        """Creates a layer with BreakWire elements.

        Args:
            layer_length (int): The length of the layer to create
            arrow_char (char): The char used to create the BreakWire element.

        Returns:
            list: The new layer.
        """
        breakwire_layer = []
        for _ in range(layer_length):
            breakwire_layer.append(BreakWire(arrow_char))
        return breakwire_layer


class InputWire(DrawElement):
    """ This element is the label and the initial value of a wire."""

    def __init__(self, label):
        super().__init__(label)

    @staticmethod
    def fillup_layer(names):
        """Creates a layer with InputWire elements.

        Args:
            names (list): List of names for the wires.

        Returns:
            list: The new layer
        """
        longest = max([len(name) for name in names])
        inputs_wires = []
        for name in names:
            inputs_wires.append(InputWire(name.rjust(longest)))
        return inputs_wires


class TextDrawing:
    """ The text drawing"""

    def __init__(self, qregs, gates,
                 line_length=None, vertical_compression='high', initial_state=True,
                 encoding=None):
        self.qregs = qregs
        self.layers = self.resolution_layers(gates)
        self.layout = None
        self.initial_state = initial_state
        self.plotbarriers = True
        self.line_length = line_length
        if vertical_compression not in ['high', 'medium', 'low']:
            raise ValueError("Vertical compression can only be 'high', 'medium', or 'low'")
        self.vertical_compression = vertical_compression
        if encoding:
            self.encoding = encoding
        else:
            if sys.stdout.encoding:
                self.encoding = sys.stdout.encoding
            else:
                self.encoding = 'utf8'

    def __str__(self):
        return self.single_string()

    def _repr_html_(self):
        return '<pre style="word-wrap: normal;' \
               'white-space: pre;' \
               'background: #fff0;' \
               'line-height: 1.1;' \
               'font-family: &quot;Courier New&quot;,Courier,monospace">' \
               '%s</pre>' % self.single_string()

    def __repr__(self):
        return self.single_string()

    def single_string(self):
        """Creates a long string with the ascii art.
        Returns:
            str: The lines joined by a newline (``\\n``)
        """
        try:
            return "\n".join(self.lines()).encode(self.encoding).decode(self.encoding)
        except (UnicodeEncodeError, UnicodeDecodeError):
            warn('The encoding %s has a limited charset. Consider a different encoding in your '
                 'environment. UTF-8 is being used instead' % self.encoding, RuntimeWarning)
            self.encoding = 'utf-8'
            return "\n".join(self.lines()).encode(self.encoding).decode(self.encoding)

    def dump(self, filename, encoding=None):
        """Dumps the ascii art in the file.

        Args:
            filename (str): File to dump the ascii art.
            encoding (str): Optional. Force encoding, instead of self.encoding.
        """
        with open(filename, mode='w', encoding=encoding or self.encoding) as text_file:
            text_file.write(self.single_string())

    def lines(self, line_length=None):
        """Generates a list with lines. These lines form the text drawing.

        Args:
            line_length (int): Optional. Breaks the circuit drawing to this length. This
                               useful when the drawing does not fit in the console. If
                               None (default), it will try to guess the console width using
                               shutil.get_terminal_size(). If you don't want pagination
                               at all, set line_length=-1.

        Returns:
            list: A list of lines with the text drawing.
        """
        if line_length is None:
            line_length = self.line_length
        if not line_length:
            if ('ipykernel' in sys.modules) and ('spyder' not in sys.modules):
                line_length = 80
            else:
                line_length, _ = get_terminal_size()

        noqubits = len(self.qregs)

        layers = self.build_layers()

        layer_groups = [[]]
        rest_of_the_line = line_length
        for layerno, layer in enumerate(layers):
            # Replace the Nones with EmptyWire
            layers[layerno] = EmptyWire.fillup_layer(layer, noqubits)

            TextDrawing.normalize_width(layer)

            if line_length == -1:
                # Do not use pagination (aka line breaking. aka ignore line_length).
                layer_groups[-1].append(layer)
                continue

            # chop the layer to the line_length (pager)
            layer_length = layers[layerno][0].length

            if layer_length < rest_of_the_line:
                layer_groups[-1].append(layer)
                rest_of_the_line -= layer_length
            else:
                layer_groups[-1].append(BreakWire.fillup_layer(len(layer), '»'))

                # New group
                layer_groups.append([BreakWire.fillup_layer(len(layer), '«')])
                rest_of_the_line = line_length - layer_groups[-1][-1][0].length

                layer_groups[-1].append(
                    InputWire.fillup_layer(self.wire_names(with_initial_state=False)))
                rest_of_the_line -= layer_groups[-1][-1][0].length

                layer_groups[-1].append(layer)
                rest_of_the_line -= layer_groups[-1][-1][0].length

        lines = []

        for layer_group in layer_groups:
            wires = list(zip(*layer_group))
            lines += self.draw_wires(wires)

        return lines

    def wire_names(self, with_initial_state=False):
        """Returns a list of names for each wire.

        Args:
            with_initial_state (bool): Optional (Default: False). If true, adds
                the initial value to the name.

        Returns:
            List: The list of wire names.
        """
        if with_initial_state:
            initial_qubit_value = '|0>'
            # initial_clbit_value = '0 '
        else:
            initial_qubit_value = ''
            # initial_clbit_value = ''

        qubit_labels = []
        if self.layout is None:
            count = 0
            for bit in self.qregs:
                label = '{name}_{index}: ' + initial_qubit_value
                qubit_labels.append(label.format(name="q",
                                                 index=count,
                                                 physical=''))
                count += 1
        else:
            for bit in self.qregs:
                if self.layout[bit.index]:
                    label = '{name}_{index} -> {physical} ' + initial_qubit_value
                    qubit_labels.append(label.format(name=self.layout[bit.index].register.name,
                                                     index=self.layout[bit.index].index,
                                                     physical=bit.index))
                else:
                    qubit_labels.append('%s ' % bit.index + initial_qubit_value)

        return qubit_labels

    def should_compress(self, top_line, bot_line):
        """Decides if the top_line and bot_line should be merged,
        based on `self.vertical_compression`."""
        if self.vertical_compression == 'high':
            return True
        if self.vertical_compression == 'low':
            return False
        for top, bot in zip(top_line, bot_line):
            if top in ['┴', '╨'] and bot in ['┬', '╥']:
                return False
        for line in (bot_line, top_line):
            no_spaces = line.replace(' ', '')
            if len(no_spaces) > 0 and all(c.isalpha() or c.isnumeric() for c in no_spaces):
                return False
        return True

    def draw_wires(self, wires):
        """Given a list of wires, creates a list of lines with the text drawing.

        Args:
            wires (list): A list of wires with instructions.
        Returns:
            list: A list of lines with the text drawing.
        """
        lines = []
        bot_line = None
        for wire in wires:
            # TOP
            top_line = ''
            for instruction in wire:
                top_line += instruction.top

            if bot_line is None:
                lines.append(top_line)
            else:
                if self.should_compress(top_line, bot_line):
                    lines.append(TextDrawing.merge_lines(lines.pop(), top_line))
                else:
                    lines.append(TextDrawing.merge_lines(lines[-1], top_line, icod="bot"))

            # MID
            mid_line = ''
            for instruction in wire:
                mid_line += instruction.mid
            lines.append(TextDrawing.merge_lines(lines[-1], mid_line, icod="bot"))

            # BOT
            bot_line = ''
            for instruction in wire:
                bot_line += instruction.bot
            lines.append(TextDrawing.merge_lines(lines[-1], bot_line, icod="bot"))

        return lines

    @staticmethod
    def label_for_conditional(instruction):
        """ Creates the label for a conditional instruction."""
        return "= %s" % instruction.condition[1]

    @staticmethod
    def params_for_label(gate):
        """Get the params and format them to add them to a label. None if there
         are no params or if the params are numpy.ndarrays."""
        ret = []
        for param in gate.pargs:
            try:
                str_param = pi_check(param, ndigits=5)
                ret.append('%s' % str_param)
            except TypeError:
                ret.append('%s' % param)
        return ret

    @staticmethod
    def special_label(instruction):
        """Some instructions have special labels"""
        labels = {IGate: 'I',
                  Initialize: 'initialize',
                  UnitaryGate: 'unitary',
                  HamiltonianGate: 'Hamiltonian',
                  SXGate: '√X',
                  SXdgGate: '√XDG'}
        instruction_type = type(instruction)
        if instruction_type in {Gate, Instruction}:
            return instruction.qasm_name
        return labels.get(instruction_type, None)

    @staticmethod
    def label_for_box(instruction, controlled=False):
        """ Creates the label for a box."""
        label = instruction.qasm_name
        params = TextDrawing.params_for_label(instruction)
        if params:
            label += "(%s)" % ','.join(params)
        return label

    @staticmethod
    def merge_lines(top, bot, icod="top"):
        """Merges two lines (top and bot) in the way that the overlapping make senses.

        Args:
            top (str): the top line
            bot (str): the bottom line
            icod (top or bot): in case of doubt, which line should have priority? Default: "top".
        Returns:
            str: The merge of both lines.
        """
        ret = ""
        for topc, botc in zip(top, bot):
            if topc == botc:
                ret += topc
            elif topc in '┼╪' and botc == " ":
                ret += "│"
            elif topc == " ":
                ret += botc
            elif topc in '┬╥' and botc in " ║│" and icod == "top":
                ret += topc
            elif topc in '┬' and botc == " " and icod == "bot":
                ret += '│'
            elif topc in '╥' and botc == " " and icod == "bot":
                ret += '║'
            elif topc in '┬│' and botc == "═":
                ret += '╪'
            elif topc in '┬│' and botc == "─":
                ret += '┼'
            elif topc in '└┘║│░' and botc == " " and icod == "top":
                ret += topc
            elif topc in '─═' and botc == " " and icod == "top":
                ret += topc
            elif topc in '─═' and botc == " " and icod == "bot":
                ret += botc
            elif topc in "║╥" and botc in "═":
                ret += "╬"
            elif topc in "║╥" and botc in "─":
                ret += "╫"
            elif topc in '║╫╬' and botc in " ":
                ret += "║"
            elif topc == '└' and botc == "┌" and icod == 'top':
                ret += "├"
            elif topc == '┘' and botc == "┐":
                ret += "┤"
            elif botc in "┐┌" and icod == 'top':
                ret += "┬"
            elif topc in "┘└" and botc in "─" and icod == 'top':
                ret += "┴"
            elif botc == " " and icod == 'top':
                ret += topc
            else:
                ret += botc
        return ret

    @staticmethod
    def normalize_width(layer):
        """
        When the elements of the layer have different widths, sets the width to the max elements.

        Args:
            layer (list): A list of elements.
        """
        instructions = list(filter(lambda x: x is not None, layer))
        longest = max([instruction.length for instruction in instructions])
        for instruction in instructions:
            instruction.layer_width = longest

    @staticmethod
    def controlled_wires(instruction, layer):
        """
        Analyzes the instruction in the layer and checks if the controlled arguments are in
        the box or out of the box.

        Args:
            instruction (Instruction): instruction to analyse
            layer (Layer): The layer in which the instruction is inserted.

        Returns:
            Tuple(list, list, list):
              - tuple: controlled arguments on top of the "instruction box", and its status
              - tuple: controlled arguments on bottom of the "instruction box", and its status
              - tuple: controlled arguments in the "instruction box", and its status
              - the rest of the arguments
        """
        num_ctrl_qubits = instruction.targets
        ctrl_qubits = instruction.cargs
        args_qubits = instruction.targs
        ctrl_state = "{:b}".format(1).rjust(num_ctrl_qubits, '0')[::-1]

        in_box = list()
        top_box = list()
        bot_box = list()

        qubit_index = sorted([i for i in ctrl_qubits + args_qubits])

        for ctrl_qubit in zip(ctrl_qubits, ctrl_state):
            if min(qubit_index) > layer.qregs.index(ctrl_qubit[0]):
                top_box.append(ctrl_qubit)
            elif max(qubit_index) < layer.qregs.index(ctrl_qubit[0]):
                bot_box.append(ctrl_qubit)
            else:
                in_box.append(ctrl_qubit)
        return (top_box, bot_box, in_box, args_qubits)

    @staticmethod
    def resolution_layers(gates):
        layers = [circuit_layer()]
        for gate in gates:
            for i in range(len(layers) - 1, -2, -1):
                if i == -1 or not layers[i].checkGate(gate):
                    if i + 1 >= len(layers):
                        layers.append(circuit_layer())
                    layers[i + 1].addGate(gate)
                    break
        return layers

    def _set_ctrl_state(self, instruction, conditional, ctrl_label, bottom):
        """ Takes the ctrl_state from instruction and appends Bullet or OpenBullet
        to gates depending on whether the bit in ctrl_state is 1 or 0. Returns gates"""

        gates = []
        num_ctrl_qubits = instruction.controls
        ctrl_qubits = instruction.cargs
        cstate = "{:b}".format(1).rjust(num_ctrl_qubits, '0')[::-1]
        for i in range(len(ctrl_qubits)):
            if cstate[i] == '1':
                gates.append(Bullet(conditional=conditional, label=ctrl_label,
                                    bottom=bottom))
            else:
                gates.append(OpenBullet(conditional=conditional, label=ctrl_label,
                                        bottom=bottom))
        return gates

    def _instruction_to_gate(self, gate, layer):
        """ Convert an gates into its corresponding Gate object, and establish
        any connections it introduces between qubits"""

        current_cons = []
        connection_label = None
        ctrl_label = None
        box_label = None
        conditional = False
        # multi_qubit_instruction = gate.targets >= 2
        # label_multibox = False

        # add in a gate that operates over multiple qubits
        def add_connected_gate(gate, gates, layer, current_cons):
            for i, g in enumerate(gates):
                gate_args = gate.cargs + gate.targs
                actual_index = self.qregs.index(gate_args[i])
                if actual_index not in [i for i, j in current_cons]:
                    layer.set_qubit(gate_args[i], g)
                    current_cons.append((actual_index, g))

        ctrl_label = ""
        box_label = gate.qasm_name

        if isinstance(gate, MeasureGate):
            mgate = MeasureFrom()
            layer.set_qubit(gate.targs[0], mgate)
        elif isinstance(gate, BarrierGate):
            layer.set_qubit(gate.targ, Barrier())
        elif isinstance(gate, SwapGate):
            # swap
            gates = [Ex(conditional=conditional) for _ in range(len(gate.cargs + gate.targs))]
            add_connected_gate(gate, gates, layer, current_cons)

        elif isinstance(gate, ResetGate):
            # reset
            layer.set_qubit(gate.targs[0], Reset(conditional=conditional))

        elif isinstance(gate, RzzGate):
            # rzz
            connection_label = "ZZ(%s)" % TextDrawing.params_for_label(gate)[0]
            gates = [Bullet(conditional=conditional), Bullet(conditional=conditional)]
            add_connected_gate(gate, gates, layer, current_cons)

        elif gate.targets + gate.controls == 1:
            # unitary gate
            layer.set_qubit(gate.targ,
                            BoxOnQuWire(TextDrawing.label_for_box(gate),
                                        conditional=conditional))

        elif gate.controls >= 1:
            label = box_label if box_label is not None \
                else TextDrawing.label_for_box(gate, controlled=True)
            params_array = TextDrawing.controlled_wires(gate, layer)
            controlled_top, controlled_bot, controlled_edge, rest = params_array
            gates = self._set_ctrl_state(gate, conditional, ctrl_label,
                                         bool(controlled_bot))
            gates.append(BoxOnQuWire(label, conditional=conditional))
            add_connected_gate(gate, gates, layer, current_cons)

        elif gate.targets >= 2:
            # multiple qubit gate
            label = TextDrawing.label_for_box(gate)
            layer.set_qu_multibox(gate.targs, label, conditional=conditional)

        elif gate.targs:
            # multiple gate, involving both qargs AND cargs
            label = TextDrawing.label_for_box(gate)
            layer._set_multibox(label, qubits=gate.targs,
                                conditional=conditional)
        else:
            raise Exception(
                f"Text visualizer does not know how to handle this instruction: {gate.type}."
            )

        # sort into the order they were declared in
        # this ensures that connected boxes have lines in the right direction
        current_cons.sort(key=lambda tup: tup[0])
        current_cons = [g for q, g in current_cons]

        return layer, current_cons, connection_label

    def build_layers(self):
        """
        Constructs layers.
        Returns:
            list: List of DrawElements.
        Raises:
            VisualizationError: When the drawing is, for some reason, impossible to be drawn.
        """
        wire_names = self.wire_names(with_initial_state=self.initial_state)
        if not wire_names:
            return []

        layers = [InputWire.fillup_layer(wire_names)]

        layer = Layer(self.qregs)
        for gate_layer in self.layers:
            layer = Layer(self.qregs)
            for gate in gate_layer.gates:
                layer, current_connections, connection_label = \
                    self._instruction_to_gate(gate, layer)

                layer.connections.append((connection_label, current_connections))
            layer.connect_with("│")
            layers.append(layer.full_layer)
        return layers


class Layer:
    """ A layer is the "column" of the circuit. """

    def __init__(self, qregs):
        self.qregs = qregs
        self.qubit_layer = [None] * len(qregs)
        self.connections = []

    @property
    def full_layer(self):
        """
        Returns the composition of qubits and classic wires.
        Returns:
            String: self.qubit_layer + self.clbit_layer
        """
        return self.qubit_layer

    def set_qubit(self, qubit, element):
        """Sets the qubit to the element.

        Args:
            qubit (qbit): Element of self.qregs.
            element (DrawElement): Element to set in the qubit
        """
        self.qubit_layer[self.qregs.index(qubit)] = element

    def _set_multibox(self, label, qubits=None, top_connect=None,
                      bot_connect=None, conditional=False, controlled_edge=None):
        bits = list(qubits)
        bit_index = sorted([i for i in self.qregs if i in bits])
        wire_label_len = len(str(len(bits) - 1))
        qargs = [str(bits.index(qbit)).ljust(wire_label_len, ' ')
                 for qbit in self.qregs if qbit in bits]
        bits.sort()
        set_bit = self.set_qubit
        OnWire = BoxOnQuWire
        OnWireTop = BoxOnQuWireTop
        OnWireMid = BoxOnQuWireMid
        OnWireBot = BoxOnQuWireBot

        control_index = {}
        if controlled_edge:
            for index, qubit in enumerate(self.qregs):
                for qubit_in_edge, value in controlled_edge:
                    if qubit == qubit_in_edge:
                        control_index[index] = '■' if value == '1' else 'o'
        if len(bit_index) == 1:
            set_bit(bits[0], OnWire(label, top_connect=top_connect))
        else:
            box_height = max(bit_index) - min(bit_index) + 1
            set_bit(bits.pop(0), OnWireTop(label, top_connect=top_connect, wire_label=qargs.pop(0)))
            for order, bit_i in enumerate(range(min(bit_index) + 1, max(bit_index))):
                if bit_i in bit_index:
                    named_bit = bits.pop(0)
                    wire_label = qargs.pop(0)
                else:
                    named_bit = (self.qregs)[bit_i]
                    wire_label = ' ' * wire_label_len

                control_label = control_index.get(bit_i)
                set_bit(named_bit, OnWireMid(label, box_height, order, wire_label=wire_label,
                                             control_label=control_label))
            set_bit(bits.pop(0), OnWireBot(label, box_height, bot_connect=bot_connect,
                                           wire_label=qargs.pop(0), conditional=conditional))
        return bit_index

    def set_qu_multibox(self, bits, label, top_connect=None, bot_connect=None,
                        conditional=False, controlled_edge=None):
        """Sets the multi qubit box.

        Args:
            bits (list[int]): A list of affected bits.
            label (string): The label for the multi qubit box.
            top_connect (char): None or a char connector on the top
            bot_connect (char): None or a char connector on the bottom
            conditional (bool): If the box has a conditional
            controlled_edge (list): A list of bit that are controlled (to draw them at the edge)
        Return:
            List: A list of indexes of the box.
        """
        return self._set_multibox(label, qubits=bits, top_connect=top_connect,
                                  bot_connect=bot_connect,
                                  conditional=conditional, controlled_edge=controlled_edge)

    def connect_with(self, wire_char):
        """Connects the elements in the layer using wire_char.

        Args:
            wire_char (char): For example '║' or '│'.
        """

        if len([qbit for qbit in self.qubit_layer if qbit is not None]) == 1:
            # Nothing to connect
            return

        for label, affected_bits in self.connections:

            if not affected_bits:
                continue

            affected_bits[0].connect(wire_char, ['bot'])
            for affected_bit in affected_bits[1:-1]:
                affected_bit.connect(wire_char, ['bot', 'top'])

            affected_bits[-1].connect(wire_char, ['top'], label)

            if label:
                for affected_bit in affected_bits:
                    affected_bit.right_fill = len(label) + len(affected_bit.mid)
