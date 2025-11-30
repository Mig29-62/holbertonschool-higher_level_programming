#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list=list(set(my_list))
    addition=0
    for element in my_list:
        count=my_list.count(element)
        if count > 1:
            addition=addition+element
        else:
            continue
    return addition