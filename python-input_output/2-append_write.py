#!/usr/bin/python3
"""function that appends a string"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and
    returns the number of characters added

    filename : string
    text : string

    Returns:
    int: Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
