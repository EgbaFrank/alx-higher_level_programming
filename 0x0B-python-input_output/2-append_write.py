#!/usr/bin/python3
"""
This module contain a write_file functionality
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file in UTF8 encoding

    Args:
        filename (str): file to be written in
        text (str): what to be written

    Returns:
        int: the number of characters
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
