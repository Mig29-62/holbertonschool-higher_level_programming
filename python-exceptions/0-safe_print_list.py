#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    addition=0
    for element in my_list:
        addition += 1
    try:
        for i in range(0,x):
            print(my_list[i],end='')
        print('\n',end='')
        return x
    except x != addition:
        for element in my_list:
            print(element,end='')
        print('\n',end='')
        return addition