
import tkinter as T
from abc import ABCMeta, ABC, abstractmethod
from typing import Callable
from typing_extensions import Self




class MenuElement(metaclass=ABCMeta):
    """ Abstract class representing an element of a menu tree hierarchy. """

    parent:  T.Menu
    """ Parent menu of the current MenuElement instance """

    @abstractmethod
    def build(self, parent:T.Widget) -> Self:
        """ Method called from the MenuBuilder internals to actually build a menu.
            This method is _NOT_ to be called from anywhere else.
            The reason for it is that Menu widgets must be built in a top-down fashion,
            meaning that the complete MenuElement tree hierarchy must be built first and,
            only then, the parent widgets are passed along, step by step/top-down.
        """
        return self




class MenuElementWithCbk(MenuElement, ABC):
    """ Abstract [`MenuElement`][src.tkutils.menu_builder.bases.MenuElement]
        subclass holding a callback property (hence, parent class of either
        [`Cmd`][src.tkutils.menu_builder.menu_builder_options.Cmd],
        [`CheckBtn`][src.tkutils.menu_builder.menu_builder_options.CheckBtn],
        or [`RadioGrp`][src.tkutils.menu_builder.menu_builder_options.RadioGrp]).
    """

    cbk: Callable
    """ Callback function run when the Menu option is used.

        The callback may take no argument (for `MenuBuilder.Cmd`) or one, which will be
        the updated value of the underlying control variable.
    """


    def bind(self, widget:T.Widget, event_str:str) -> Self:
        """ Bind the given widget widget to the given event, using the callback of the current
            instance (Cmd, CheckBtn or RadioGrp).

            !!! tip "Number of arguments of `self.cbk` and their type"
                The callback will never receive see the `T.Event` argument that triggered it, but
                 it will receive the new state of the control variable of this instance, if any,
                 or no argument at all (for callbacks hold by a `Cmd` instance).

            Parameters:
                widget:    Widget to bind
                event_str: Event string identifying the event.
        """
        widget.bind(event_str, self.cbk)
        return self
