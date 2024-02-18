#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        """function to calculate this area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
