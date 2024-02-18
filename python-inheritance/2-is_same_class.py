#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """function returns True if object is an instance of the specified class"""

    return type(obj) is a_class
