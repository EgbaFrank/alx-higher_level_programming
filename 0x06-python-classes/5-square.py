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
        Gets the size of the square side

        Returns:
            int: the size of the square side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square side

        Args:
            value(int): The square's side new value

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

    def my_print(self):
        """
        Prints a square of entered size,
        or a blank line if size is 0
        """
        for i in range(self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print()
