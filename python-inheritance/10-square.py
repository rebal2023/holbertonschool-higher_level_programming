#!/usr/bin/python3
"""Define Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass representing a rectangle"""

    def __init__(self, size):
        """Initialize a new square"""
        
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method for area of square"""
        return self.__size ** 2
