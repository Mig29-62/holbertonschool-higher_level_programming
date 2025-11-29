#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c=[]
    for i in range(0,2):
        if tuple_a[i] or tuple_b[i] in tuple_a or tuple_b:
            c=tuple_a[i]+tuple_b[i]
            list_c.append(c)
        else:
            list_c.append(0)
    tuple_c=tuple(list_c)
    return tuple_c
