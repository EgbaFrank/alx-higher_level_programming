#!/usr/bin/python3
"""
This module contains an add_integer function
"""


def add_integer(a, b=98):
    """ Adds two integers or floats

    Args:
        a (int, float): The first number
        b (int, float): The second number. Defaults to 98

    Returns:
        int: result of adding two numbers

    Raises:
        TypeError: if either 'a' or 'b' is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a + b
