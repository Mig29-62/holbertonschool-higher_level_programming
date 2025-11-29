#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = list(my_list)
    while search in my_list:
            search_index = my_list.index(search)
            new_matrix[search_index] = replace
    return new_matrix

