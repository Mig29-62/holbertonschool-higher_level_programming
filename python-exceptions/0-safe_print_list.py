#!/usr/bin/python3
def safe_print_integer(my_list=[],x=0):
    try:
        for i in range(0,x):
            print(my_list[i],end='')
        print('\n')
        return x
    except IndexError:
        addition=0
        for element in my_list:
            print(element,end='')
            addition += 1
        print('\n')
        return addition