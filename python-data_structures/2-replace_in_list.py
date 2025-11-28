#!/usr/bin/python3
def element_at(my_list, idx,element):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx > length-1:
        return my_list
    else:
        my_list[idx]=element
        return my_list[idx]
