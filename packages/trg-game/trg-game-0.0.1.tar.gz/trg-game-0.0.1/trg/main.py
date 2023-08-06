"""
Main file for TRG
"""

from trg.player import Player
from trg.game import Game, Mode

from trg import game_map, terminal, inventory, game_input

def main():
    """
    Main function, only executes if the script is run as a program
    """

    game = Game()
    player = Player()

    print("======================")
    print(" TRG, by Tal & Henri")
    print("======================")
    input("Press enter to begin")

    print("Initializing map...")
    game.game_map = game_map.parse_map(game_map.read_map())
    terminal.clear()

    # Game loop
    while True:
        if game.mode == Mode.MAP:
            game_map.render_map(game, player)
        elif game.mode == Mode.INVENTORY:
            inventory.render_inventory(game, player)
        game_input.read_input(game, player)


if __name__ == "__main__":
    main()
