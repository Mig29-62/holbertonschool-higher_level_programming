#!/usr/bin/python3
"""the module contains data about reading file"""


def read_file(filename=""):
    with open('filename', encoding='utf-8') as f:
        reading = f.read()
        return reading