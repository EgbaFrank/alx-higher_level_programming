#!/usr/bin/python3

def max_integer(my_list=[]):
    # Return None if list is empty
    if not my_list:
        return None

    # Calculate and return largest number in list
    lrgt = my_list[0]

    for i in my_list[1:]:
        if i > lrgt:
            lrgt = i

    return lrgt
