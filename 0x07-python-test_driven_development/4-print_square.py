#!/usr/bin/python3
"""
This module contains a ``print_square`` function
"""


def print_square(size):
    """
    ``print_square`` prints a square of specified size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print('\n'.join(['#' * size] * size), end='')
