#!/usr/bin/python3
"""
This module contains a BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
