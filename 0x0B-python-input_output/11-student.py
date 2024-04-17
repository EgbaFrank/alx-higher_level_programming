#!/usr/bin/python3
"""
This module contains a class ``student``
"""


class Student:
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): optional), attributes the be present.
                Defaults to none, returns all attributes

        Returns:
            dict: Representation of Student instance
        """
        if (isinstance(attrs, list)
                and all(isinstance(key, str) for key in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): dict to be replaced with
        """
        for key, value in json.items():
            setattr(self, key, value)
