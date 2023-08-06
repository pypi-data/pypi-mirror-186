# pylint: disable=too-few-public-methods



import tkinter as T

from typing import Any, Callable, List, Union
from PIL.ImageTk import PhotoImage

from .bases import MenuElement, MenuElementWithCbk







class COption:
    """ Dedicated data container class, to allow all possible options for the different menu
        items, without cluttering the method signatures of the MenuBuilder.

        The most likely used or interesting options are declared explicitly, the others are
        allowed through the `**kwargs` optional arguments.
    """

    # pylint: disable-next=too-many-arguments
    def __init__(
        self,
        accelerator:str=None,
        activebackground:str=None,
        columnbreak=False,
        compound:str=None,
        hidemargin=False,
        image:PhotoImage=None,
        selectimage:PhotoImage=None,
        underline:int=None,
        **kwargs
    ):
        kwargs.update({
            'accelerator': accelerator,
            'activebackground': activebackground,
            'columnbreak': columnbreak,
            'compound': compound,
            'hidemargin': hidemargin,
            'image': image,
            'selectimage': selectimage,
            'underline': underline,
        })
        self.kw_c_options = kwargs



class RadioBtn:
    """ Wrapper for `Menu.add_radiobutton`.

        Store the needed data to add a radio button to a menu section. The kwarg @options can
        be used with any kwarg normally used to build a T.RadioButton widget.

        Parameters:
            label:      Label for the radio button item
            value:      String of int value to associate with this choice
            c_options:  Options that can be used with the RadioButton when it's instantiated.
                        See: `T.Menu.add_radiobutton(..., coption, ...)`
    """

    def __init__(self, label:str, value:Union[str,int], c_options:COption=None):
        self.label     = label
        self.value     = value
        self.c_options = c_options.kw_c_options if c_options else {}





#--------------------------------------------------------------------
#                   Menu Constructors/Helpers
#--------------------------------------------------------------------





class Sep(MenuElement):
    """ Wrapper for `Menu.add_separator`.

        (reminder: separators do not show up on top level menus)
    """
    def __init__(self, **c_options):
        self.c_options = c_options

    def build(self, parent:T.Menu):
        self.parent = parent
        parent.add_separator(**self.c_options)
        return self





class Cmd(MenuElementWithCbk):
    """ Wrapper for `T.Menu.add_command`.

        Parameters:
            label:      Name of the item
            cbk:        Callback taking no argument, to execute on selection of this option
            c_options:  Additional config options for the menu item. See:
                        `T.Menu.add_command(..., coption, ...)`
    """

    def __init__(self, label:str, cbk:Callable[[],None], c_options:COption=None):
        self.label = label
        self.cbk   = lambda *_: cbk()
        self.c_options = c_options.kw_c_options if c_options else {}
        self.parent:T.Menu = None


    def build(self, parent:T.Menu):
        self.parent = parent
        parent.add_command(
            label=self.label,
            command=self.cbk,
            **self.c_options,
        )
        return self






class CheckBtn(MenuElementWithCbk):
    """ Wrapper for `T.Menu.add_checkbutton`.

        Takes a command callback expecting a boolean argument (the value of the underlying control
        variable). The control variable is automatically built by the function, unless an instance
        is passed through the constructor arguments.

        Parameters:
            label:     Name of the item
            cbk:       Callback taking a bool argument (the state of the check button when clicked)
            ctrl_var:  A `T.BooleanVar` instance that will be used for the internal check button.
                       If not given, one will be instantiated automatically and will be accessible
                       through the `self.ctrl_var` property.
            c_options: COptions that can be used when building the check button item.
                       See: `T.Menu.add_check_button(..., coptions, ...)`
    """

    def __init__(self,
        label:str, cbk:Callable[[bool],None],
        ctrl_var:T.BooleanVar=None, c_options:COption=None
    ):
        self.label     = label
        self.cbk       = lambda *_: cbk(self.ctrl_var.get())
        self.c_options = c_options.kw_c_options if c_options else {}
        self.ctrl_var  = ctrl_var or T.BooleanVar(value=False)
        self.parent:T.Menu = None


    def build(self, parent:T.Menu):
        self.parent = parent
        parent.add_checkbutton(
            label   = self.label,
            command = self.cbk,
            variable= self.ctrl_var,
            **self.c_options
        )
        return self






class RadioGrp(MenuElementWithCbk):
    """ Wrapper for a group of `T.Menu.add_radiobutton` definitions.

        Build a group of radio buttons bound to a single control variable instance. Note that
        one of the items must always be selected, within a group of radio buttons.

        A RadioGrp automatically put separators before the first radio button and after the
        last one, if there are other items before/after in the parent menu, and if those items
        aren't already separators.

        Parameters:
            cbk:      Callback taking a str|int argument (the current value of the control variable)
            *radios:  `RadioBtn` instances, describing the radio buttons to create for that group.
            ctrl_var: A `T.Variable` instance, that will be used for the check button (if not
                      given, `T.StringVar()` is instantiated). This control variable will be
                      accessible through the `self.ctrl_var` property, if you need it later on.
            starting_val_idx: Index of the `Radio` instance to use as starting value.
    """

    def __init__(self,
        cbk:Callable[[Union[str,int]],None],
        *radios:RadioBtn,
        ctrl_var:Union[T.StringVar,T.IntVar]=None,
        starting_val_idx:int=0,
    ):
        self.cbk      = lambda *_: cbk(self.ctrl_var.get())
        self.radios   = radios
        self.start_on = starting_val_idx
        self.ctrl_var = ctrl_var or T.StringVar()
        self.parent:T.Menu = None


    def build(self, parent:T.Menu):
        self.parent = parent
        for radio in self.radios:
            parent.add_radiobutton(
                label   = radio.label,
                command = self.cbk,
                variable= self.ctrl_var,
                value   = radio.value,
                **(radio.c_options or {})
            )
        self.ctrl_var.set(self.radios[self.start_on].value)
        return self






class SubMenu(MenuElement):
    """ Wrapper for `T.Menu.add_cascade`.

        Build a cascade sub-menu with the given `subs` elements.

        Parameters:
            label:          Label of the submenu item in the parent Menu.
            subs:           Tree hierarchy of the cascade.
            **menu_options: Additional options to use when building the T.Menu widget
                            holding the subtree hierarchy.
    """

    def __init__(self, label:str, subs:List[MenuElement], **menu_options:Any):
        self.label   = label
        self.subs    = subs
        self.options = menu_options
        self.parent:T.Menu = None
        self.menubar: T.Menu = None


    def build(self, parent:T.Menu):
        self.parent = parent
        self.menubar = T.Menu(parent, tearoff=0, **self.options)
        parent.add_cascade(label=self.label, menu=self.menubar)

        for i,sub in enumerate(self.subs):

            if not isinstance(sub, RadioGrp):
                sub.build(self.menubar)

            else:
                if i and not isinstance(self.subs[i-1], Sep):
                    self.menubar.add_separator()
                sub.build(self.menubar)
                if i+1<len(self.subs) and not isinstance(self.subs[i+1], Sep):
                    self.menubar.add_separator()

        return self






