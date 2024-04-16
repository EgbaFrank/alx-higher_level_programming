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

    def area(self):
        """
        Computes the area of the rectanle instance

        Returns:
            int: area of the rectanglr instance
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Called when print or str is called

        Returns:
            str: string representation of the rectangle instance
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
