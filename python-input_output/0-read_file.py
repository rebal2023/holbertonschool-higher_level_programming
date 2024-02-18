#!/usr/bin/python3
"""Defines a function that reads a UTFS file and prints it to stdout"""


def read_file(filename=""):
    """function that reads a UTFS file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
