#!/usr/bin/python3
"""
This module contains JSON functionality
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename (str): file to be read from
    """
    with open(filename, encoding='utf-8') as file:
        if file.read().strip() == '':
            return []
        else:
            file.seek(0)
            return json.load(file)
