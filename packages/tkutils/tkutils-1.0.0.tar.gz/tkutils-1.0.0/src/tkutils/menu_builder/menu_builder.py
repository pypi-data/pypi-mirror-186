# pylint: disable=too-few-public-methods


import tkinter as T


from typing import List

from tkutils.utilities.singleton_namespace import Singleton
from tkutils.helpers.event_provider import Event

from .bases import MenuElement
from .menu_builder_options import (         # pylint: disable=unused-import    # OFC it is used... x/
    Cmd, COption, CheckBtn, RadioBtn, RadioGrp, Sep, SubMenu
)




#--------------------------------------------------------------------
#                      Abstract base classes
#--------------------------------------------------------------------





#--------------------------------------------------------------------
#                           MenuBuilder
#--------------------------------------------------------------------






class MenuBuilder(Singleton):
    """ Utility to build the menus. This is a singleton/namespace,
        providing autocompletion support to build `tkinter` menus:

        | Property                                                             | Use case                               |
        |:---------------------------------------------------------------------|:---------------------------------------|
        | `sep`                                                                | Menu separator instance (ready to use) |
        | [`Sep`][src.tkutils.menu_builder.menu_builder_options.Sep]           | Relay constructor for `T.Menu.add_separator` (if customized behaviors are needed)|
        | [`Cmd`][src.tkutils.menu_builder.menu_builder_options.Cmd]           | Relay constructor for `T.Menu.add_command` items |
        | [`COption`][src.tkutils.menu_builder.menu_builder_options.COption]   | Handle various options that could be needed at some point for sub widgets |
        | [`CheckBtn`][src.tkutils.menu_builder.menu_builder_options.CheckBtn] | Relay constructor for `T.Menu.add_checkbutton` items |
        | [`RadioGrp`][src.tkutils.menu_builder.menu_builder_options.RadioGrp] | Relay constructor to automatically build a group of radio buttons |
        | [`RadioBtn`][src.tkutils.menu_builder.menu_builder_options.RadioBtn] | Relay constructor for `T.Menu.add_radiobutton` items |
        | [`SubMenu`][src.tkutils.menu_builder.menu_builder_options.SubMenu]   | Relay constructor for `T.Menu.add_cascade` |
    """

    sep      = Sep()        # singleton
    Sep      = Sep          # if ever one needs a custom instance...
    COption  = COption      # config helper for sub widgets
    Cmd      = Cmd          # simple commands
    CheckBtn = CheckBtn     # check button item
    RadioGrp = RadioGrp     # group of radio buttons
    RadioBtn = RadioBtn     # one radio button of a RadioGrp...
    SubMenu  = SubMenu      # Sub/cascade menu


    @classmethod
    def build_menu_on(cls,
                 parent:     T.Widget,
                 menu_tree:  List[MenuElement],
                 is_context: bool = False,
                 event:      str = None,
                 **menu_options,
    ) -> T.Menu :
        """ Build the entire menu hierarchy and return the built `Menu` widget. The `parent`
            widget must be provided, as well as the `menu_tree` hierarchy.

            If `is_context` is False and `event` is None, `parent['menu']` will hold the
            resulting `Menu` widget.

            To build a context menu, or a menu bound to an event:

            - If `is_context` is True, the parent is bound with a right click release event
              and the menu is setup as a context menu.
            - If `event` is provided, the menu is made a context menu of the parent, bound
              to the given `event`. Note: `is_context` takes precedence on `event`, if both
              are provided.

            Parameters:
                parent:     Parent widget for the menu (NOTE: on the root, separators at first
                            level aren't visible).
                menu_tree:  The tree menu hierarchy, as a `List[MenuElement]`.
                is_context: If True, do not bind the menu to `parent['menu']` but set up a
                            context menu opening on right mouse click release.
                event:      If given, do not bind the menu to `parent['menu']` but set up a
                            context menu opening on the given event (NOTE: `is_context` takes
                            precedence over `event`).

            Returns:
                The built menu widget, already carried by the parent widget, or bound to an
                `Event` if it's a context menu.
        """

        menu = T.Menu(parent, tearoff=0, **menu_options)
        for sub in menu_tree:
            sub.build(menu)

        # is_context argument takes precedence over event argument:
        event = Event.RightClick if is_context else event

        if not event:
            parent['menu'] = menu

        else:
            def popup_menu(event:T.Event):
                menu.tk_popup(event.x_root, event.y_root)
            parent.bind(event, popup_menu)

        return menu
