#!/usr/bin/python3
"""
This module contains an ``add_attribute`` function
"""


def add_attribute(obj, attr, value):
    """
    adds an attribute to an object

    Args:
        obj: object to be applied on
        attr: attribute to be added
        value: value of attribute to be added

    Raises:
        TypeError: if object is immutable \
                that is, attribute cannot be added
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
