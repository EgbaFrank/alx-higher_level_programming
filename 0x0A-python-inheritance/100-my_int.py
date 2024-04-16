#!/usr/bin/python3
"""
This module contains an MyInt class
"""


class MyInt(int):
    """
    Provides same ``int`` functionalities
    but inverts equal and not equal
    """
    def __eq__(self, other):
        """
        Inverting it's equality
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverting it's inequality
        """
        return super().__eq__(other)
