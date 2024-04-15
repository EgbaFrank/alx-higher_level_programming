#!/usr/bin/python3
"""
This module provides utilities on objects and class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an obj is an instance
    or a "subinstance" of a specified class
    """
    return issubclass(obj.__class__, a_class) or isinstance(obj, a_class)
