import os
import mhi.common.path

from mhi.common.collection import IndexableDict
from mhi.common.codec import SimpleCodec
from .component import Component
from .remote import Remotable, rmi, rmi_property, requires

#===============================================================================
# Codecs
#===============================================================================

_pagesize = SimpleCodec({'A/A4': 0, 'B/A3': 1, 'C/A2': 2, 'D/A1': 3,
                         'Oversize':4})
_pagesize.alternates({'A': 0, 'B': 1, 'C': 2, 'D': 3,
                      'A4': 0, 'A3': 1, 'A2': 2, 'A1': 3,
                      '8.5x11':0, '11x17':1, '17x22':2, '22x34':3, '34x44': 4})

_orient = SimpleCodec(Portrait=0, Landscape=1)

#===============================================================================
# Enerplot Books
#===============================================================================

class Book(Remotable):

    """
    An Enerplot Book holds one or more sheets, which in turn will hold
    graph frames for viewing curve data.
    """

    @property
    def name(self):
        """
        The name of the book (read-only)
        """
        return self._identity['name']

    @rmi_property
    def file(self):
        """
        The book's filename (read-only)
        """

    @rmi_property
    def description(self):
        """
        The book's description (read-only)
        """

    header = rmi_property(True, True, doc="Header Text", name='header')

    title = rmi_property(True, True, doc="Header Title", name='title')

    footer_left = rmi_property(True, True, doc="Left footer",
                               name='footer_left')
    footer_center = rmi_property(True, True, doc="Centre footer",
                                 name='footer_center')
    footer_right = rmi_property(True, True, doc="Right footer",
                                name='footer_right')

    @rmi
    def unload(self):
        """
        Unload this book

        The book is unloaded from the Enerplot workspace.

        Warning:

            Any changes made to the book, which have not explicitly been
            saved, will be lost.  Call :meth:`save` or :meth:`save_as`
            before unloading to preserve changes.
        """

    @requires('1.1')
    @rmi
    def reload(self):
        """
        Reload this book

        The book is reloaded into the Enerplot workspace.

        Warning:

            Any changes made to the book, which have not explicitly been
            saved, will be lost.  Call :meth:`save` or :meth:`save_as`
            before reloading to preserve changes.

        .. versionadded:: 2.3
        """

    @rmi_property
    def dirty(self) -> bool:
        """
        Has the book been modified since it was last saved (read-only)

        .. versionadded:: 2.3
        """

    @requires('1.1')
    def is_dirty(self) -> bool:
        """
        Check if the project contains unsaved changes

        Returns:
            `True`, if unsaved changes exist, `False` otherwise.

        .. versionadded:: 2.3
        """

        return self.dirty

    #-----------------------------------------------------------------------
    # Save / Save as
    #-----------------------------------------------------------------------

    @rmi
    def _save(self, path=None):
        pass

    def save(self):
        """
        Save all changes in book
        """

        self._save()

    def save_as(self, path, folder=None):
        """
        Save book to a new path location

        Parameters:
            path (str): location to store the book.
                The extension .epbx is appended if not present.

            folder (str): If provided, the path to the book is resolved
                relative to this folder.
        """

        if not path.endswith(".epbx"):
            path += '.epbx'

        if folder:
            path = os.path.join(folder, path)

        path = mhi.common.path.expand_path(path, abspath=True)

        name = os.path.splitext(os.path.basename(path))[0]

        enerplot = self._context._main

        try:
            book = enerplot.book(name)

            # Ok to save to the same name in a new location;
            # not ok to save to the name of an existing book, otherwise.
            if self._identity != book._identity:
                raise ValueError("Book %r already exists" % name)
        except Exception:
            pass

        self._save(path)

        book = enerplot.book(name)
        if self._identity != book._identity:
            self._identity = book._identity

    #-----------------------------------------------------------------------
    # Sheets
    #-----------------------------------------------------------------------

    @rmi
    def _sheets(self):
        """
        List all of the sheets in this book

        Returns:
            List[Sheet]: the list of sheets.
        """

    def sheets(self):
        """
        List all of the sheets in this book.

        Returns:
            IndexableDict[str,Sheet]: An indexable dictionary of sheets.
        """

        sheets = self._sheets()
        return IndexableDict((sheet.name, sheet) for sheet in sheets)

    @rmi
    def sheet(self, name):
        """
        Retrieve a sheet reference, by name

        Parameters:
            name (str): the name of the sheet

        Returns:
            Sheet: the named sheet (if present)
        """

    @rmi
    def _new_sheet(self, name, description):
        """Create a new sheet"""

    def new_sheet(self, name="", description=""):
        """
        Create a new sheet

        Parameters:
            name (str): The desired sheet name; if not provided, "Sheet#" will
                be used.

            description (str): a description to be given to the sheet.

        Returns:
            Sheet: the created sheet.
        """

        return self._new_sheet(name, description)

    #-----------------------------------------------------------------------
    # Components
    #-----------------------------------------------------------------------

    @rmi
    def _find(self, _id, classid=None):
        """
        Find a component in a book by id number and classid.

        This function exists for backward compatibility only.
        Other find functions are easier to use.

        Parameters:
            _id (int): The component's ID number
            classid (str): The component's class-id

        Returns:
            Component: the identified component
        """

    #-----------------------------------------------------------------------
    # Link/Unlink
    #-----------------------------------------------------------------------

    @rmi
    def delink_all(self):
        """
        Delink all channel data from book
        """

    @rmi
    def relink_all(self, datafile):
        """
        Relink the channel data to the given datafile

        Parameters:
            datafile (DataFile): the datafile to link channel data to.
        """



