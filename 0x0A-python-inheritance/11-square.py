#!/usr/bin/python3
"""
This module contains a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a square instance """

    def __init__(self, size):
        """
        Initializes a square instance

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square instance

        Returns:
            int: the area of the square instance
        """
        return self.__size ** 2

    def __str__(self):
        """
        Called with print() or str()

        Returns:
            str: the string representation of the square instance
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
