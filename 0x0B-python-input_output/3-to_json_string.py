#!/usr/bin/python3
"""
This module contains a JSON serialization functionality
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object

    Args:
        my_obj (str): string to be converted

    Returns:
        str: json representations of the object
    """
    return json.dumps(my_obj)
