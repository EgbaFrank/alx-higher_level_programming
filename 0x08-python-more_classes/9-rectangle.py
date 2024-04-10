#!/usr/bin/python3
"""Module: rectangle.py

Defines a rectangle class for representing rectangle objects.

Classes:
    Rectangle: represents a rectangle object.
"""


class Rectangle:
    """
    Defines a rectangle object.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes new rectangle object.

        Args:
            width (int): rectangle's width
            height (int): rectangle's height.

        Returns:
            New rectangle object.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Prints a message when an instance is deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """
        Prints a rectangle of specified size
        or an empty string if any size is 0.

        Returns:
            str: string representation of the rectangle object.
        """
        string = ''
        if self.__width != 0 and self.__height != 0:
            row = str(self.print_symbol) * self.__width
            string = '\n'.join([row] * self.__height)

        return string

    def __repr__(self):
        """
        displays rectangle object's string representation.

        Returns:
            string representation of rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """
        Gets the rectangle's width.

        Returns:
            int: the rectangle's width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the rectangle's width.

        Args:
           value (int): the new value to be set.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): new value to be set.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of a rectangle instance.

        Returns:
            int: the area of the rectangle instance.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the rectangle object's perimeter.

        Returns:
            int: the perimeter of the rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        or rect_1 if equal.

        Args:
            rect_1 (Rectangle): first rectangle instance.
            rect_2 (Rectangle): second rectangle instance.

        Returns:
            Rectangle: rectangle instance with bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Creates a square instance of the rectangle class.

        Args:
            size (int): size of each side. Defaults to 0.

        Returns:
            Rectangle: new Rectangle instance.
        """
        return cls(size, size)
