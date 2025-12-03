#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    addition = 0
    for element in my_list:
        if  isinstance(addition,int):
            addition += 1
        else:
            pass
    for i in range(0,x):
        try:
            print("{:d}".format(my_list[i]),end='')
        except IndexError:
            break
    print('\n',end='')
    if x < addition:
        return x
    elif x > addition:
        return addition
    else:
        return addition
