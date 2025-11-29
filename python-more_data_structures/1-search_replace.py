#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_matrix = [0 for y in range(length)]
    search_index=my_list.index(search)
    new_matrix[search_index] = replace
    return new_matrix
