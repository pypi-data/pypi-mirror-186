"""
For managing all items
"""


class Item:
    """
    It's an item, pretty self explanitory
    """

    def __init__(self, name: str):
        self.name = name


class Weapon(Item):
    """
    A weapon, inherits from Item
    """

    def __init__(self, name: str, damage: int):
        super().__init__(name)
        self.damage = damage


Items = {
    "ROCKET_LAUNCHER": Weapon("Rocket Launcher", 4),
}
