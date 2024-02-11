#!/usr/bin/python3
"""Empty class that defines a rectangle"""


class Rectangle:
    """Empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle"""
        
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @property
    def height(self):
        """Get height"""
        return self.__height
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width*2) + (self.__height*2)
