#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorted=dict(sorted(a_dictionary.items()))
    for element in dict_sorted.items():
        print (dict_sorted(element),end='\n')