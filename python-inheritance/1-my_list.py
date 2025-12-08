#!/usr/bin/python3
"""module contains the class which prints list in a sorted order"""


class MyList(list):

    """class contains function which defines print function using sorted function"""

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        sorted_list=sorted(self)
        print(sorted_list)