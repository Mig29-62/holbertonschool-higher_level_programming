#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = [s.replace(search, replace) for s in my_list]
    return new_matrix

