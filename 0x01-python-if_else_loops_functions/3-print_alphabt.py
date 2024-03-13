#!/usr/bin/python3

for letter in range(97, 123):
    if letter == ord('e') or letter == ord('q'):
        continue
    print("{}".format(chr(letter)), end='')
