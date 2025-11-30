#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list=list(set(my_list))
    addition=0
    for element in my_list:
        if element in my_list and not new_list:
            addition += element
        else:
            continue
    return addition