#!/usr/bin/python3
"""we define file writing function in this module"""
def write_file(filename='',text=''):
    """we write to file using write method"""
    with open('filename',encoding='utf-8') as f:
        f.write(text)
