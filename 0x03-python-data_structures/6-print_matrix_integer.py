#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 1

        for i in row:
            if count < 3:
                print("{:d} ".format(i), end='')
            else:
                print("{:d}".format(i), end='')
            count += 1
        print()
