#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_matrix = list(my_list)
    search_index=my_list.index(search)
    new_matrix[search_index] = replace
    return new_matrix
