#!/usr/bin/python3
def max_integer(my_list=[]):
    length=len(my_list)
    i=0
    while i > length-1:
        if my_list[i] > my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
            i += 1
        else:
            i+= 1
    return my_list[length-1]