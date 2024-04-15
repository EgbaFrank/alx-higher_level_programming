#!/usr/bin/python3
"""
This module contains a BaseGeometry class
"""


class BaseGeometry:
    """
    Creates a Geometry blueprint
    """
    def area(self):
        """
        Should output the geometry's area

        Returns:
            int / float: The geometry's area

        Raises:
            Exception: That is being worked on currently
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value entered

        Args:
            name (str): Name of perhaps the shape
            value (int): value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value if less than 1
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        elif value < 1:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Represents a rectangle blueprint
    """
    def __init__(self, width, height):
        """
        Initializes a new rectangle instance

        Args:
            width (int): rectangle's width size
            height (int): rectangle's height size
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
