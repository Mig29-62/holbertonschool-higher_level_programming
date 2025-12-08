#!/usr/bin/python3
"""module contains the class which prints list in a sorted order"""


class MyList(list):

    """class contains function which defines print function using sorted function"""

    def print_sorted(self):
        print([item for item in sorted(self)])

    def __str__(self):
        return str(list(self))