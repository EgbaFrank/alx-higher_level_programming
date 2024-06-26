#!/usr/bin/python3
"""
Module: square.py

This module defines a Square class for representing square objects.

Classes:
    Square: Represents a square object.
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

        Raises:
            TypeError: if value is not integer

            ValueError: if value is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
