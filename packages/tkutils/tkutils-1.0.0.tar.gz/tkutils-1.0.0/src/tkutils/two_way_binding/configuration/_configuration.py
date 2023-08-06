# pylint: disable=too-few-public-methods

import tkinter as T

from textwrap import dedent
from typing import Any

from tkutils.utilities.singleton_namespace import MutableSingleton
from ..errors import BindingError, TwoWaysBindingConfigError








class _CtrlVarHandler(MutableSingleton):
    """ Master/parent class centralizing the configuration/registration checks and error handling.
    """
    _configurer_arg_name = None     # overridden in subclasses


    @classmethod
    def get(cls, holder:T.Widget, default=None):
        """ Return the needed attribute name to assign a "two-way binding" control variable
            to the given widget.

            @holder:       Current widget/component instance used.
            @default=None: If given, return this value instead of raising TwoWaysBindingConfigError
                           when there is no configuration information for the @holder.
        """
        w_name     = holder.__class__.__name__
        is_defined = w_name in cls

        if not is_defined and default is not None:
            return default

        if not is_defined:
            raise TwoWaysBindingConfigError(
                f"\nUnregistered widget configuration for { w_name !r} widget.\n"
                "Did you forget to register its configuration? "
                "You may want to use the BinderConfig.custom_component(...) function."
            )
        return cls[w_name]


    @classmethod
    def _get_value(cls, value:Any) -> str:
        """ Return the value to display in for the current value item, with appropriate
            formatting if needed.
        """
        raise NotImplementedError()


    @classmethod
    def show(cls, returns=False):
        """ Return a string representation of the current configuration """
        data = '\n    '.join( f'{ key+":" : <{MAX_KEY_SIZE}} { cls._get_value(value) }'
                              for key,value in cls )
        start,end = ('### ','') if returns else ('\033[32;4;1m','\033[0m')
        return f'''
{ start }{ cls._configurer_arg_name }{ end }

{ _clever_dedent(cls.__doc__).strip() }

    { data }
'''








class CtrlVarTypeForWidget(_CtrlVarHandler):
    """ Define what type of control variable to use by default, depending on the widget class name.
    """
    _configurer_arg_name = "BinderConfig.custom_component(..., default_ctrl_var_type, ...)"

    Button            = T.IntVar
    Checkbutton       = T.BooleanVar
    Combobox          = T.StringVar
    Entry             = T.StringVar
    Label             = T.StringVar
    Listbox           = T.StringVar
    MenuButton        = T.StringVar
    Message           = T.StringVar
    OptionMenu        = T.StringVar
    Progressbar       = T.IntVar
    Radiobutton       = T.StringVar
    Scale             = T.DoubleVar
    Spinbox           = T.DoubleVar

    # Custom widget
    ToggleButton      = T.BooleanVar
    SwitchButtonGroup = T.StringVar


    @classmethod
    def _get_value(cls, value:Any):
        return value.__name__









class CtrlVarWidgetPathToHolder(_CtrlVarHandler):
    """ Gives the "path" to the nested widget holding the control variable to assign to,
        for the binding operations.

        All usual widgets are defined (even if they hold the default value as path: "") so that
        they are locked and the user would have to create custom components to bve able to do
        something unexpected.
    """
    _configurer_arg_name = "BinderConfig.nested_component(..., attr_chain_to_holder)"

    Button            = ''
    Checkbutton       = ''
    Combobox          = ''
    Entry             = ''
    Label             = ''
    Listbox           = ''
    MenuButton        = ''
    Message           = ''
    OptionMenu        = ''
    Progressbar       = ''
    Radiobutton       = ''
    Scale             = ''
    Spinbox           = ''

    # Custom widgets
    LabelEntry        = 'entry'
    ToggleButton      = ''
    SwitchButtonGroup = ''


    @classmethod
    def extract(cls, widget, *, attr_chain_to_holder=None):
        """ Given a widget instance, extract the nested widget of interest. If no configuration
            information are available for that widget, assume the component is the one holding
            the control variable.

            @widget: Object to "dig through", to reach the object holding the control variable.
            @attr_chain_to_holder=None: If given, replace the default configuration (or its absence)
        """
        component_name = widget.__class__.__name__
        attr_path:str  = attr_chain_to_holder or cls.get(widget, default='')

        if not attr_path:
            return widget

        for attr in attr_path.split('.'):
            if not hasattr(widget, attr):
                raise BindingError(
                    f"Impossible to bind { component_name } component, accessing a nested object "
                    f"supposed to hold a control variable with the attributes path: {attr_path!r},"
                    f" but couldn't find the { attr !r} attribute."
                )
            widget = getattr(widget, attr)

        if isinstance(widget, T.Variable):
            raise TwoWaysBindingConfigError(
                f"Incorrect custom nested object configuration for { component_name }:\n"
                f"The chain of attributes { attr_path !r} is leading to a control variable "
                "instead of its parent."
            )

        return widget


    @classmethod
    def _get_value(cls, value:Any):
        return repr(value)










