#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):  # noqa: E251
    length = len(mylist)
    for i in range(length,0):
        string = "{:d}".format(mylist[i])
        print(string, end='\n')  # noqa: E251
