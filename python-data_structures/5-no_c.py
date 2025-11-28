#!/usr/bin/python3
def no_c(my_string):
    for ch in my_string:
        if ch not in('c','C'):
            new_string += ch
    return new_string