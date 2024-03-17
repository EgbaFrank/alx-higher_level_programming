#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 1

        for i in row:
            if count < 3:
                print("{} ".format(i), end='')
            else:
                print("{}".format(i), end='')
            count += 1
        print()
