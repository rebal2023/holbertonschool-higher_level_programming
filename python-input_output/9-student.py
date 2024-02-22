#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Class Student that defines a student by first_name , last_name & age"""

    def __init__(self, first_name, last_name, age):
        """Create a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description of the Student"""
        return self.__dict__
