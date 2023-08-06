
from typing import Type

from tkutils.utilities.singleton_namespace import Singleton








class EventDescriptor(str):
    """ Articulate the EventBuilder instances together, allowing to chain them
        when declaring a tkinter event.
    """

    def __get__(self, obj:'EventStr', _kls:Type['EventStr']):
        if obj is None:             # base event (Event class)
            event_str = f'<{ self }>'
        else:                       # using modifier
            event_str = f"<{ self }-{ obj[1:-1] }>"
        return EventStr(event_str)






class EventStr(str):
    """ Chaining modifiers after using the Event singletons. """

    Shift:   'EventStr'=EventDescriptor('Shift')
    """ Shift event key modifier """

    Control: 'EventStr'=EventDescriptor('Control')
    """ Control event key modifier """

    Ctrl:    'EventStr'=EventDescriptor('Control')
    """ Ctrl event key modifier """

    Alt:     'EventStr'=EventDescriptor('Alt')
    """ Alt event key modifier """

    Any:     'EventStr'=EventDescriptor('Any')
    """ Any event key modifier """

    Lock:    'EventStr'=EventDescriptor('Lock')
    """ Lock event key modifier """



    def __getattr__(self, prop:str) -> str:
        """ Build of the full event string, assuming an unknown property name
            is the "finalization" of that event.

            Returns:
                A finalized `tkinter` event string.
        """
        return self(prop)


    def __call__(self, val:Any=None) -> str:
        """ Build the final event string, with the previously chosen event and modifiers, adding
            the given argument as final element (if provided).

            Returns:
                A finalized `tkinter` event string.
        """
        event_str = self[:-1] + f'-{val}' * (val is not None) + '>'
        return event_str







class Event(Singleton):                                   # pylint: disable=too-few-public-methods
    """ Generic utility to build `tkinter` event strings with autocompletion support.

        General syntax:

        - `Event.event_name.modifier(finaliser)` (button, key name)
        - `Event.event_name.modifier.finaliser` (key name)
    """

    Activate = EventStr('<Activate>')
    """ Widget gets activated """

    Button = EventStr('<Button>')
    """ Mouse button pushed """

    ButtonRelease = EventStr('<ButtonRelease>')
    """ Mouse button released """

    Configure = EventStr('<Configure>')
    """ Resized root window """

    Click = EventStr('<ButtonRelease>')
    """ Mouse button released """

    ClickDown = EventStr('<Button>')
    """ Mouse button pushed """

    DblClick = EventStr('<Double-Button>')
    """ Mouse double click """

    TplClick = EventStr('<Triple-Button>')
    """ Mouse triple click """

    TriClick = EventStr('<Triple-Button>')
    """ Mouse triple click """

    Deactivate = EventStr('<Deactivate>')
    """ Widget gets deeactivated """

    Destroy = EventStr('<Destroy>')
    """ Widget gets destroyed """

    Enter = EventStr('<Enter>')
    """ Mouse enters the Widget """

    Expose = EventStr('<Expose>')
    """ Widget becomes visible (hidden by another window) """

    FocusIn = EventStr('<FocusIn>')
    """ widget gets focus """

    FocusOut = EventStr('<FocusOut>')
    """ Widget loses focus """

    KeyPress = EventStr('<KeyPress>')
    """ Key pressed """

    KeyRelease = EventStr('<KeyRelease>')
    """ Key released """

    LeftClick = EventStr('<ButtonRelease-1>')
    """ Mouse left button released """

    Leave = EventStr('<Leave>')
    """ Mouse leaves the widget """

    Map = EventStr('<Map>')
    """ Widget becomes visible (after .grid() or .pack()) """

    Motion = EventStr('<Motion>')
    """ Mouse move over the widget """

    Move = EventStr('<Motion>')
    """ Mouse move over the widget """

    MouseWheel = EventStr('<MouseWheel>')
    """ Mouse wheel used """

    Resize = EventStr('<Configure>')
    """ Resized root window """

    RightClick = EventStr('<ButtonRelease-3>')
    """ Mouse right button released """

    Unmap = EventStr('<Unmap>')
    """ Widget becomes invisible (.grid_remove, for example) """

    Visibility = EventStr('<Visibility>')
    """ Widget gets hidden by another window """

    Wheel = EventStr('<MouseWheel>')
    """ Mouse wheel used """
