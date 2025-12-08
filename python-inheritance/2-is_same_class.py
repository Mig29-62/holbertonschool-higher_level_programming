#!/usr/bin/python3
"""in this module we define is_same_class function"""


def is_same_class(obj, a_class):

    """in this function we use isinstance to detect if the object is an instance of class"""

    if isinstance(obj,a_class) and is_same_class(obj,a_class):
        return True
    else:
        return False