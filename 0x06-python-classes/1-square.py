#!/usr/bin/python3
"""Module: square.py

This module defines a Square class for representing square objects.

Classes:
    Square: Represents a square object
"""


class Square:
    """
    Defines a square object

    This class defines a square object with no
    attributes
    """
    def __init__(self, size):
        """
        Initializes a new square instance

        Args:
            size: the size of the square
        """
        self.__size = size
