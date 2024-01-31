#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The object corresponding to the JSON file.
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
