#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_val = list(a_dictionary.keys())[0]

    for i in a_dictionary:
        if a_dictionary[i] > a_dictionary[max_val]:
            max_val = i
    return max_val
