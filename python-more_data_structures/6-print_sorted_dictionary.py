#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l1=list(sorted(a_dictionary.keys()))
    l2=list(a_dictionary.values())
    for key in l1:
            string='{}:{}'.format(key,l2[key])
            print(string,end='\n')
            continue

