#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for x in range(len(matrix)):
            new[i][x] = ((new[i][x])**2)
    return new
