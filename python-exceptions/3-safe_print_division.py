#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c=a/b
        print("Inside result:",end='')
    except:
        pass
    finally:
        print("{:.2f}".format(c))
        return c