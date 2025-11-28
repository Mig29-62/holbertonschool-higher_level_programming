#!/usr/bin/python3
def print_list_integer(mylist=[]):
    length=len(mylist)
    for i in range(0,length):
        string="{:d}".format(mylist[i])
        print(string,end='\n')

