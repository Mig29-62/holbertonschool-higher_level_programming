#!/usr/bin/python3
def best_score(a_dictionary):
    maximum=0
    for key in a_dictionary:
        a=a_dictionary[key]
        if a > maximum:
            maximum = key
    return maximum