#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Print list in sorted ascending order"""
        print(sorted(self))
