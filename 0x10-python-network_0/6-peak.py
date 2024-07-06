#!/usr/bin/python3
"""
Implements finding a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    if n == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if ((mid == 0 or
                list_of_integers[mid] >= list_of_integers[mid - 1]) and
            (mid == n - 1 or
                list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]

        elif ((mid > 0) and
                (list_of_integers[mid] < list_of_integers[mid - 1])):
            right = mid - 1

        else:
            left = mid + 1

    return None
