#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    addition = 0
    i = 0
    for element in my_list:
        if not isinstance(element,int):
            pass
        else:
            addition += 1
    try:
        while i < x:
            if not isinstance(element,int):
                pass
            else:
                print("{:d}".format(my_list[i]),end='')
            i += 1
    except IndexError:
        if i < addition-1:
            while i < addition:
                print("{:d}".format(my_list[i]),end='')
                i += 1
        else:
            return addition
    except TypeError:
        if i < addition-1:
            while i < addition:
                print("{:d}".format(my_list[i]),end='')
                i += 1
        else:
            return addition