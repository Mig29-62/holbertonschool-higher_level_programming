#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l1=list(sorted(a_dictionary.items()))
    for element in l1:
        print(element, end='\n')