"""
For managing the game state & information
"""

from enum import Enum
from shutil import get_terminal_size

from trg.type import Map


class Mode(Enum):
    """
    Describes the mode the game is in
    """

    MAP = 1
    INVENTORY = 2
    SHOP = 3
    BATTLE = 4


class Game:
    """
    Game information

    This is a class so that we can actually edit information like the mode
    """

    game_map: Map = []
    TERM_SIZE = get_terminal_size()
    NAME = "TRG"
    mode = Mode.MAP
