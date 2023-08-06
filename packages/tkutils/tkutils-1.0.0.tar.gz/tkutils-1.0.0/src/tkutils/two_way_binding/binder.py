

import tkinter as T

from inspect import Parameter, signature
from functools import wraps
from typing import Any, Callable, Type, TypeVar
from PIL import ImageTk


from .errors import BinderError, BinderLockedError, BindingCtrlVarError, BindingError
from .configuration._configuration import (
    CtrlVarTypeForWidget,
    CtrlVarHolderAttribute,
    CtrlVarWidgetPathToHolder,
)
from .configuration._configurer_image_factory import get_image_factory
from . configuration._binder_config import BinderConfig
from .binding_descriptor import BindingDescriptor




Widget = TypeVar('Widget', bound=T.Widget)









def unbound_only(meth):
    """ Decorator to ensure that a locked/used Binder instance isn't several times after
        a binding as been set with it.
    """
    @wraps(meth)
    def wrapper(self:'Binder',*a,**kw):
        if self.bound:
            raise BinderLockedError("This object already created a two-way binding...")
        return meth(self, *a,**kw)
    return wrapper




def check_hashable(that:Any):
    """ Raises BidingError if the input object isn't hashable """

    if not hasattr(that, '__hash__'):
        raise BindingError(f"The { that.__class__.__name__ } instances are not hashable")






