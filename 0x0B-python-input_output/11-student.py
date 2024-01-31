#!/usr/bin/python3
"""
This module contains a class Student that defines a student by.
"""


class Student:
    """A class Student that defines a student by.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list of str): A list of attribute names to filter.

        Returns:
            dict: The dictionary representation of the student's attributes.
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary of new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
