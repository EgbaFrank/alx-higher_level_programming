#!/usr/bin/python3
"""
This module prints contains a say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """ 
    ``say_my_name()`` prints the name inputted.
        
    Args:
        first_name (str): first name of the individual.
        last_name (str): last name of the individual. Defaults to an empty string.

    Raises:
        TypeError: if first_name is not a string.
        TypeError: if last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
