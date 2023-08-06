""" Errors specific to the two-way binding tool """



class TwoWaysBindingConfigError(AttributeError):
    """ Error while registering new custom widgets configurations """



class BindingError(Exception):
    """ Error during binding """



class BindingCtrlVarError(BindingError):
    """ Cannot instantiate a control variable in Binder.on method """


class BinderError(BindingError):
    """ Wrong use of the Binder class """


class BinderLockedError(BinderError):
    """ Cannot reuse a Binder instance that already bound an object property on a widget """
