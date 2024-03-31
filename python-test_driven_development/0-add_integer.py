#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """checks if a is integer or float"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    """checks if b is integer or float"""
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    """return the addition of a and b"""
    return int(a) + int(b)