class Binder:               # pylint: disable=too-many-instance-attributes
    """
    Helper to declare a two-way binding between widgets using a control variable and an object
    property in the model layer of the application, providing syntactic sugar, to make the
    declarations clearer and more versatile (order of definitions).

    The different registration methods can be used in any order and each one of them returns a
    fresh `Binder` object. Their `bind` method is to be called last and actually creates the
    two-way binding, based on the registered information.

    !!! tip "Binder factories"
        The above behavior makes it possible to use various Binder instances as factories, avoiding
        some code repetition. For example:

        * A `Binder(obj)` can be used as base to define several bindings on different properties
          of that `obj` instance (object of the model layer in the application).

        * A `Binder(prop="price")` can be used to define bindings between pairs of widget/object,
          that will work on the `price` value of different items.

    Parameters:
        obj:    Instance whose a property is to be bound (must be hashable)
        prop:   property name to bind
    """

    def __init__(self, obj:Any=None, prop:str=None):
        if obj is not None:
            check_hashable(obj)

        self.obj  = obj
        self.prop = prop

        self.bound = False

        self.widget:           Widget = None
        self.ctrl_var:         T.Variable = None
        self.after_change_cbk: Callable = None
        self.cbk_n_args:       int = None

        self.image:            ImageTk.PhotoImage = None
        self.image_width:      int = None
        self.image_height:     int = None
        self.attr_chain_to_holder: str = None
        self.widget_attribute: str = None
        self.widget_option:    str = None
        # self.auto_resize_widget_on_image: bool = None


    def __make_fresh_binder(self, **kw) -> 'Binder':
        # Create  copy of the current instance, adding the given arguments.
        # Ensure that no previous arguments are overridden.
        #
        # NOTE: the fresh instance is mutated to keep as few arguments as possible for the
        #      __init__ method (makes it easier to use with IDE suggestions).
        #
        fresh  = Binder()
        stored = {
            'obj': self.obj,
            'prop': self.prop,
            'bound': self.bound,
            'widget': self.widget,
            'ctrl_var': self.ctrl_var,
            'after_change_cbk': self.after_change_cbk,
            'cbk_n_args': self.cbk_n_args,
            'image': self.image,
            'image_width': self.image_width,
            'image_height': self.image_height,
            # 'auto_resize_widget_on_image': self.auto_resize_widget_on_image,
            'attr_chain_to_holder': self.attr_chain_to_holder,
            'widget_attribute': self.widget_attribute,
            'widget_option': self.widget_option,
        }
        if not all(stored[k] is None for k in kw):
            raise BinderError("Cannot redefine one of those arguments: "+', '.join(map(repr,kw)))

        for k,value in {**stored, **kw}.items():
            setattr(fresh, k, value)
        return fresh


    #----------------------------------------------------------------------



    @unbound_only
    def of(self, obj:Any) -> 'Binder':      # pylint: disable=invalid-name
        """ Register the targeted object (model layer of the application), when not given through
            the constructor.

            Parameters:
                obj: The object instance to bind (must be hashable).

            Raises:
                BinderError:    If the object instance has already been registered
                BindingError:   If the object it is not hashable

            Returns:
                A new `Binder` instance with the property name added.
        """
        check_hashable(obj)
        return self.__make_fresh_binder(obj=obj)



    @unbound_only
    def for_property(self, prop:str) -> 'Binder':
        """ Register the property name info (for the targeted object), when not given
            through the constructor.

            Parameters:
                prop: name of the property to bind

            Raises:
                BinderError: If the property name has already been registered

            Returns:
                A new `Binder` instance with the property name added.
        """
        return self.__make_fresh_binder(prop=prop)



    @unbound_only
    def on(self,                                    # pylint: disable=invalid-name
           widget:               Widget, *,
           ctrl_var:             T.Variable = None,
           ctrl_typ:             Type[T.Variable] = None,
           attr_chain_to_holder: str = None,
           widget_attribute:     str = None,
           widget_option:        str = None,
    ) -> 'Binder':
        """
        Register the widget and the control variable to use for the two-way binding. The
        assumed preconditions/contract here is the following:

        1. The widget isn't supposed to already hold a control variable
        1. The way to define the control variable for the binding must be known upfront:
            - either by providing the instance to use (`ctrl_var`)
            - or by providing its type (`ctrl_typ`)
            - or by using the default configuration, if the  widget class name is known from
              the Binder configuration (see [`BinderConfig`][src.tkutils.two_way_binding.configuration._binder_config.BinderConfig])
        1. The `Binder` must know upfront "where" to put the control variable on the widget:
            - either using the default configuration information (see [`BinderConfig`][src.tkutils.two_way_binding.configuration._binder_config.BinderConfig])
            - or using the optional arguments to provide the needed information:
                * `attr_chain_to_holder`, to know how to access the widget holding the control
                  variable.
                * `widget_attribute` or `widget_option`, to know where to put the control variable.
                  (note that only one of those arguments can be used at the same time)

            See [`BinderConfig`][src.tkutils.two_way_binding.configuration._binder_config.BinderConfig]
            for more explanations about the above arguments/configurations.

        !!! tip "Controlling the control variable..."
            * When defining the control variable kind/instance to use, the priority order of the
              arguments/definitions is:

                `ctrl_var > ctrl_typ > default configuration`

            * When choosing where/how to patch the resulting control variable on the widget:

                `Optional arguments of Binder.on(...) > default configuration`

        !!! warning "About using preexisting control variables"
            * Any control variable already defined on the widget will be overridden and lost at
              binding time.
            * Any preexisting `trace` callback defined in `"write"` mode on a control variable will
              get overridden and lost at binding time. Use the `after_change` callback registration
              to apply any behavior you'd need.

        !!! warning "Custom widgets requirement"
            * The `widget` object can actually be of any kind, but it has to implement a `destroy()`
              method.
            * The `widget` must be hashable.

        ---

        Parameters:
            widget:
                The widget instance to bind (possibly custom). If it is not extending Widget, it
                must have a `destroy()` method implemented
            ctrl_var:
                Instance of `tkinter.Variable` to use. Overrides the default behavior.
            ctrl_typ:
                Type of the control variable to instantiate.
                Overrides the default behavior.
            attr_chain_to_holder:
                Path of attributes to reach the object holding the control variable.
                Overrides the default configuration.
            widget_attribute:
                Name of the attribute holding the control variable.
                Overrides the default configuration.
            widget_option:
                Name of the config option of a widget holding the control variable.
                Overrides the default configuration.

        Raises:
            BinderError:  If a widget or a control variable has already been registered for
                          this Binder.
            BindingCtrlVarError: If the registered configuration or the arguments defined to
                                 extract the control variable itself instead of its parent, or
                                 if some information cannot be found for the widget/object.
            BindingError: If the `widget` isn't hashable.
            BindingError: If the widget supposed to hold the control variable cannot be reached
            BindingError: If both `widget_attribute` and `widget_option` arguments are used at
                          the same time.
            TwoWaysBindingConfigError: If the registered configuration or the arguments lead to
                                       extract the control variable itself instead of its
                                       parent, or if some information cannot be found for the
                                       widget/object, or if both `widget_attribute` and
                                       `widget_option` are used at the same time.

        Returns:
            A new `Binder` instance with the callback added.
        """
        check_hashable(widget)

        ctrl_holder = CtrlVarWidgetPathToHolder.extract(
            widget, attr_chain_to_holder=attr_chain_to_holder
        )

        if widget_attribute and widget_option:
            raise BinderError(
                "Only one of the widget attribute or option to which to assign the control "
                f"variable should be provided as argument, but got: {widget_attribute=} and "
                f"{widget_option=}"
            )

        if not ctrl_var:        # Instantiate if type given or pick one based on widget type
            ctrl_typ = ctrl_typ or CtrlVarTypeForWidget.get(ctrl_holder)
            ctrl_var = ctrl_typ()

        if not isinstance(ctrl_var, T.Variable):
            raise BindingCtrlVarError(
                f"Couldn't extract or build a control variable instance: ctrl_var={ctrl_var}"
            )

        return self.__make_fresh_binder(
            widget=widget,
            ctrl_var=ctrl_var,
            attr_chain_to_holder=attr_chain_to_holder,
            widget_attribute=widget_attribute,
            widget_option=widget_option,
        )



    @unbound_only
    def after_change(self, after_change_cbk:Callable) -> 'Binder':
        """ Register the "after change" callback that will update the GUI.

            Different signatures can be used:

            * `after_change() -> None`

                No argument

            * `after_change(new_value:Any) -> None`

                Receives the value  of the bound property after it has been updated

            * `after_change(new_value:Any, model:Object, widget:T.Widget) -> None`

                Receives the value  of the bound property after it has been updated

            The correct signature to use will be determined through inspection, so the user does
            not have to care about putting default arguments when defining a callback of the
            simplest form.

            Arguments will always be passed as positional arguments, so you can use keyword only
            arguments to pass extra constant values to the function if you need it.

            !!! warning
                Positional arguments with default value _will_ be overwritten at call time, if they
                are in first, second or third position. Enforce the use of keyword arguments to
                avoid this behavior: `cbk(value, *, my_default=42)`.

            Parameters:
                after_change_cbk:
                    Consumer callback, to apply various updates that should occur after
                    a change, either `Callable[[],None]`, `Callable[[Any],None]` or
                    `Callable[[Any,Object,T.Widget],None]`.

            Raises:
                BinderError: If the callback has already been registered
                ValueError:  If the `after_change_cbk` argument is not callable
                ValueError:  If the callback signature cannot be determined or is not compatible

            Returns:
                A new `Binder` instance with the callback added.
        """
        if not callable(after_change_cbk):
            raise ValueError("after_change_cbk must be callable")

        counted_param_kinds = (
            Parameter.POSITIONAL_ONLY,
            Parameter.POSITIONAL_OR_KEYWORD,
            Parameter.VAR_POSITIONAL,
        )
        cbk_n_args = 0
        if after_change_cbk:
            cbk_params = signature(after_change_cbk).parameters
            args       = [ p for p in cbk_params.values() if p.kind in counted_param_kinds ]

            cbk_n_args = len(args)
            if args and args[-1].kind == Parameter.VAR_POSITIONAL:
                # If vararg are used, always pass the 3 arguments
                cbk_n_args = max(3, cbk_n_args)

        if cbk_n_args==2 or cbk_n_args>3:
            raise ValueError(
                "The after_change callback should take either 0, 1 or 3 positional arguments, "
            + f"but those where found for the callback { after_change_cbk.__name__ }:"
            + "".join(f'\n\t{p.name}: {p.kind}' for p in args)
            + '\nOther arguments present:'
            + ( "".join(f'\n\t{p.name}: {p.kind}' for p in args if p not in args)
                or "\n\tNone" )
            )

        return self.__make_fresh_binder(
            after_change_cbk = after_change_cbk,
            cbk_n_args       = cbk_n_args,
        )





    @unbound_only
    def with_image(self, file:str, width:int=None, height:int=None, size:int=None,
                # auto_resize_widget_on_image=True
    ) -> 'Binder':
        """ _This is unrelated to binding tasks, but is an useful syntax helper._

            Register an image stored into a preconfigured directory of assets. That image wll be
            put on the widget during binding.

            !!! warning
                To use this helper, the image factory of the `Binder` must be already configured
                (see [`BinderConfig.image_location`][src.tkutils.two_way_binding.configuration._binder_config.BinderConfig.image_location]).

            Parameters:
                file: name of the file to use (with the configured image factory)
                size: width and height to use, for a squared image
                width: width to give to the image
                height: height to give to the image

            Raises:
                BinderError: If an image has already been registered
                ValueError: For invalid dimensions arguments, or FileNotFoundError if the
                            filename or the path is invalide.

            Returns:
                A new `Binder` instance with the callback added.
        """
        image_from = get_image_factory()
        image, width, height = image_from(          # pylint: disable=not-callable   # dafuck!?! x/
            file, width=width, height=height, size=size
        )
        return self.__make_fresh_binder(
            image=image, image_width=width, image_height=height,
            # auto_resize_widget_on_image=auto_resize_widget_on_image
        )










    #----------------------------------------------------------------------
    # Actual binding operations, handling all previously defined binding configurations








    @unbound_only
    def bind(self) -> Widget:
        """ Put the binding in place, using all previously registered elements, and returns the
            bound widget.

            The binding operation will automatically set the control variable value to the one
            of the bound property object of the model layer. This initialization will trigger
            the `after_change` callback, if it has been registered.

            The `Binder.bind` method "consumes" the Binder instance: it is not usable anymore
            after this call, so all registrations must be done properly before that (even a
            possible `with_image` registration cannot be done once `bind` has been called).

            Raises:
                AttributeError:            If the bound property value doesn't already exist.
                BinderError:               If the `object`, its `property` name, or the `widget`
                                           have not been registered.
                BindingCtrlVarError:       If the control variable is not a control variable
                                           instance (wrong `Binder.on` call)
                BindingError:              If the widget/object supposed to hold the control
                                           variable cannot be reached.
                TwoWaysBindingConfigError: If the registered configuration or the arguments defined
                                           to extract the control variable itself instead of its
                                           parent, or if some information cannot be found for the
                                           widget/object.

            Returns:
                The bound widget instance, with the initial value set to the bound object property.

        """
        if self.obj is None:
            raise BinderError("No object instance to bind to.")

        if self.prop is None:
            raise BinderError("No property to bind to.")

        if self.widget is None:
            raise BinderError("No widget to bind to.")

        if not isinstance(self.ctrl_var, T.Variable):
            raise BindingCtrlVarError(
                f"Couldn't extract or build a control variable instance: ctrl_var={self.ctrl_var}"
            )

        self.bound = True           # Lock the Binder instance
        self.__attach_image()
        self.__handle_ctrl_var_and_reactivity()
        return self.widget







    #----------------------------------------------------------------------






    def __attach_image(self):
        if not self.image: return                       # pylint: disable=multiple-statements

        self.widget._image_ref_to_avoid_GC = self.image   # pylint: disable=protected-access
        self.widget.config(image=self.image)

        # Doesn't work
        # if self.auto_resize_widget_on_image:
        #     self.widget.config(width = self.image_width,
        #                        height= self.image_height)



    def __handle_ctrl_var_and_reactivity(self):

        ctrl_var_holder = CtrlVarWidgetPathToHolder.extract(
            self.widget, attr_chain_to_holder=self.attr_chain_to_holder
        )

        CtrlVarHolderAttribute.assign(
            ctrl_var_holder,
            self.ctrl_var,
            self.widget_attribute,
            self.widget_option,
        )

        flash_on_error = flasher(ctrl_var_holder, 2, 100)
        stack_level = 0

        def two_ways_setter(val):
            """ Multi-setter callback: allow to update the control variable and/or the targeted
                object property.
                Updates occur only when the current value differs from the argument, so any
                kind of update can pass through this very same callback without ending in
                circular updates.
            """
            nonlocal stack_level

            if not BinderConfig.limit_stack:
                stack_level = 1
            else:
                stack_level += 1
                if stack_level>2:
                    raise OverflowError(
                        '\nIt looks like the two-way binding will run into infinite recursion. '
                        'If you are certain it will not be the case, you can set '
                        'BinderConfig.limit_stack to False.\n'
                        'Binding involving:\n'
                        f'\tModel: { self.obj.__class__.__name__ }.{ self.prop }\n'
                        f'\tGUI: { self.widget.__class__.__name__ }\n'
                    )

            try:
                changed = False
                current_ctrl = self.ctrl_var.get()
                if current_ctrl != val:
                    changed = True
                    self.ctrl_var.set(val)
                    # print(f'set {self.prop} ctrl_var to: {val}')

                current_obj = getattr(self.obj, self.prop)
                if current_obj != val:
                    changed = True
                    setattr(self.obj, self.prop, val)
                    # print(f'set {self.obj.__class__.__name__}.{self.prop} to: {val}')

                if changed and self.after_change_cbk:
                    # pylint: disable=not-callable
                    if not self.cbk_n_args:
                        self.after_change_cbk()
                    elif self.cbk_n_args==1:
                        self.after_change_cbk(val)
                    else:
                        self.after_change_cbk(val, self.obj, self.widget)

            except T.TclError:
                flash_on_error()
            stack_level -= 1


        #----------------------------------------------------


        def safe_tracer(*_):
            """ Relay callback used for ctrl_var.trace_add (which stupidly receives useless
                arguments instead of the value itself...)
            """
            try:
                val = self.ctrl_var.get()
                two_ways_setter(val)
            except T.TclError:
                flash_on_error()


        # Bind, way 1: the control variable itself:
        self.ctrl_var.trace_add('write', callback=safe_tracer)


        # Bind, way 2: put the Descriptor in place on the object property, or update it:
        desc = BindingDescriptor.bind(self.obj, self.prop, two_ways_setter, self.widget)


        # Hack the widget destroy method to automatically unsubscribe from the BindingDescriptor:
        def two_ways_destroyer():
            desc.unsubscribe_on_destroy(self.widget)
            old_destroy()

        old_destroy = self.widget.destroy
        self.widget.destroy = two_ways_destroyer


        # Set initial state, triggering the control variable with the current object value:
        value = getattr(self.obj,self.prop)
        self.ctrl_var.set(value)











def flasher(widget:T.Widget, n_times:int, delta_ms:int, prop='bg', flash_color='#ffaaaa'):
    """ Build a callback to make flash any kind of widget, playing on its colors.

        @widget:      target of the flash
        @n_times:     number of times the flash is repeated
        @delta_ms:    number of milliseconds between to changes of color (1 flash = 2 changes)
        @prop:        property name to flash
        @flash_color: color to use for the flash
    """
    try:
        base_bg = widget[prop]
    except Exception:               # pylint: disable=broad-except
        return lambda: None

    def color_flash(color):
        return lambda:widget.configure(**{prop:color})

    def cbk():
        colors = (flash_color, base_bg) * n_times
        for i,color in enumerate(colors):
            widget.after(i*delta_ms, color_flash(color))
    return cbk
