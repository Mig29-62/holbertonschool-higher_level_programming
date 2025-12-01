#!/usr/bin/python3
def best_score(a_dictionary):
    maximum=0
    for key in a_dictionary:
        if a_dictionary[key] > maximum:
            maximum = a_dictionary[key]
    return maximum