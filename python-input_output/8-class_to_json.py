#!/usr/bin/python3
"""we define object to json"""

def class_to_json(obj):
    dictionary={}
    for key,value in obj.__doc__.items():
        dictionary[key]=value
    return dictionary