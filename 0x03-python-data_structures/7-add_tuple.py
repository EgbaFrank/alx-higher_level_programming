#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # calculate tuple lenght
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    
    # checks if tuple_b lenght is less than 2
    if a_len == 0:
        tuple_a = (0, 0)
    elif a_len == 1:
        tuple_a = (tuple_a[0], 0)

    # checks if tuple_b lenght is less than 2
    if b_len == 0:
        tuple_b = (0, 0)
    elif b_len == 1:
        tuple_b = (tuple_b[0], 0)

    # calculate and return result
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
