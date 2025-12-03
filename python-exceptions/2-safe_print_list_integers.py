#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for element in my_list:
        i = 0
        addition = 0
        if not isinstance(element,int):
            pass
        else:
            addition += 1
    try:
        while i < x:
            if not isinstance(element,int):
                pass
            else:
                print("{:d}".format(my_list[i]))
    except IndexError:
        if i < addition-1:
            while i < addition:
                print("{:d}".format(my_list[i]))
        else:
            return addition