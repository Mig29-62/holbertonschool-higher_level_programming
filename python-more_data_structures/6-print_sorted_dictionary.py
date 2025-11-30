#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l1=list(sorted(a_dictionary.keys()))
    l2=list(a_dictionary.values())
    for key,value in l1,l2:
            string='{}:{}'.format(key,value)
            print(string,end='\n')


