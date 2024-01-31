#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation of an
object (string).
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to serialize.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
