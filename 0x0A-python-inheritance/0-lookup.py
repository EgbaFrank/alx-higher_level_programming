#!/usr/bin/python3
"""
This module contains a function ``lookup``
which returns the attributes and methods defines in an object
"""


def lookup(obj):
    """
    Returns a list of methods and attributes
    contained in an object

    Args:
        obj (*): object to be applied on

    Returns:
        list: attributes and methods obj contains
    """
    return dir(obj)
