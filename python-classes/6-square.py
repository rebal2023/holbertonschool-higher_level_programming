#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute named size"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
        
    @property
    def size(self):
        """Get / Set the current square size"""
        return self.__size

    @property
    def position(self):
        """Get / Set the current square position"""
        return self.__position
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
                print()
