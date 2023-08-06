

import tkinter as T
from dataclasses import dataclass
from typing import Any, Dict, NewType, Sequence, Tuple, Union
from typing_extensions import Self




LayOut2D = NewType('LayOut2D', Sequence[Sequence[ Union[None,T.Widget] ]])




@dataclass
class GridLayout:
    """ # `GridLayout(widget)`

        Create a helper to manage the grid of the widget passed to the constructor. Can handle
        rows and columns characteristics, widgets placement and spanning.
    """

    holder: T.Widget


    def col_weights(self, *weights:int) -> Self :
        """ Define the weight for each column of the grid, using varargs. """
        return self.__applier('columnconfigure', 'weight', weights)

    def row_weights(self, *weights:int) -> Self :
        """ Define the weight for each row of the grid, using varargs. """
        return self.__applier('rowconfigure', 'weight', weights)

    def col_minsizes(self, *minsizes:int) -> Self :
        """ Define the minsizes for each column of the grid, using varargs. """
        return self.__applier('columnconfigure', 'minsize', minsizes)

    def row_minsizes(self, *minsizes:int) -> Self :
        """ Define the minsizes for each row of the grid, using varargs. """
        return self.__applier('rowconfigure', 'minsize', minsizes)


    def __applier(self, row_or_col:str, option:str, values:Sequence) -> Self :
        grid_method = getattr(self.holder, row_or_col)
        for i,value in enumerate(values):
            grid_method(i, **{option:value})
        return self


    def weights(self, *, cols:Tuple[int]=(1,), rows:Tuple[int]=(1,)) -> Self :
        """ Alternative to do both `GridLayout.col_weights` and `GridLayout.row_weights` calls
            one shot.

            Parameters:
                cols: tuple of weights for the columns
                rows: tuple of weights for the rows

            !!! note
                On the contrary of the isolated calls through [col_weights]
                [src.tkutils.grid_layout.GridLayout.col_weights] and [row_weights]
                [src.tkutils.grid_layout.GridLayout.row_weights], if one of the dimensions isn't given, it
                will be automatically handled to make it one row/column filling with a weight of 1.
        """
        self.col_weights(*cols)
        self.row_weights(*rows)
        return self


    def minsizes(self, *, cols:Tuple[int]=(None,), rows:Tuple[int]=(None,)) -> Self :
        """ Alternative to do `GridLayout.col_minsizes` and `GridLayout.row_minsizes` one shot.

            Parameters:
                cols: tuple of minimal sizes (in pixels) for the columns
                rows: tuple of minimal sizes (in pixels) for the rows
        """
        self.col_minsizes(*cols)
        self.row_minsizes(*rows)
        return self



    def fill_with(
        self,
        grid:LayOut2D,
        *,
        pad:int = 5,
        sticky:str = T.EW,
        specials:Dict[T.Widget, Dict]=None,
        **options:Any,
    ) -> Self :
        """ Given a grid of widgets as a 2D-array (`Layout2D`) and a bunch of options, determine
            automatically  the placement of all the widgets in the grid (and their "spanning" if
            any), and apply automatically the wanted options on each widget.

            !!! tip
                If some cells of the LayOut2D grid must stay empty, use `None` for them.

                To get a "spanning widget" over several cells, put the reference to the widget in
                adjacent cells. Note that the spanning widget must cover a rectangular area in the
                LayOut2D.

            The grid options applied to the widgets are controlled using the following way:

            * `pad` and `sticky` arguments are applied to all the widgets of the grid (note: `pad` is
              assigned to `padx` and `pady`)
            * The `**options` kwargs are any option that could be used with a `widget.grid(...)`.
              They will override `pad` and `sticky` arguments and will be applied to all widgets in
              the grid.
            * For fine tuning, the `specials` keyword argument can be used, as a dictionary of
              widgets associated to dictionaries of grid options. Those options can define specific
              values and/or override generic ones for a specific widget in the grid.

            !!! tip
                Precedence order for the different options arguments to configure a widget grid cell:

                `pad, sticky  <  options  <  specials[widget]`

            Parameters:
                grid:       2D-array layout of widgets references
                pad:        Default value applied to padx and pady for all widgets in the grid
                sticky:     Default value  applied to all widgets in the grid
                specials:   Specific grid options to use for a specific widget. Provided as a
                            `Dict[Widget,Options]`, the `specials` will override any other generic
                            option.
                **options:  Options usable when using the widget.grid(...) method. If defined, they
                            are overriding `pad` and `sticky` related options. `options` are applied
                            to all the widgets in the grid.

            Raises:
                ValueError: If the `grid` isn't rectangular.
                ValueError: If some spanning widgets aren't covering a rectangular area of the grid
                            (`w * h` references).
        """

        lengths = set(map(len,grid))
        if len(lengths) != 1:
            raise ValueError(f"Some row lengths are mismatched: {lengths}")


        options  = {'padx':pad, 'pady':pad, 'sticky':sticky, **options}
        specials = specials or {}


        refs: Dict[T.Widget,_GridRef] = {}

        for i,row in enumerate(grid):
            for j,widget in enumerate(row):

                if widget is None: continue     # pylint: disable=multiple-statements

                if widget not in refs:
                    w_options = {**options, **specials[widget]} if widget in specials else options
                    refs[widget] = _GridRef(widget, w_options)

                ref = refs[widget]
                ref.at(i,j)


        for ref in refs.values():
            ref.apply()

        return self


    # def expandable(self, *, fill_h=True, fill_v=True):
    #     """ Makes the current widget a single cell that will resize automatically in
    #         one or both directions.

    #         @fill_h=True:   expand horizontally
    #         @fill_v=True:   expand vertically
    #     """
    #     if fill_v:
    #         self.holder.rowconfigure(0, weight=1)
    #     if fill_h:
    #         self.holder.columnconfigure(0, weight=1)
    #     return self


    # def expanse(self, row=0, col=0, pad=0, sticky=T.NSEW):
    #     """ Typically used on Frame widget, so that they become automatically resizable.
    #         `pad`=0:         add padding around the cell
    #         `sticky`=T.NSEW: how the content should adapt.
    #     """
    #     if not isinstance(self.holder, T.Tk):
    #         self.holder.grid(row=row, column=col, padx=pad, pady=pad, sticky=sticky)
    #     return self








