#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description with
simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON
        serialization of an object.

    Args:
        obj (any): An instance of a class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
