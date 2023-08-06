"""
Define the logistic to build the equivalent of Namespaces (argparse), but which are
singletons, mutable or not (shallow if not), and hold some utilities to work with them
(iteration, containment, item access and modification, observers, conversion to dict).
"""
# pylint: disable=too-few-public-methods, no-value-for-parameter
#                                         |-> for: "cls._keys()" stuff

from typing import Any, Dict, Tuple, Type
from collections import Counter




def check_not_in_body(prop:str, body:Dict[str,Any], cls:Type['MetaIIIN']):
    """ Verify that the given property name has not been defined by the user on his new
        Singleton or MutableSingleton class.
    """
    if prop in body:
        raise ValueError(
            f'{ prop !r} cannot be used as a property in a {cls.__name__} class, because '
            f'it is used there to keep track of some internal states.'
    )



def is_public_prop_or_is_lambda(name:str, prop_value:Any) -> bool:
    """ Determine if the given name/property pair should be iterated over or not, in a
        MetaIIIN instance.
            - Private or protected properties will never be.
            - class methods and static methods are skipped (they can be spotted at class
              declaration time because the value associated to the name isn't a callable yet).

        Any other property/value will be iterated over.
    """
    cls_name = hasattr(prop_value,'__class__') and prop_value.__class__.__name__
    return (
            not name.startswith('_')
        and cls_name != 'classmethod'
        and cls_name != 'staticmethod'
    )



def is_class_or_static_method(prop_value:Any) -> bool:
    """ Determine if the given name/property pair should be identified as an immutable method
        for MetaMIIN instance.
    """
    cls_name = hasattr(prop_value,'__class__') and prop_value.__class__.__name__
    return cls_name in ('classmethod','staticmethod')




class MetaIIIN(type):
    """ Metaclass used to define Immutable, Iterable, Indexable, Namespace classes.

        The classes using `MetaIIIN` as metaclass:

            - Cannot be instantiated (`__init__` and `__new__` throw TypeError).

            - Do not allow mutation of their properties, once defined in the class body
              (shallow immutability / throw AttributeError).

            - All public properties defined in class body can be iterated over, associated with
              their values, doing `for k,v in cls`.
              Static and class methods aren't iterated over, but any lambda of simple fonction
              defined inside the body wll be considered a callback associated to a property.

            - All non private and non protected items can be rendered as dict with `cls.to_dict()`

            - Inheritance is working as expected, whatever its depth.


        Namespace functions/methods and inheritance behaviors:

        A class built from MetaIIIN can define functions in its body in various ways.
        From a technical point of view, all those are working, but some present some drawbacks.

            - Class methods, with the cls argument, which behaves like the usual (inheritance
              included). That's the way you're supposed to use... (see below)

            - Static methods, which behaves exactly like the two next, at runtime, and so are
              accessible through inheritance, which is in contradiction with what usually happens
              with regular classes. So don't use static methods.

            - Regular functions (no argument needed for any context). Pylint will complain with
              the absence of argument, but that works.

            - Assigned lambdas, using whatever arguments you want. Pylint will as well, but
              about not using the "def" keyword, this time...

        In any of these cases, the body of the functions can make use of any of the property of
        the class, inherited or not, according to it's public/protected/private status.

        But... When iterating over the properties, one would expect to not iterate over methods
        (comparing to the content of the __dict__ of an instance, in usual OOP situations: the
        dict holds the properties, but not the methods). It's easy to spot static or class methods
        but it's not possible to differentiate properties holding a reference toward a function
        defined somewhere else from a regular "def" function definition done directly in the class.
        For that reason, all functions, whatever the way they are defined will be considered
        callbacks associated to property names and will be iterated over, while class (and static)
        methods will be skipped.
        To avoid confusions, regular "def" function definitions and @staticmethod definitions
        should be avoided in MetaIIIN instances, and if behaviors involving protection or privacy
        are needed, this should be handled through @classmethod definitions only.


        Examples:

        ```python
            class A(Singleton):
                regular = 42
                _protected = 55
                __privy = 1

                def bla():              # (works, but don't use that... pylint is complaining)
                    print(A.__privy)

                @staticmethod           # (works but don't use that... weird inheritance behavior)
                def bla_static():
                    print(A.__privy)

                @classmethod
                def bla_cls(cls):
                    print(cls._protected)
                    print(cls.__privy)


            class B(A):
                @classmethod
                def bla_cls(cls):
                    super().bla_cls()

                @classmethod
                def no_access_to_private_parent_field(cls):
                    print(cls._protected)
                    # cls.__privy           # <<< doesn't work!


            assert '_protected' not in A.to_dict(), "protected properties aren't accessible"
            assert 'regular' in B.to_dict(), "inherited properties are accessible"
        ```
    """
    _singleton_data: Dict[str,Any]


    def __new__(cls, name:str, parents:Tuple, body:Dict[str,Any]):
        check_not_in_body('_singleton_data', body, cls)

        all_items = cls._collect_hierarchy_data(cls,parents,body,'_singleton_data')

        body['_singleton_data'] = dict((k,v) for k,v in all_items.items()
                                             if is_public_prop_or_is_lambda(k,v))

        return type.__new__(cls, name, parents, body)



    def _collect_hierarchy_data(cls, parents:Tuple, body:Dict[str,Any], target_prop:str):
        iiin_parents = [p for p in parents if isinstance(p, MetaIIIN)]
        cnt_types    = Counter(map(type, iiin_parents))
        if len(cnt_types) > 1:
            raise TypeError(
                "Cannot mix MetaIIIN and MetaMIIN in inheritance chains: "+str(cnt_types)
            )

        # Handle inheritance of properties/items of the parents, following reversed mro order, to
        # keep the order of definition from parent to child, then add the current body (same reason)
        items = dict( item for parent in reversed(iiin_parents)
                           for item in getattr(parent,target_prop).items() )
        items.update(body)
        return items


    def _do_not_do_that(cls, msg):
        """ Raises AttributeError with the given message """
        raise AttributeError(f'{cls.__name__} class cannot be mutated ({ msg })')


    def __call__(cls, *a, **kw):                        # Singletons are... singletons
        msg = f"{cls.__name__} class is a singleton namespace: it cannot be instantiated"
        raise TypeError(msg)


    def __getitem__(cls, key:str):                      # Singletons are indexable
        if key not in cls._singleton_data:
            raise AttributeError(f"{key} property is not exist accessible")
        return getattr(cls,key)


    def __setattr__(cls, name:str, value:Any):          # Singletons are immutable (shallow)
        cls._do_not_do_that(
            f"attempt to {'modify' if hasattr(cls,name) else 'define'}  {name!r} with {value!r}"
        )

    def __delattr__(cls, name:str):                     # Singletons are immutable (shallow)
        cls._do_not_do_that(f"attempt to delete {name!r} attribute")



    def _keys(cls):
        return cls._singleton_data.keys()

    def _values(cls):
        return cls._singleton_data.values()



    def __iter__(cls):                                  # Singletons are iterable (k,v) pairs
        return iter(zip( cls._keys(), cls._values() ))

    def __contains__(cls, key:str):                     # Singletons support containment check
        return key in cls._singleton_data

    @property
    def keys(cls):
        """ Convert the Singleton class to a tuple of keys """
        return tuple(cls._keys())

    @property
    def values(cls):
        """ Convert the Singleton class to a tuple of values """
        return tuple(cls._values())

    def to_dict(cls):
        """ Convert the Singleton class to a dict (with inherited items / protected and
            private items excluded)
        """
        return dict(iter(cls))









