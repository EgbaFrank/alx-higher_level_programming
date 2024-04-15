#!/usr/bin/python3
"""
This module contains a Mylist Class

Classes:
    MyList (list): inherits the list class providing similar functionalities
"""


class MyList(list):
    """
    Defines a list class
    """
    def __init__(self):
        """
        Initializes a MyList object
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
