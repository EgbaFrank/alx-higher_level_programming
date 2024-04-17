#!/usr/bin/python3
"""
This module contains a pascal triangle function
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle of size n

    Args:
        n (int): size of triangle
    """
    trig = []
    for i in range(n):
        val = [1]
        if i > 0:
            for j in range(1, i):
                value = trig[i - 1][j - 1] + trig[i - 1][j]
                val.append(value)
            val.append(1)
        trig.append(val)
    return trig
