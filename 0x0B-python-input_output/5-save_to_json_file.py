#!/usr/bin/python3
"""
Contains JSON functionality
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be written
        filename: file to be written to
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
