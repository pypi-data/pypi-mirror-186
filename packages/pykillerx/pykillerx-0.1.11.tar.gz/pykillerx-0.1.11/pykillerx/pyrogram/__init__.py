from ._wrappers import eod, eor
from .func import Function
from .misc import Misc
from .sections import section
from .toolbot import ToolBot
from .tools import Tools


class DarkMethods(
    Function,
    Misc,
    ToolBot,
    Tools,
):
    pass
