#!/usr/bin/python3
"""Define a function that inserts a line of text to a file"""


def append_after(filename, search_string, new_string):
  """
  Inserts a line of text after each line containing a specific string in a file.

  Args:
    filename: The name of the file to modify.
    search_string: The string to search for in the file.
    new_string: The line of text to insert after each matching line.
  """
  with open(filename, "r+") as file:
    lines = file.readlines()
    modified_lines = []
    for line in lines:
      modified_lines.append(line)
      if search_string in line:
        modified_lines.append(new_string + "\n")
    file.seek(0)
    file.writelines(modified_lines)
