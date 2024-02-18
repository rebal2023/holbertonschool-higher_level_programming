#!/usr/bin/python3
"""Defines lookup function"""


def lookup(obj):
    """
    Args:
        obj: passed object

    Returns:
        list: list of attributes
    """
    return dir(obj)
