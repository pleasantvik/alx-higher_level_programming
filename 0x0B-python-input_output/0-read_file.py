#!/usr/bin/python3
"""
This function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
