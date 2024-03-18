#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    # Return None if list is empty
    if not my_list:
        return None

    # return new list with True if even or otherwise False
    # values based on original list element position
    return [True if i % 2 == 0 else False for i in my_list]
