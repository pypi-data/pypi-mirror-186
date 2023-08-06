"""
For managing the terminal
"""

from shutil import get_terminal_size


def clear():
    """
    Clears the screen by printing a lot of new lines
    """

    # Prints out a ton of new lines to clear the terminal
    # Somehow it is faster than os.system("clear") and minimizes flashing
    print("\n" * get_terminal_size().lines, end="\x1b[H")
