#!/usr/bin/python3
"""
This module contains utilities on objects and classes
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj: object to be checked
        a_class: class to check against

    Returns:
        Bool: True if obj is a_class instance, false otherwise
    """
    return type(obj) is a_class
