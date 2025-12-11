#!/usr/bin/python3
"""the module which defines base geometry class"""


class BaseGeometry:
    """Basegeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) == Bool:
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
        else:
            name = value

