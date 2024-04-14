#!usr/bin/python3
"""
This module contains a matrix divide function
"""


def matrix_divided(matrix, div):
    """ This function divides each element

    Args:
        matrix (list of list): matrix to be divided
        div (int, float): what element would be divided by

    Returns:
        list of list: A new matrix

    Raises:
        TypeError: if matrix is not a list of list or
                   elements are not integers or floats
        TypeError: if div is not an integer or float
        TypeError: if each matrix row is not of same size
        ZeroDivisionError: if div is equal to zero
    """
    flag = 0
    if not isinstance(matrix, list):
        flag = 1
    elif not all(isinstance(sublist, list) for sublist in matrix):
        flag = 1
    elif not all(isinstance(i, (int, float)) for sub in matrix for i in sub):
        flag = 1
    if flag == 1:
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(value/div, 2) for value in row] for row in matrix]
