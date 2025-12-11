#!/usr/bin/python3
"""the module which defines base geometry class"""


class BaseGeometry:
    """Basegeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) == bool:  # noqa: E721
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return 1


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

