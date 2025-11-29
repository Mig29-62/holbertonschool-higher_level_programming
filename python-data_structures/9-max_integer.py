#!/usr/bin/python3
def max_integer(my_list=[]):
    length=len(my_list)
    i=0
    j=0
    max=0
    while i < length-1:
        while j < length-1:
            if my_list[i]>my_list[j]:
                max=my_list[i]
            else:
                max=my_list[j]
            j=j+1
        i=i+1
    return my_list[length-1]