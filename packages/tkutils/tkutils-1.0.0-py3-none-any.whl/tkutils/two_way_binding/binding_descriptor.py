


import tkinter as T

from typing import Any, Callable, Dict, DefaultDict, Set
from collections import defaultdict

from .errors import BindingError


BIND_PREFIX = '_bound_'



# NOTE:
#   Using directly the patched property name to work on the bound instances doesn't work because
#   of the setattr operation: if the property name is the one of the descriptor, it's impossible
#   to use setattr (the instance property is always shadowed by the descriptor), while it's not
#   always possible to resort to mutating the __dict_ directly (which isn't good practice anyway).
#   Typically, it becomes impossible to bind class level properties with a metaclass (the
#   __dict__ returned by `vars` is a "mappingproxy", which doesn't support assignment...).
#
#   So, unfortunately, resorting to prefixed_property is absolutely necessary...





class BindingDescriptor:
    """ Descriptor handling the "Model -> Presentation" way of the two-way binding, at runtime.

        The BindingDescriptor.bind(...) classmethod is hacking at runtime the class body of a
        given instance, preserving any preexisting state/behavior (at class or instance level)
        and put in place a way to update the given widget each time the object property is updated.

        - The binding auto update is working on a specific widget instance for a specific instance
          property.
        - If the widget is destroyed, the binding is "unreferenced", but the descriptor stays in
          place on the class body, for the sake of simplicity.
    """

    DESCRIPTOR_SPECIFIC_METHODS_SET = set('__get__ __set__ __delete__'.split())

    inner_descriptor:  Any = None   # None | a descriptor originally on the class at binding time

    patched_property:  str = None   # Property of the class bound with the descriptor
    prefixed_property: str = None   # prefixed property name, added by the descriptor to each
                                    # instance/class, to keep track of the bound property value.

    _bindings:     DefaultDict[Any, Dict[T.Widget,Callable[[Any],None]] ]
        # dict of dicts tracking which instance (or class) is bound to what widget

    _unbindings: DefaultDict[T.Widget, Set[Any] ]
        # tracks all objects bound to a widget, for proper unsubscription on widget destruction.



    def __init__(self, prop=None, holder:type=None):
        self._bindings   = defaultdict(dict)
        self._unbindings = defaultdict(set)
        self._holder     = holder
        if prop:
            self.__set_name__(None, prop)

    def __set_name__(self, _, prop):
        """ (automatically called during regular "in body" declaration only) """
        self.patched_property = prop
        self.prefixed_property = BIND_PREFIX + prop

    def __repr__(self):
        return f'{ self.__class__.__name__}({self._holder.__name__}.{self.patched_property})'



    def __get__(self, obj, kls):
        """ Relay the "reading" operation to the inner descriptor, or extract the protected
            data from the object or the class.
        """
        # RATIONALS: Binding descriptor is there, so class already bound before.
        #
        #   * If an "inner_descriptor" is present: delegate the logic to it, and that is all.
        #
        #   * If kls given: return its prefixed_property if exists, otherwise transfer the getattr
        #                   call to the next parent class in line, SEARCHING FOR THE PATCHED
        #                   PROPERTY! This will apply correct the mro behavior and if ever a parent
        #                   class is bound as well, it will apply it's logic appropriately
        #
        #   * If obj given, there are several cases:
        #       - The instance has a value for prefixed_property:
        #               This means it has been set explicitly at instance level, so just return that
        #       - The instance has instead a value for its patched_property, in its `__dict__`:
        #               Extract it, assign it to the prefixed property, then return it
        #       - The instance holds nothing relevant:
        #               Apply normal mro, transferring the attribute access of the patched_property
        #               to the parent class (which will call again the descriptor, using the kls
        #               argument!).

        # Delegate...
        if self.inner_descriptor:
            out = self.inner_descriptor.__get__(obj, kls)
            return out

        if obj:
            dct = vars(obj)

            # If instance value already set through the descriptor? reuse it
            if self.prefixed_property in dct:
                out = dct[ self.prefixed_property ]
                return out

            # If instance value shadowed by the descriptor? put it in place on the
            # prefixed property and return it:
            if self.patched_property in dct:
                out = dct[ self.patched_property ]              # Extract original

                # Here, if the output is a BindingDescriptor, the user is trying to access a class
                # level property, which is itself bound (using a metaclass), while an instance of
                # obj (which is a CLASS, here!) has been bound as well.
                # In that case, the BindingDescriptor of the upper level in the hierarchy muse be
                # used instead,
                if not isinstance(out, self.__class__):
                    # Archive instance value for later (cover the case where the instance isn't the
                    # one that had been bound and was instantiated before )
                    setattr(obj, self.prefixed_property, out)
                    return out

            # Otherwise, let's try on the class itself...

            #return getattr(kls, self.patched_property)
            # ^ <<< USELESS: leads to the next lines in the function anyway!

            #return getattr(super(kls,obj), self.patched_property)
            # ^ <<< WRONG! skips the class attribute...

        # If the class had a value that got replaced by the descriptor? return it
        dct = vars(kls)
        if self.prefixed_property in dct:
            out = dct[ self.prefixed_property ]
            return out

        # Otherwise, push further in the mro, relying on python's builtin
        typ = obj if isinstance(obj, type) else kls
        out = getattr(typ.mro()[1], self.patched_property)
        return out




    def __set__(self, obj, value):
        """ Relay the "setting" operation to the inner descriptor, or set the value of the
            prefixed property on the target (may be an instance or a class).

            REMINDER:
                If the attribute is set at the class level directly, the Descriptor WILL BE LOST!
        """
        if self.inner_descriptor:
            self.inner_descriptor.__set__(obj, value)
        else:
            setattr(obj, self.prefixed_property, value)

        if obj in self._bindings:
            for cbk in self._bindings[obj].values():
                cbk(value)


    def __delete__(self, obj):
        """ Suppress the field on the property, leaving the descriptor in place.
        """
        if self.inner_descriptor:
            self.inner_descriptor.__delete__(obj)
        else:
            dct  = vars(obj)
            done = False

            if self.prefixed_property in dct:
                del dct[self.prefixed_property]
                done = True

            if self.patched_property in dct:
                del dct[self.patched_property]
                done = True

            if not done:
                raise AttributeError(f'Cannot delete attribute {self.patched_property} on {obj}')




    # WEAKREFS!?
    def subscribe(self, obj, widget, two_ways_cbk):
        """ Register the two way bindig for the given association ("model -> GUI way") """
        self._bindings[obj][widget] = two_ways_cbk
        self._unbindings[widget].add(obj)


    def unsubscribe(self, obj:Any, widget:T.Widget):
        """ Remove the update callback for the given association from the descriptor register """
        del self._bindings[obj][widget]


    def unsubscribe_on_destroy(self, widget:T.Widget):
        """ specific unsubscription for widgets destruction """
        objs = self._unbindings[widget]
        for obj in objs:
            self.unsubscribe(obj, widget)
        objs.clear()
        del self._unbindings[widget]





    @classmethod
    def bind(cls,                       # pylint: disable=too-many-locals
             instance:Any,
             prop:str,
             two_ways_cbk:Callable[[Any],None],
             widget:T.Widget
    ) -> 'BindingDescriptor':
        """ Set up the two-way binding logic for the given object/class and widget, meaning:

            - patch the class property with a BindingDescriptor if not already done
            - secure current state of this property to not lose any data
            - set up the callback so that the widget is updated after a property update
            - return the BindingDescriptor so that the widget.destroy method can be
                hacked to trigger unsubscription (this isn't done in the current function
                to avoid to create a lingering scope/callback here with widget and obj).

            NOTE: Support class level binding as well!
        """
        is_cls_level_binding = isinstance(instance, type)

        # pylint: disable-next=unidiomatic-typecheck
        if is_cls_level_binding and type(instance) is type:
            raise BindingError(
                f"Attempt to bind {instance.__name__}.{prop}:\n"
                "Binding a class level property isn't allowed if the class is directly derived "
                "from the builtin type function. An intermediate metaclass has to be defined."
            )

        kls = instance.__class__

        # State of what's currently on the class body and on the instance itself
        instance_attributes      = vars(instance)
        has_instance_level_value = prop in instance_attributes
        instance_level_value     = instance_attributes.get(prop,None)

        kls_attributes        = vars(kls)
        has_kls_level_value   = prop in kls_attributes
        kls_level_value       = kls_attributes.get(prop,None)

        is_descriptor = has_kls_level_value and bool(
            cls.DESCRIPTOR_SPECIFIC_METHODS_SET & set( dir(kls_attributes[prop]) )
        )
        is_binder_descriptor  = isinstance(kls_level_value, BindingDescriptor)
        is_kls_level_property = not is_descriptor and has_kls_level_value


        # Binder descriptor to use:
        binder = kls_level_value if is_binder_descriptor else cls(prop, kls)


        if not is_binder_descriptor:        # No Binding yet!

            if is_descriptor:               # Just archive it for __get__ accesses...
                binder.inner_descriptor = kls_level_value

            else:
                # Enforce prefixed property name availability:
                prefixed_name_defined   = binder.prefixed_property in instance_attributes
                annotations             = kls_attributes.get('__annotations__', ())
                annotated_prefixed_name = binder.prefixed_property in annotations
                if prefixed_name_defined or annotated_prefixed_name:
                    raise BindingError(
                        f"{binder.prefixed_property} must be available on the class/instance "
                        "without collisions to put a two-way binding in place."
                    )

                # Backup any existing instance level value:
                if has_instance_level_value:
                    # WARNING: an instance could have overridden the class level definition!
                    # So prepare instance level prefixed property as well, if needed
                    setattr(instance, binder.prefixed_property, instance_level_value)

                    delattr(instance, binder.patched_property)
                    # ^ <<< "clean up the place"
                    # NOTE: implementation of __get__ was using `super(typ,typ)` => doesn't work.

                # Backup default value defined at class level if any:
                if is_kls_level_property:
                    setattr(kls, binder.prefixed_property, kls_level_value)
                    # No need to delete the class attribute: replaced with the binder anyway...


            parent_dct   = dict(vars(kls.__class__))
            parent_level = parent_dct.get(prop)
            is_lower_level_binding = isinstance(parent_level, BindingDescriptor)

            # Hot patch the new descriptor on the class:
            if is_lower_level_binding:
                # Currently trying to setup a binding on an instance of the currently bound class
                # (meaning a class level binding is currently running, and an instance level is
                # being setup right now). The current descriptor logic forbids to put in place the
                # new binding, so:
                #       - Remove temporarily the current BindingDescriptor on the metaclass
                #       - Put the wanted binding in place
                #       - Put back the BindingDescriptor (ie. self!) on the metaclass

                delattr(kls.__class__, prop)
                setattr(kls, prop, binder)
                setattr(kls.__class__, prop, parent_level)

            else:
                setattr(kls, prop, binder)


        # Activate the Model -> GUI binding, at last:
        binder.subscribe(instance, widget, two_ways_cbk)
        return binder
