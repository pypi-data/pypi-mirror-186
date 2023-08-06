"""
# Overview

`KeySym` is a helper to provide autocompletion for all `tkinter KeySym` strings, as well as their
`keycode` and `keysym_num` values (as properties of the inner Key string object itself).

# Examples

* `KeySym.Escape             ->  "Escape"`
* `KeySym.Escape.keycode     ->  9`
* `KeySym.Escape.keysym_num  ->  65307`
* ...
"""




from dataclasses import dataclass
from typing import Optional

from tkutils.utilities.singleton_namespace import Singleton
# from tkutils.singleton_namespace import Singleton

def _scoped_definition():
    """ Used to hide the elements that shouldn't be accessible from outside
        (as implementation details)
    """

    class Key(str):
        """ Key string with keycode and keysym_num values as properties """

        keycode:    int
        keysym_num: int

        def __new__(cls, code, num, name):
            # Use __new__ to bypass the limitations due to the super().__init__ interface.
            obj = super().__new__(cls, name)
            obj.keycode = code
            obj.keysym_num = num
            return obj


    @dataclass
    class KeyDesc:
        """ Descriptor to DRY the KeySym definition.
            If the name is not provided to the constructor, the attribut name will be automatically
            used as value, through the __set_name__ method.
            It the constructor receives a name, it will be used instead. This allows to decorelate
            the attribute name from its value, where needed.
        """
        keycode:    int
        keysym_num: int
        name:       Optional[str] = None
        key:        Optional[Key] = None

        def __set_name__(self, _, name:str):
            if not self.name:
                self.name = name
            self.key = Key(self.keycode, self.keysym_num, self.name)

        def __get__(self, _,__):
            return self.key



    # pylint: disable-next=redefined-outer-name, too-few-public-methods
    class KeySym(Singleton):
        """ All keysym string names """

        Alt_L       : Key = KeyDesc(64,  65513)
        Alt_R       : Key = KeyDesc(113, 65514)
        BackSpace   : Key = KeyDesc(22,  65288)
        Cancel      : Key = KeyDesc(110, 65387)
        Caps_Lock   : Key = KeyDesc(66,  65549)
        Control_L   : Key = KeyDesc(37,  65507)
        Control_R   : Key = KeyDesc(109, 65508)
        Delete      : Key = KeyDesc(107, 65535)
        Down        : Key = KeyDesc(104, 65364)
        End         : Key = KeyDesc(103, 65367)
        Escape      : Key = KeyDesc(9,   65307)
        Execute     : Key = KeyDesc(111, 65378)
        F1          : Key = KeyDesc(67,  65470)
        F2          : Key = KeyDesc(68,  65471)
        F3          : Key = KeyDesc(69,  65472)
        F4          : Key = KeyDesc(70,  65473)
        F5          : Key = KeyDesc(71,  65474)
        F6          : Key = KeyDesc(72,  65475)
        F7          : Key = KeyDesc(73,  65476)
        F8          : Key = KeyDesc(74,  65477)
        F9          : Key = KeyDesc(75,  65478)
        F10         : Key = KeyDesc(76,  65479)
        F11         : Key = KeyDesc(77,  65480)
        F12         : Key = KeyDesc(96,  65481)
        Home        : Key = KeyDesc(97,  65360)
        Insert      : Key = KeyDesc(106, 65379)
        Left        : Key = KeyDesc(100, 65361)
        Linefeed    : Key = KeyDesc(54,  106  )
        KP_0        : Key = KeyDesc(90,  65438)
        KP_1        : Key = KeyDesc(87,  65436)
        KP_2        : Key = KeyDesc(88,  65433)
        KP_3        : Key = KeyDesc(89,  65435)
        KP_4        : Key = KeyDesc(83,  65430)
        KP_5        : Key = KeyDesc(84,  65437)
        KP_6        : Key = KeyDesc(85,  65432)
        KP_7        : Key = KeyDesc(79,  65429)
        KP_8        : Key = KeyDesc(80,  65431)
        KP_9        : Key = KeyDesc(81,  65434)
        KP_Add      : Key = KeyDesc(86,  65451)
        KP_Begin    : Key = KeyDesc(84,  65437)
        KP_Decimal  : Key = KeyDesc(91,  65439)
        KP_Delete   : Key = KeyDesc(91,  65439)
        KP_Divide   : Key = KeyDesc(112, 65455)
        KP_Down     : Key = KeyDesc(88,  65433)
        KP_End      : Key = KeyDesc(87,  65436)
        KP_Enter    : Key = KeyDesc(108, 65421)
        KP_Home     : Key = KeyDesc(79,  65429)
        KP_Insert   : Key = KeyDesc(90,  65438)
        KP_Left     : Key = KeyDesc(83,  65430)
        KP_Multiply : Key = KeyDesc(63,  65450)
        KP_Next     : Key = KeyDesc(89,  65435)
        KP_Prior    : Key = KeyDesc(81,  65434)
        KP_Right    : Key = KeyDesc(85,  65432)
        KP_Subtract : Key = KeyDesc(82,  65453)
        KP_Up       : Key = KeyDesc(80,  65431)
        Next        : Key = KeyDesc(105, 65366)
        Num_Lock    : Key = KeyDesc(77,  65407)
        Pause       : Key = KeyDesc(110, 65299)
        Print       : Key = KeyDesc(111, 65377)
        Prior       : Key = KeyDesc(99,  65365)
        Return      : Key = KeyDesc(36,  65293)
        Right       : Key = KeyDesc(102, 65363)
        Scroll_Lock : Key = KeyDesc(78,  65300)
        Shift_L     : Key = KeyDesc(50,  65505)
        Shift_R     : Key = KeyDesc(62,  65506)
        Tab         : Key = KeyDesc(23,  65289)
        Up          : Key = KeyDesc(98,  65362)

    return KeySym


KeySym = _scoped_definition()
