#!/usr/bin/python3
"""module contains the class which prints list in a sorted order"""


class MyList(list):

    """class contains function which defines print function using sorted function"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        sorted_list=sorted(self)
        print(sorted_list)

    def __str__(self):
        return str(list(self))
