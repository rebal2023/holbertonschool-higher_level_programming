#!/usr/bin/python3
"""is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of the specified class or subclass"""
    
    if isinstance(obj, a_class):
        return True
    return False
