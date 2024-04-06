#!/usr/bin/python3
"""Module: square.py

This module defines a Square class for representing square objects.

Classes:
    Square: Represents a square object with methods for calculating its area.
"""


class Square:
    """
    Defines a square object

    This class defines a square object with no
    attributes
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size: the size of the square. Defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the value of the property

        Returns:
            int: the value of the property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of a property

        Args:
            value(int): The property's new value

        Raises:
            TypeError: if value is not integer

            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of a square instance

        Returns:
            returns the square's area
        """
        return self.__size ** 2
