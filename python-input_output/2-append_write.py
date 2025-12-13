#!/usr/bin/python3
"""we define append function in this module"""


def append_write(filename="", text=""):

    """we use 'a' and 'w' regimes to write to file"""

    if filename:
        with open(filename, 'a') as f:
            f.write(text)
    else:
        with open(filename, 'w') as f:
            f.write(text)