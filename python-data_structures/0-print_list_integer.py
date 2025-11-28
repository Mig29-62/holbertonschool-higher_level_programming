#!/usr/bin/python3
def print_list_integer(mylist=[]):
    length=len(mylist)
    for i in range(0,length):
        string="{}".format(i)
        print(string,end='\n')

