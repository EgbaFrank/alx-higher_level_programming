#!/usr/bin/python3
"""
This module contains a read file functionality
"""


def read_file(filename=""):
    """
     reads a text file in utf-8 encoding and prints it to stdout

     Args:
        filename (str): Name of the file to be read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
