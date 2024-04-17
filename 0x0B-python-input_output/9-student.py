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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: Representation of Student instance
        """
        return self.__dict__