class _GridRef:
    """ Helper class to handle GridLayout.fill_with(...) logic """

    def __init__(self, widget:T.Widget, options:Dict):
        self.widget = widget        # Widget to put in the grid
        self.options=options        # Grid options for that widget (already merged with specials)
        self.coords = set()         # All cells coordinates for the widget in LayOut2D


    def __hash__(self):
        return hash(self.widget)


    def at(self, i:int, j:int):                 # pylint: disable=invalid-name
        """ Register the widget at the given position in the grid """
        self.coords.add((i,j))


    def apply(self):
        """ Analyze the positions where the widget has been registered and check they are
            consistent with a rectangle.
            If so, determine the column and row spans to use, then apply the grid logic
        """
        i, height = self.__min_max(0)
        j, width  = self.__min_max(1)
        n_refs    = len(self.coords)
        if height*width != n_refs:
            raise ValueError(
                f"Shape isn't rectangular for {self.widget}: h*w = {height}*{width} != {n_refs}"
            )

        self.options.update({
            'row':i,    'rowspan':height,
            'column':j, 'columnspan':width,
        })
        self.widget.grid(**self.options)


    def __min_max(self, dim:int):
        """ Return a tuple (int,int), with the min coordinate for the current widget on the given
            dimension, and its size for that dimension.
        """
        data = tuple(coords[dim] for coords in self.coords)
        low  = min(data)
        size = max(data) - low + 1
        return low, size
