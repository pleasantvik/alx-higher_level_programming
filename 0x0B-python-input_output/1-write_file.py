#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8) and returns the number
of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The string to write to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
