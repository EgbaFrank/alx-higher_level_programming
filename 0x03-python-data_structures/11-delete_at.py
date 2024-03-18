#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Return list if index is out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete at index
    del my_list[idx]

    # Return modified list
    return my_list
