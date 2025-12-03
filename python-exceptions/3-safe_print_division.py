#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ",end='')
    except TypeError:
        pass
    finally:
        print("{:.1f}".format(a/b))
        return a/b