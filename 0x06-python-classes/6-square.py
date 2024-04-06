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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance

        Args:
            size: the size of the square. Defaults to 0
            position: coordinate of the square. Defaults to 0
            position[0] = x, the horizonatal position
            position[1] = y, the vertical position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Gets the size of the square's side

        Returns:
            int: the value of the square's side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's side

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

    @property
    def position(self):
        """
        Gets the coordinates of the square

        Returns:
            tuple: the coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value(tuple): coordinates of the square

        Raises:
            TypeError: if value is not a tuple or is negative
        """
        flag = 0
        if not isinstance(value, tuple) or len(value) != 2:
            flag = 1
        elif not all(isinstance(item, int) and item >= 0 for item in value):
            flag = 1
        if flag == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of a square instance

        Returns:
            returns the square's area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square at specified coordinates
        of entered size,
        or a blank line if size is 0
        """
        a, b = self.__position
        for i in range(b):
            print()
        for i in range(self.__size):
            print(" "*a, end='')
            print("#"*self.__size)
        if self.__size == 0:
            print()
