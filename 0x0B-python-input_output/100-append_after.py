#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file, after
each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string.

    Args:
        filename (str): The name of the file to modify. Defaults to "".
        search_string (str): The string to search for in the file. Defaults to
                             "".
        new_string (str): The string to insert after the search string.
                          Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
