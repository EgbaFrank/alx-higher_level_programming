#!/usr/bin/python3
"""
This module contains utilities for objects and classes
"""


def inherits_from(obj, a_class):
    """
    Checks if an instance is a subclass of a specified class

    Args:
        obj: object to be checked. Instance of any type
        a_class: class to be checked against

    Returns:
        Bool: True if obj is an instance of a subclass a_class, False otherwise
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