class MetaMIIN(MetaIIIN):
    """ Mutable version of MetaIIIN.

        Only public properties can be mutated or deleted. Class methods (or static ones, but
        remember you shouldn't use those...) are considered immutable, on the other hand.

        Note that reassigning an inherited property behaves like assigning at instance level
        a property that was defined at class level, so properties of children classes can
        shadow those of their parent classes without modifying the parent property.
    """

    _class_methods: Dict[str,Any]   # Actually used like a Set, but kept as Dict to keep the
                                    # logic centralized in MetaIIIN type


    def __new__(cls, name:str, parents:Tuple, body:Dict[str,Any]):
        check_not_in_body('_class_methods', body, cls)

        all_items = cls._collect_hierarchy_data(cls,parents,body,'_class_methods')

        body['_class_methods'] = dict((k,v) for k,v in all_items.items()
                                            if is_class_or_static_method(v))

        return super().__new__(cls, name, parents, body)


    def _values(cls):
        """ Override the behavior of MetaIIIN to extract the value at runtime """
        return (getattr(cls,k) for k in cls._keys())


    def _check_and_raise_if_not_doable(cls, what:str, name:str):
        """ Raises AttributeError with the given info if wrong property used """
        if name in cls._class_methods or name.startswith('_'):
            raise AttributeError(
                f'Cannot {what} private or protected attributes, or class method: {name!r}'
            )


    def __delattr__(cls, name:str):
        cls._check_and_raise_if_not_doable('delete', name)
        type.__delattr__(cls, name)
        del cls._singleton_data[name]


    def __setattr__(cls, name:str, value:Any):
        cls._check_and_raise_if_not_doable('set', name)
        type.__setattr__(cls, name, value)
        cls._singleton_data[name] = value


    def __setitem__(cls, name:str, value:Any):
        setattr(cls, name, value)













class Singleton(metaclass=MetaIIIN):
    """ Classes inheriting from Singleton are the equivalent of Namespaces which are:
            - Singletons
            - Not instantiable
            - Immutable (shallow)
            - Extendable at any depth, keeping consistency about protected and private
              properties of the parents
            - Iterable (`for key,value in SingletonChild`, for their public properties)
            - Can be converted to dict (`Singleton.to_dict()`, public properties only)

        See MetaIIIN documentation for more details.
    """






class MutableSingleton(metaclass=MetaMIIN):
    """ Classes inheriting from MutableSingleton are the equivalent of Namespaces which are:
            - Singletons
            - Not instantiable
            - Mutable (updating, adding, deleting properties. Class methods are locked/protected
              at class body declaration, on the other hand).
            - Extendable at any depth, keeping consistency about protected and private
              properties of the parents
            - Iterable (`for key,value in SingletonChild`, for their public properties)
            - Can be converted to dict (`Singleton.to_dict()`, public properties only)

        See MetaIIIN and MetaMIIN documentation for more details.
    """
