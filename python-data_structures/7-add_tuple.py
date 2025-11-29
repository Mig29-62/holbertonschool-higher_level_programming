#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c=[]
    for i in range(0,2):
        c=tuple_a[i]+tuple_b[i]
        list_c.append(c)
    tuple_c=tuple(list_c)
    return tuple_c
