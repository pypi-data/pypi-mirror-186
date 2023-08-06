"""
For capturing user input and then executing code based on that input
"""

import readchar

from trg.game import Mode, Game
from trg.player import Player


def read_input(game: Game, player: Player):
    """
    Reads a singular character and then executes something based on that character

    Keybinds:

    Q:          Quit the game
    E:          Open inventory
    M:          Open map
    S:          Open shop (TODO)
    ARROW KEYS:
                MAP:       Moves the character
                INVENTORY: Navigates inventory
                BATTLE:    Navigates battle menu (TODO)
                SHOP:      Navigates shop menu   (TODO)
    """

    key = readchar.readkey()

    # Quit
    if key == "q":
        quit(0)

    # Switching Modes
    elif key == "e":
        game.mode = Mode.INVENTORY
    elif key == "m":
        game.mode = Mode.MAP

    # MAP mode keybinds
    elif game.mode == Mode.MAP:
        if key == readchar.key.UP:
            player.move_up(game)
        elif key == readchar.key.DOWN:
            player.move_down(game)
        elif key == readchar.key.LEFT:
            player.move_left(game)
        elif key == readchar.key.RIGHT:
            player.move_right(game)
