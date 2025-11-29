#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c=[]
    list_c=list(tuple_a) + list(tuple_b)
    tuple_c=tuple(list_c)
    return tuple_c
