from mhi.common.codec import SimpleCodec
from mhi.common.colour import Colour
from mhi.common.arrow import Arrow
from .component import Component
from .remote import Remotable, rmi, rmi_property

#===============================================================================
# Codecs
#===============================================================================

_colour_codec = Colour()
_arrow_codec = Arrow()

# Divider line style
_line_style_codec = SimpleCodec(Solid=0, Dash=1, Dot=2, DashDot=3)
_line_style_codec.keywords('style')

# Divider line weights
_weight_codec = SimpleCodec({'0.2':0, '0.4':1, '0.6':2, '0.8':3, '1.0':4,
                             '1.2':5, '1.4':6})
_weight_codec.alternates({'0.2 pt':0, '0.4 pt':1, '0.6 pt':2, '0.8 pt':3,
                          '1.0 pt':4, '1.2 pt':5, '1.4 pt':6})
_weight_codec.keywords('weight')


#===============================================================================
# Enerplot Line (Divider & ...?)
#===============================================================================

class Line(Component):
    """
    Divider Line
    """

    def _codecs(self):
        return (_colour_codec, _line_style_codec, _weight_codec)

    def horizontal(self, width):
        """
        Change the line to be horizontal, with the given length.

        Parameters:
            width (int): Length of the horizontal line

        Returns:
            self, to allow fluent-style chained commands.
        """

        if width < 1:
            raise ValueError("Width must be positive")
        self.size(width=width, height=0)
        return self

    def vertical(self, height):
        """
        Change the line to be vertical, with the given length.

        Parameters:
            width (int): Length of the horizontal line

        Returns:
            self, to allow fluent-style chained commands.
        """

        if height < 1:
            raise ValueError("Height must be positive")
        self.size(width=0, height=height)
        return self

    def flat(self, style=None, weight=None, colour=None):
        """
        Change the line to be a "flat" (non-3D) line.
        Optionally change the line's style, weight and/or colour.

        Parameters:
            style (str): new style ``Solid``, ``Dash``, ``Dot`` or ``DotDash``
            weight (str): new weight (``"0.2 pt"`` to ``"1.4 pt"``
                in increments of 0.2 pt)
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        self.properties(state=0, style=style, weight=weight, true̵color=colour)
        return self

    def solid(self, weight=None, colour=None):
        """
        Change the line to be a solid, non-3D line.
        Optionally change the line's weight and/or colour.

        Parameters:
            weight (str): new weight (``"0.2 pt"`` to ``"1.4 pt"``
                in increments of 0.2 pt)
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        return self.flat('Solid', weight, colour)

    def dashed(self, weight=None, colour=None):
        """
        Change the line to be a dashed, non-3D line.
        Optionally change the line's weight and/or colour.

        Parameters:
            weight (str): new weight (``"0.2 pt"`` to ``"1.4 pt"``
                in increments of 0.2 pt)
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        return self.flat('Dash', weight, colour)

    def dotted(self, weight=None, colour=None):
        """
        Change the line to be a dotted, non-3D line.
        Optionally change the line's weight and/or colour.

        Parameters:
            weight (str): new weight (``"0.2 pt"`` to ``"1.4 pt"``
                in increments of 0.2 pt)
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        return self.flat('Dot', weight, colour)

    def dot_dash(self, weight=None, colour=None):
        """
        Change the line to be a dot-dashed, non-3D line.
        Optionally change the line's weight and/or colour.

        Parameters:
            weight (str): new weight (``"0.2 pt"`` to ``"1.4 pt"``
                in increments of 0.2 pt)
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        return self.flat('DotDash', weight, colour)

    def raised(self, colour=None):
        """
        Change the line to be a raised, 3D line.
        Optionally change the line's colour.

        Parameters:
            colour: new colour (``"red"``, ``"#FF0000"``, ...)

        Returns:
            self, to allow fluent-style chained commands.
        """

        self.properties(state=1, true̵color=colour)
        return self


#===============================================================================
# Enerplot TextArea (Sticky Notes & Captions)
#===============================================================================

class TextArea(Component):
    """
    Text Area - Sticky Notes & Captions
    """

    text = rmi_property(True, True, doc="Text in the text area", name='text')

    def _codecs(self):
        return (_colour_codec, _arrow_codec)

    def colour(self, foreground=None, background=None):
        """
        Alter the foreground and/or background colours of the Text Area.

        Parameters:
            foreground (colour): Desired foreground colour
            background (colour): Desired foreground colour

        Returns:
            self, to allow fluent-style chained commands.
        """
        self.properties(fg_color=foreground, bg_color=background)
        return self

    def arrows(self, *args, add=None, remove=None):
        """
        Get or set the arrows on the Text Area.

        With no arguments, the current arrows are returned as a string.

        If any positional arguments are given, the arrows are set to the
        indicated directions only.

        If the `add` keyword argument is specified, these arrows
        are added on the text area, joining any existing arrows.

        If the `remove` keyword argument is specified, these arrows
        are removed from the text area.

        The direction arrows may be given as iterable group of strings,
        or as a space-separated string.

        Parameters:
            *args: arrow directions to set on the Text Area
            add: arrow directions to add to the Text Area
            remove: arrow directions to remove from the Text Area

        Returns:
            - a string describing the current arrow configuration, or
            - self, to allow fluent-style chained commands

        Examples::

            note.arrows("N", "NE")  # Set North & North-East arrows only.
            note.arrows("N NE")     # Set North & North-East arrows only.
            note.arrows(add="N NE") # Add the North & North-East arrows.
            note.arrows(remove=("N", "NE")) # Remove those arrows.
        """

        arrows = 0 if args else int(self['arrows'])

        if args or add or remove:
            for arg in args:
                arrows |= _arrow_codec.encode(arg)

            arrows |= _arrow_codec.encode(add)
            arrows &= ~_arrow_codec.encode(remove)
            self['arrows'] = arrows
            return self
        else:
            return _arrow_codec.decode(arrows)
