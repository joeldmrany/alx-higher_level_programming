#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    col = len(matrix[0])
    for i in range(rows):
        for x in range(col):
            print("{:d}".format(matrix[i][x]), end='')
            if x < col-1:
                print("", end=' ')
        print("")
