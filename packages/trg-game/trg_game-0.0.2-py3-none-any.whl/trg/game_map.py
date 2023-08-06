"""
For managing the game map & camera
"""

import math
from importlib.resources import files
import os

import trg.terminal
from trg.game import Game
from trg.player import Player
from trg.type import Map


def read_map() -> str:
    """
    Reads the map text file (`map.txt`)

    MASSIVE WARNING: USE A RECTANGULAR MAP. NON RECTANGULAR MAPS BREAK EVERYHING
    """

    path = os.path.join(os.path.dirname(__file__), 'data', 'map.txt')

    with open(path, "r", encoding="UTF-8") as file:
        content = file.read()
        return content.strip("\n")

    # content = files("trg.data").joinpath('map.txt').read_text()
    # return content.strip("\n")


def parse_map(raw_map: str) -> Map:
    """
    Parses the map
    """

    parsed_map: Map = []
    lines = raw_map.split("\n")

    for line in lines:
        chars = list(line)

        parsed_map.append(chars)

    return parsed_map


def calculate_camera_columns(line: list[str], player: Player, game: Game):
    """
    Calculate what part of the row can fit on the screen

    For example:

    ```
    ----------------------i------------------------
        ^ CHOPS OFF HERE       AND HERE ^
        < -------- TERM SIZE ---------- >
    ```
    Note: This example will probably look very strange if you don't use a monospace font
    """

    term_size = game.TERM_SIZE.columns

    area_from = math.floor(player.coordinates[0] - (term_size / 2))
    area_to = math.floor(player.coordinates[0] + (term_size / 2))

    # This code essentially makes it so that if the player gets close enough to the edge,
    # The camera will not move past the edge. This is pretty common for camera systems.

    # Close to left edge
    if area_from < 0:
        area_from = 0
        area_to = term_size

    # Close to right edge
    if area_to > len(line):
        area_to = len(line)
        area_from = term_size * -1

    area_to_print = line[area_from:area_to]

    return area_to_print


def calculate_camera_rows(game_map: Map, player: Player, game: Game):
    """
    Calculate which rows can fit on the screen

    For example:
    ```

                                      ---
              ^     CHOPS OFF HERE -> ---
              |                       -i-
    TERM SIZE |                       ---
              |                       ---
              .     CHOPS OFF HERE -> ---
                                      ---
    ```
    Note: This example will probably look very strange if you don't use a monospace font
    """

    # -1 To account for trailing newline at the end of the map
    term_size = game.TERM_SIZE.lines - 1

    area_from = math.floor(player.coordinates[1] - (term_size / 2))
    area_to = math.floor(player.coordinates[1] + (term_size / 2))

    # Close to top
    if area_from < 0:
        area_from = 0
        area_to = term_size

    # Close to bottom
    if area_to > len(game_map):
        area_to = len(game_map)
        area_from = term_size * -1

    area_to_print = game_map[area_from:area_to]

    return area_to_print


def render_map(game: Game, player: Player):
    """
    Renders the map and prints it to the screen
    """

    # Make copy of game map
    # Note: any modifications we make to 'map' will also apply to 'game.map' because of refrences
    game_map = game.game_map

    # Save previous tile
    previous_tile = game_map[player.coordinates[1]][player.coordinates[0]]

    # Plot the player
    game_map[player.coordinates[1]][player.coordinates[0]] = "i"

    # Calculate how to print the map
    map_to_print = ""
    area_of_map_to_print = calculate_camera_rows(game_map, player, game)

    for line in area_of_map_to_print:
        area_of_line_to_print = calculate_camera_columns(line, player, game)
        map_to_print += "".join(area_of_line_to_print) + "\n"

    # After it's calculated, we put back the tile where the player use to be,
    # so we don't have duplicates of the player
    # This is actually much faster than making a deep copy of 'game.map',
    # and we need this to be as fast as possible so the terminal doesn't flash
    game_map[player.coordinates[1]][player.coordinates[0]] = previous_tile

    # Clearing after we have already calculated the map to reduce the flashing,
    # so we can just display the old map while the new one is rendering
    trg.terminal.clear()

    # NOTE: This will produce a trailing newline (\n at the end of the output)
    # This is to prevent cursor flicker on some terminals
    print(map_to_print.strip("\n"))
