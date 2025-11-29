#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_matrix = list(my_list)
    for element in new_matrix:
        if element == search:
            search_index = my_list.index(search)
            new_matrix[search_index] = replace
            continue
    return new_matrix

