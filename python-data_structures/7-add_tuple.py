#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c=()
    for i in range(0,2):
        tuple_c[i]=tuple_a[i]+tuple_b[i]
    return tuple_c
