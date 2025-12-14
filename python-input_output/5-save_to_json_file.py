#!/usr/bin/python3
"""we define save_to_json function in this module"""
import json


def save_to_json_file(my_obj,filename):

    """we use loads and open method"""
    a = json.dump(my_obj)
    with open(filename, 'w') as f:
        f.write(a)
