import warnings
from dataclasses import dataclass
# from decoders import print_with_style
from screen import Screen
from index_rounder import index_error_overrider as ieo
from __init__ import USER
# from id import ID
from abc import ABC, abstractmethod
import default_logger_configuration_for_logging as dlcl

###########################              CONSTANTS                  ############################
LOGGER = dlcl.default_logger_configuration_for_logging("eyes")  # since it watches the entire goddamn thing
USER = USER
##############################


# class NonStandardDynamicInternalStream:  # guys look this is the class that the creator made his first video about
#     """ an internal stream for situations where return keyword is don't work
#     :usage: just create a stream instance (you must do that as the first thing) and give it a name, then use """
#     def __init__(self):
#         self.__stream = StringBuffer(prelisting=False)
#         self._stream_name_lis: list[str | int | ID] = []  # THIS IS JUST A SKETCH NOTHING WORKS DONT USE THIS
#
#     def stream_capturer(self, name: int | str | ID):  # FIXME: use a auto-scalable data class
#         raise NotImplementedError("not done yeeeet")


class Reference:
    """first RTFM (read the FU**ING manual)
    if you have a very big object, instead of copying, make a reference to it also use only slicable objects"""

    def __init__(self, main_object, main_object_getter_attribute):
        self.main_object = main_object
        self.main_object_getter_attribute = main_object_getter_attribute

    def __getitem__(self, item):
        return self.main_object[item]

    def get_item(self, item):
        warnings.warn("READ THE FU**ING MANUAL AND USE THE DAMN BRACKETS YOU IDIOT", SyntaxWarning)
        return self.main_object[item]


class ABCClassForNonGetItemSupportiveClasses(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass


@dataclass
class Cell:
    """ the class that has all the data for the cell
    :param color: the color of the cell
    :param size: the size of the cell
    """

    color: tuple[int, int, int] | str | int = (
    0, 0, 0)  # that last int and str means that you can put hexadecimal values
    size: tuple[int, int] = (1, 1)

    def __init__(self, color: tuple[int, int, int] | str | int, size: tuple[int, int] = (1, 1)):
        self.color = color
        self.size = size


# FIXME : use a damn validator and buffererror since its actually gonna be helpful
class StringBuffer:
    """ stringling buffer class for buffering and short term and easy to use me
        the best 6-star hotel for your stringlings (6. star is because they get to stay in a shell
        where they will be safe from... IDK but probably something exist that threatens them so, how cool is that!!)"""

    def __init__(self, stringling: str = None, *, prelisting: bool = False):
        self.stringling = stringling
        self.prelisting = prelisting
        if self.prelisting:
            self.__buffer_shell = [list(self.stringling)]
        else:
            self.__buffer_shell = [stringling]

    def put(self, stringling: str):
        """a function that puts the stringling in the buffer shell and REMOVES THE ALREADY EXISTING ONE"""
        if len(self.__buffer_shell) >= 1:
            self.__buffer_shell.clear()  # buffer_shell can only have 1 stringling
        if self.prelisting:
            self.__buffer_shell.append(list(stringling))
        else:
            self.__buffer_shell.append(stringling)

    def free(self):
        """the function for freeing the buffer shell"""
        self.__buffer_shell.clear()

    def replace(self, new_stringling: str):
        """a function that replaces the old stringling with the new one"""
        self.stringling = list(new_stringling) if self.prelisting else new_stringling

    def char_generator(self, index: int,):
        """a function that returns the character at the given index"""
        if index > len(self.stringling):  # so app doesn't just crash when İndexError occurs
            return self.stringling[ieo(len(self.stringling), index=index)]
        else:
            return self.stringling[index]


class CellPointer(int):  # pointer for short because Im but a monster >:)
    """the official class for the (unholy) cell pointer"""

    def __init__(self, p: int):
        self.p = p

    # ::sector-movement-::

    def slide(self, to_left: bool = True):
        if to_left:
            self.p -= 1
        else:
            self.p += 1

    def move(self, new_point: int):
        self.p = new_point

    def jump(self, subscreen_id, start_point: int = 0):
        self.p = Screen.Subscreen.get_start_point(subscreen_id) + start_point

    def goto_cell_start(self, file_sample: str):
        """goes the start of the next cell and returns starting index"""
        char_buffer = StringBuffer()
        helper_pointer = CellPointer(0)
        char_buffer.put(file_sample)
        while True:
            if char_buffer.char_generator(helper_pointer.p) == "(":
                char_buffer.free()
                self.p += helper_pointer.p
                return self.p + helper_pointer.p
            else:
                helper_pointer.p += 1
                return helper_pointer.p + 1

