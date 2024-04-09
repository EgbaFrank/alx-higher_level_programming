#!/usr/bin/python3
"""Module: rectangle.py

Defines a rectangle class for representing rectangle objects

Classes:
    Rectangle: represents a rectangle object
"""


class Rectangle:
    """
    Defines a rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        Initializes new rectangle object

        Args:
            width (int): rectangle's width
            height (int): rectangle's height

        Returns:
            New rectangle object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the rectangle's width

        Returns:
            int: the rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the rectangle's width

        Args:
           value (int): the new value to be set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): new value to be set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
