#!/usr/bin/python3

def remove_char_at(str, n):
    count = 0
    new = ''

    for i in str:
        if count != n:
            new += i
        count += 1
    return new
