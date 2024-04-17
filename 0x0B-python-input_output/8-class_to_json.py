#!/usr/bin/python3
"""
This module contains JSON funtionality
"""


def class_to_json(obj):
    """
    Returns the dictionary description for an object JSON serialization

    Args:
        obj: object to be applied on

    Returns:
        dict: description JSON serialization with simple data structures
    """
    return obj.__dict__
