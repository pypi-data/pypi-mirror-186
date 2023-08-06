
import inspect
import tkinter as T

from typing import Collection, Type

from ..errors import TwoWaysBindingConfigError

from ._configurer_image_factory import (
    get_image_factory_config_location,
    configure_image_factory,
)
from ._configuration import (
    _CtrlVarHandler,
    CtrlVarTypeForWidget,
    CtrlVarHolderAttribute,
    CtrlVarWidgetPathToHolder,
)






def _check_not_already_configured(
    widget_type: Type,
    config_singletons:Collection[_CtrlVarHandler]
):
    if not isinstance(widget_type, type):
        raise TwoWaysBindingConfigError(f"{widget_type} should be a class type, not an instance.")

    widget_name = widget_type.__name__
    defined_in = [ singleton.__name__ for singleton in config_singletons
                                      if widget_name in singleton ]
    if defined_in:
        raise TwoWaysBindingConfigError(
            f"Cannot add { widget_name } to the two-way binder configuration: a widget is already"
            f" registered with that name in { ' and '.join(defined_in) }.\n"
            "You can print the current configuration by using two_way_binding.show_binder_config()"
        )









class BinderConfig:
    """ Manage the different configurations of the two-way binding utility, the configuration for
        images used through the `Binder`, as well the observers for those configurations.
    """


    limit_stack = True
    """ If True, an OverflowError is raised if an infinite recursion is suspected during the
        two-way binding updates. This behavior can be turned off by updating this attribute.
    """



    @staticmethod
    def nested_component(widget_type:Type, attr_chain_to_holder:str):
        """ Register a configuration for a custom component/widget whose one of the children is
            actually holding the desired control variable.

            This method allows to register the "path of attributes" leading from the component
            instance to the child object that is _holding_ the control variable.

            !!! warning
                * The object _holding_ the control variable is to be  extracted, not the control
                  variable itself.
                * Settings are identified using the class name of the registered widget
                  (`widget_type.__name__`)
                * Any custom configuration must be made each time the application is run, before
                  the GUI is built (the registered data do not persist throughout different runs).

            Parameters:
                widget_type:
                    The class of the custom component to register.
                attr_chain_to_holder:
                    Path of attributes to follow from the top level custom component, to get
                    access to the object holding the control variable.

            Raises:
                TwoWaysBindingConfigError: If the widget type isn't a type, or if it is already
                                           registered with a chain of attributes.
        """
        _check_not_already_configured(widget_type, [CtrlVarWidgetPathToHolder])
        CtrlVarWidgetPathToHolder[widget_type.__name__] = attr_chain_to_holder




    @staticmethod
    def custom_component(
        widget_type:              Type,
        default_ctrl_var_type:    Type[T.Variable],
        *,
        widget_attribute: str = None,
        widget_option:   str = None,
    ) -> None :
        """ For a custom widget/component that _is holding_ (directly) a control variable.

            This method allows to register the informations to know how/where the `Binder` has to
            "plug in" the control variable instance on the widget.

            !!! warning
                * The object _directly holding_ the control variable is to be configured (see
                  [`BinderConfig.nested_component`][src.tkutils.two_way_binding.configuration._binder_config.BinderConfig.nested_component]).
                * Settings are identified using the class name of the registered widget
                  (`widget_type.__name__`)
                * Any custom configuration must be made each time the application is run, before
                  the GUI is built (the registered data do not persist throughout different runs).

            Parameters:
                widget_type:
                    The class of the custom component to register.
                default_ctrl_var_type:
                    Type of control variable used when instantiated automatically during binding.
                widget_attribute:
                    Gives the name of the attribute where to inject the control variable, when it
                    is hold as an instance property by the custom component. If this argument is
                    used, `widget_option` must be None.
                widget_option:
                    Gives the name of the option to use to inject the control variable, when it is
                    hold by a tkinter widget on or inside the custom component. If this argument
                    is used, `widget_attribute` must be None.

            Raises:
                TwoWaysBindingConfigError: If the widget type isn't a type, or if it is already
                                        registered with a chain of attributes.
        """
        _check_not_already_configured(widget_type, [CtrlVarTypeForWidget, CtrlVarHolderAttribute])
        widget_name = widget_type.__name__

        if default_ctrl_var_type and not isinstance(default_ctrl_var_type, type):
            raise TwoWaysBindingConfigError(
                f"The given type class to automatically build control variables for {widget_name} "
                f"is not a type class: {default_ctrl_var_type}"
            )

        one_arg_only = bool(widget_attribute) + bool(widget_option) == 1
        if default_ctrl_var_type and not one_arg_only:
            raise TwoWaysBindingConfigError(
                f"If a control variable type is given (here: {default_ctrl_var_type}), either "
                "widget_option or widget_attribute has to be defined."
            )


        if default_ctrl_var_type:
            CtrlVarTypeForWidget[widget_name] = default_ctrl_var_type

        location          = widget_attribute or widget_option
        is_tkinter_option = widget_attribute is not None
        CtrlVarHolderAttribute[widget_name] = (location, is_tkinter_option)




    @staticmethod
    def image_location(
        project_name:str,
        *path_to_images:str,
        any_file_in_project:str=None
    ):
        """ Configure the path to the directory holding images, to use the
            [`Binder.with_image`][src.tkutils.two_way_binding.binder.Binder.with_image] method.

            This functionality uses the interface of
            [`tkutils.images.images_factory`][src.tkutils.images.images_factory].

            !!! tip
                If `any_file_in_project` is not provided, the location of the project is discovered
                through inspection of the call stack, getting the filename of the caller of the
                function.

            Parameters:
                project_name:        Name of the root directory of the project
                *path_to_images:     Path of subdirectories to the one containing the images.
                any_file_in_project: To provide only if the `project_name` directory isn't in
                                     the path of the file of the caller.
        """
        caller = any_file_in_project or inspect.stack()[1].filename
        configure_image_factory(project_name, *path_to_images, any_file_in_project=caller)




    #-------------------------------------------------------------------------




    @staticmethod
    def show_binder_config(returns=False):
        """ Print the current binding configuration to the console or return it if `returns=True`
        """
        classes = (
            CtrlVarTypeForWidget,
            CtrlVarHolderAttribute,
            CtrlVarWidgetPathToHolder,
        )
        msg = (_title("two-way binding configuration", returns)
                    + "\n\n(Some custom configurations are shown at the end of each list)\n\n"
                    + "\n".join( kls.show(returns) for kls in classes )
                    + "\n"
        )
        print(msg)
        return msg if returns else None




    @staticmethod
    def show_images_location(returns=False):
        """ Print the current image factory configuration to the console or return it if
            `returns=True`.
        """
        msg = (
            _title("Current images location for Binder.with_image(...) factory", returns)
                    + '\n\n    '
                    + repr(get_image_factory_config_location())
                    + "\n"
        )
        print(msg)
        return msg if returns else None




def _title(msg, returns):
    format_in  = "### " if returns else '\033[33;4;1m'
    format_out = "" if returns else "\033[0m:"
    return f"\n\n{ format_in }{ msg }{ format_out }"
