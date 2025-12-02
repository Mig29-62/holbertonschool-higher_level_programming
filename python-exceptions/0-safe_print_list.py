#!/usr/bin/python3
def safe_print_integer(my_list=[],x=0):
    try:
        for i in range(0,x):
            print(my_list[i])
    except IndexError:
        for i in range(0,len(my_list)):
            print(my_list[i])