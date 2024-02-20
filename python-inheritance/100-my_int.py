#!/usr/bin/python3
"""Class MyInt"""

class MyInt(int):
    """Represents an integer with inverted comparison operators (== and !=)"""

    def __eq__(self, other):
        """Overrides the default equality operator (`==`)"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Overrides the default inequality operator (`!=`)"""
        return not super().__ne__(other)
