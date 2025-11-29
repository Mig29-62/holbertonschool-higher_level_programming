#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c=[]
    list_c=[x+y for x,y in zip(tuple_a, tuple_b)]
    list_c=list_c[:2]
    tuple_c=tuple(list_c)
    return tuple_c