class CtrlVarHolderAttribute(_CtrlVarHandler):
    """ Define what argument/property name to which assign the control variable,
        depending on the widget class name.
    """
    _configurer_arg_name = "BinderConfig.custom_component(..., widget_attribute or widget_option)"


                        # (property_name, existing_tkinter_attribute)
    Button            = ('variable',      True)
    Checkbutton       = ('variable',      True)
    Combobox          = ('textvariable',  True)
    Entry             = ('textvariable',  True)
    Label             = ('textvariable',  True)
    Listbox           = ('listvariable',  True)
    MenuButton        = ('textvariable',  True)
    Message           = ('textvariable',  True)
    OptionMenu        = ('variable',      True)
    Progressbar       = ('variable',      True)
    Radiobutton       = ('variable',      True)
    Scale             = ('variable',      True)
    Spinbox           = ('textvariable',  True)

    # Custom widgets
    ToggleButton      = ('ctrl_var',      False)
    SwitchButtonGroup = ('ctrl_var',      False)


    # DEPRECATED: only useful for custom widgets with actual attributes => removed.
    #
    # @classmethod
    # def extract(cls, widget:T.Widget, *, widget_attribute:str=None, widget_option:str=None):
    #     """ Extract the control variable instance from the widget, assuming it already exists.
    #
    #         @widget: Object holding the control variable.
    #         @widget_attribute=None: the control variable must be extracted from the given property
    #                  name (override any default configuration, or its absence).
    #         @widget_option=None: the control variable must be extracted from the given tkinter
    #                  option name (override any default configuration, or its absence).
    #     """
    #
    #     if widget_attribute:
    #         prop, is_tk = widget_attribute, False
    #     elif widget_option:
    #         prop, is_tk = widget_option, True
    #     else:
    #         prop, is_tk = cls.get(widget)
    #
    #     # if is_tk:
    #     #     raise BindingError('Control variables put on ')
    #
    #     return widget[prop] if is_tk else getattr(widget, prop)


    @classmethod
    def assign(
        cls,
        widget:             T.Widget,
        ctrl_var:           T.Variable,
        widget_attribute:   str = None,
        widget_option:      str = None,
    ):
        """ Assign the control variable to the correct property of the given widget.
            If the widget doesn't hold natively a control variable for the current purpose
            (see ToggleButton), it will be assigned to a regular property of the object
            instead. It's to the user building the custom class to account for the correct
            use of the control variable.
        """
        if widget_attribute and widget_option:
            raise BindingError(
                "Only one of the widget attribute or option to which to assign the control variable "
                f"should be provided as argument, but got: {widget_attribute=} and {widget_option=}"
            )

        prop, is_tk = cls.get(widget, (widget_attribute or widget_option,False) )

        if prop is None:
            raise BindingError(
                "No tkinter widget option or attribute where to assign the control variable defined "
                f"for { widget.__class__.__name__ !r}"
            )

        if is_tk:
            widget[prop] = ctrl_var
        else:
            setattr(widget, prop, ctrl_var)


    @classmethod
    def _get_value(cls, value:Any):
        return value[0]


    @classmethod
    def is_widget(cls, name:str):
        """ Testing purpose, mostly (interface to check the internal state, keeping it "isolated")
        """
        return cls[name][1]

    @classmethod
    def get_value(cls, name:str):
        """ Testing purpose, mostly (interface to check the internal state, keeping it "isolated")
        """
        return cls[name][0]










__OOPS = "Unbalanced widgets definition for CtrlTypeConfig and CtrlVarWidgetArg"
assert set(CtrlVarTypeForWidget.keys) == set(CtrlVarHolderAttribute.keys), __OOPS

__BASE_CONFIG = set( CtrlVarTypeForWidget.keys
                 + CtrlVarWidgetPathToHolder.keys
                 + CtrlVarHolderAttribute.keys)

MAX_KEY_SIZE = 2 + max(map(len, __BASE_CONFIG))







def _clever_dedent(doc:str):
    """ Take a docstring and dedent it appropriately by comparing the first two lines:

        - If the first line is empty: dedent normally/automatically.
        - Otherwise, lstrip the first line and dedent all other lines separately.
    """
    # attempt to appropriately dedent the docstring, depending on where is the first line
    first_nl = doc.find('\n')

    # first line is empty, just dedent without any further question...
    if first_nl==0:
        dedent_doc = dedent(doc[1:])

    # The docstring is starting on the triple quote line, dedent only from second line
    else:
        dedent_doc = doc[:first_nl+1].lstrip() + dedent(doc[first_nl+1:])

    return dedent_doc
