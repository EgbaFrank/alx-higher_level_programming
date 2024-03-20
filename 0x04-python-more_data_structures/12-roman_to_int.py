#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prv = 0
    intgr = 0

    for i in roman_string:
        cur = roman[i]

        if cur > prv:
            intgr += cur - 2 * prv

        else:
            intgr += cur

        prv = cur

    return intgr
