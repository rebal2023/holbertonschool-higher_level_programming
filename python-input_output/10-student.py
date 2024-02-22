#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """"""Class Student that defines a student by first_name , last_name & age"""

    def __init__(self, first_name, last_name, age):
        """Create new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves attribute names"""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict
