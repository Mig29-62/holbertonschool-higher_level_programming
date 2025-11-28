#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):  # noqa: E251
    length = len(mylist)
    i=length
    while i >= 0:
        string = "{:d}".format(mylist[i])
        print(string, end='\n')  # noqa: E251
        i -= 1