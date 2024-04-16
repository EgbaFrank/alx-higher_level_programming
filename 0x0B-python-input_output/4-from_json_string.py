#!/usr/bin/python3
"""
This contains a JSON conversion functionality
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): string to be converted

    Returns:
        Python data structures: python object represented by a JSON string
    """
    return json.loads(my_str)
