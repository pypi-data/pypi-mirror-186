"""
Contains the player class & any other player logic
"""

from trg.game import Game

class Player:
    """
    Player class, should only be one at a time!
    """

    coordinates = [0, 0]
    hp = 20
    money = 100
    level = 1
    inventory = []

    def move_up(self, game: Game):
        """
        Moves the player up by reducing `coordinates[1]` by 1
        """

        if self.coordinates[1] <= 0:
            return

        self.coordinates[1] -= 1

    def move_down(self, game: Game):
        """
        Moves the player down by increasing `coordinates[1]` by 1
        """

        if self.coordinates[1] >= len(game.game_map) - 1:
            return

        self.coordinates[1] += 1

    def move_left(self, game: Game):
        """
        Moves the player left by decreasing `coordinates[0]` by 1
        """

        if self.coordinates[0] <= 0:
            return

        self.coordinates[0] -= 1

    def move_right(self, game: Game):
        """
        Moves the player left by increasing `coordinates[0]` by 1
        """

        if self.coordinates[0] >= len(game.game_map[0]) - 1:
            return

        self.coordinates[0] += 1