#===============================================================================
# Enerplot Sheet
#===============================================================================

class Sheet(Component):

    """
    An Enerplot Sheet
    """

    @rmi_property
    def name(self):
        """
        The name of the sheet (read-only)
        """

    @rmi_property
    def description(self):
        """
        The description of the sheet (read-only)
        """

    @rmi
    def focus(self):
        """
        Switches the currently focused sheet to become this sheet.
        """

    #---------------------------------------------------------------------------
    # Properties (Grid, Orientation, Size)
    #---------------------------------------------------------------------------

    @property
    def grid(self):
        """
        Set to `True` to show a grid on the canvas, `False` otherwise.
        """

        return self['show_grid'] != '0'

    @grid.setter
    def grid(self, value):
        self['show_grid'] = 1 if value else 0

    #---------------------------------------------------------------------------

    @property
    def orientation(self):
        """
        Set to `"Landscape"` to orient the paper horizontally,
        `"Portrait"` to orient vertically.
        """

        return _orient.decode(self['orient'])

    @orientation.setter
    def orientation(self, value):
        self['orient'] = _orient.encode(value)

    @property
    def portrait(self):
        """
        `True` if the sheet is oriented vertically, `False` otherwise.
        """

        return self['orient'] == '0'

    @property
    def landscape(self):
        """
        `True` if the sheet is oriented horizontally, `False` otherwise.
        """

        return self['orient'] != '0'

    #---------------------------------------------------------------------------

    @property
    def pagesize(self):
        """
        The size of the canvas.

        The size may be set by US name `"A"` or metric name `"A4"`, or by
        dimension in inches `"8.5x11"`.  The following statements all set the
        same canvas size::

            >>> sheet.pagesize = 'A/A4'
            >>> sheet.pagesize = 'A4'
            >>> sheet.pagesize = 'A'
            >>> sheet.pagesize = '8.5x11'
            >>> sheet.pagesize
            'A/A4'
        """

        return _pagesize.decode(self['size'])

    @pagesize.setter
    def pagesize(self, value):
        self['size'] = _pagesize.encode(value)


    #---------------------------------------------------------------------------
    # Removing components
    #---------------------------------------------------------------------------

    @rmi
    def remove(self, *components):
        """
        Remove components from the sheet
        """


    #---------------------------------------------------------------------------
    # Create child components
    #---------------------------------------------------------------------------

    @rmi
    def _create(self, classid, **attrs):
        pass

    def sticky(self, x=None, y=None, w=None, h=None, text=None, **kwargs):
        """
        Create a "Sticky Note" styled TextArea

        Parameters:
            x (int): x location for the Sticky Note
            y (int): y-location for the Sticky Note
            w (int): width of the Sticky Note
            h (int): height of the Sticky Note
            text (str): the contents of the sticky note
            **kwargs: Additional key=value properties for the TextArea.

        Returns:
            TextArea: the sticky note

        Example::

            note = sheet.sticky(1, 1, 8, 3, "Hello world", arrows="NE E SE",
                                fg_color='yellow', bg_color='black')
        """

        sticky = self._create("Sticky", x=x, y=y, w=w, h=h)
        sticky.properties(**kwargs)
        if text is not None:
            sticky.text = text
        return sticky

    def caption(self, x=None, y=None, w=20, h=2, text="Caption", **kwargs):
        """
        Create a "Caption" styled TextArea

        Parameters:
            x (int): x location for the Caption
            y (int): y-location for the Caption
            w (int): width of the Caption
            h (int): height of the Caption
            text (str): the contents of the Caption
            **kwargs: Additional key=value properties for the TextArea.

        Returns:
            TextArea: the caption

        Example::

            caption = sheet.caption(1, 5, 8, 2, "Output", fg_color='red')
        """

        options = dict(style=0, align=1, full_font='Tahoma, 16pt')
        options.update(kwargs)

        caption = self._create("Sticky", x=x, y=y, w=w, h=h)
        caption.properties(**options)
        if text is not None:
            caption.text = text
        return caption


    def divider(self, x=None, y=None, w=None, h=None, **kwargs):
        """
        Create a "Divider"

        Parameters:
            x (int): x location for the start of Divider
            y (int): y-location for the start of Divider
            w (int): width of the Divider (if horizontal)
            h (int): height of the Divider (if vertical)
            **kwargs: Additional key=value properties for the note.

        Returns:
            Line: the divider

        Example::

            divider = sheet.divider(1, 10, 6, 0, state=0, style='Dash')
        """

        if w and (h is None):
            h = 0
        elif h and (w is None):
            w = 0
        elif w and h:
            raise ValueError("Width and height must not both be given")

        divider = self._create("Divider", x=x, y=y, w=w, h=h)
        if kwargs:
            divider.properties(**kwargs)
        return divider

    def graph_frame(self, x=None, y=None, w=None, h=None, **kwargs):
        """
        Create a "Graph Frame"

        Parameters:
            x (int): x location for the start of Frame
            y (int): y-location for the start of Frame
            w (int): width of the Frame
            h (int): height of the Frame
            **kwargs: Additional key=value properties for the frame.

        Returns:
            GraphFrame: the graph frame
        """

        graph_frame = self._create("GraphFrame", x=x, y=y, w=w, h=h)
        if kwargs:
            graph_frame.properties(**kwargs)
        return graph_frame


    def plot_frame(self, x=None, y=None, w=None, h=None, **kwargs):
        """
        Create a "Plot Frame" for X-Y plots

        Parameters:
            x (int): x location for the start of Frame
            y (int): y-location for the start of Frame
            w (int): width of the Frame
            h (int): height of the Frame
            **kwargs: Additional key=value properties for the frame.

        Returns:
            PlotFrame: the x-y plot frame
        """

        plot_frame = self._create("PlotFrame", x=x, y=y, w=w, h=h)
        if kwargs:
            plot_frame.properties(**kwargs)
        return plot_frame


    def fft_frame(self, x=None, y=None, w=None, h=None, **kwargs):
        """
        Create a "FFT Frame" for FFT Graphs

        Parameters:
            x (int): x location for the start of Frame
            y (int): y-location for the start of Frame
            w (int): width of the Frame
            h (int): height of the Frame
            **kwargs: Additional key=value properties for the frame.

        Returns:
            FFTFrame: the FFT graph frame
        """

        fft_frame = self._create("FFTFrame", x=x, y=y, w=w, h=h)
        if kwargs:
            fft_frame.properties(**kwargs)
        return fft_frame
