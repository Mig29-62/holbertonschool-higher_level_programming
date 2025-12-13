#!/usr/bin/python3
import json

"""in this module we turn a python data to json"""


def to_json_string(my_obj):

    """we use json dumps method to turn string into json"""

    return json.dumps(my_obj)