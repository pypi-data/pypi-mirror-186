"""
# Welcome to TkUtils

`tkutils` is a package offering some additional logic and syntactic sugar when using tkinter.
The main goal is to fill some gaps of tkinter, which might make it very annoying to use.

Online version of the help documentation: http://frederic.zinelli.gitlab.io/tkutils/



## Features


### Additional logic: two-way binding with [`Binder`](http://frederic.zinelli.gitlab.io/tkutils/binder/binder_overview/)

The [`Binder`](http://frederic.zinelli.gitlab.io/tkutils/binder/binder_overview/) class is an utility to setup a transparent two-way
binding reactivity between widgets and underlying object properties from the model/logic layer
of the application.

Several advantages come with this:

* Changes of bound properties in the model layer are cascading in the GUI automatically.
* The model layer of the application becomes (finally) totally independent from the presentation
  layer. This means it becomes very easy to build and test the model layer, without any need to
  think about its integration with `tkinter` itself.



### Syntactic sugar


#### [`GridLayout`](http://frederic.zinelli.gitlab.io/tkutils/grid_layout/grid_layout/)

A grid layout manager which is abstracting away all the naughty `widget.grid(...)` calls and
rows/columns grid configuration. Positioning widgets in the grid and controlling their "spanning"
becomes very easy, without extra typing.


#### [`MenuBuilder`](http://frederic.zinelli.gitlab.io/tkutils/menu_builder/menu_builder/)

A helper to build menus and to abstract away all the technicalities, when creating menus through
`tkinter`, which quickly make the declarations very unclear. Using the [`MenuBuilder`](http://frederic.zinelli.gitlab.io/tkutils/menu_builder/menu_builder/),
the actual Menu hierarchy becomes very obvious: "what you see is what you get".


#### [`Event`](http://frederic.zinelli.gitlab.io/tkutils/event/)

An utility to build event strings with autocompletion/IDE suggestions support.


#### [`KeySym`](http://frederic.zinelli.gitlab.io/tkutils/key_sym/)

An utility to get all keysym informations with autocompletion/IDE suggestions (providing string,
keycode and keysym_num values).


#### [`images`](http://frederic.zinelli.gitlab.io/tkutils/images/images/)

Various factories related to images to:

* Simplify and reduce the syntaxes/typing needed,
* Handle file conversions automatically,
* Register automatically the image object on the host for the user (to avoid garbage collection).




## Requirements

- python 3.8+
- Pillow



## Installation

* Through [PyPi](https://pypi.org/project/tkutils/):

```bash
pip install tkutils
```

* Using an archive file (with the appropriate version number):

```bash
pip install tkutils.1.0.2.tar.gz
```

* Cloning the [GitLab repository](https://gitlab.com/frederic.zinelli/tkutils).


"""

from .helpers.event_provider import Event, EventStr
from .helpers.keysym import KeySym
from .grid_layout import GridLayout
from .menu_builder.menu_builder import MenuBuilder
from .images import (
    images_factory,
    widgets_with_images_factory,
)
from .two_way_binding import (
    BindingError,
    BinderError,
    BinderLockedError,
    BindingCtrlVarError,
    TwoWaysBindingConfigError,

    Binder,
    BinderConfig,
)

__all__ = [
    'Event',
    'EventStr',

    'KeySym',

    'GridLayout',

    'MenuBuilder',

    'images_factory',
    'widgets_with_images_factory',

    'BindingError',
    'BinderError',
    'BinderLockedError',
    'BindingCtrlVarError',
    'TwoWaysBindingConfigError',

    'Binder',
    'BinderConfig',
]