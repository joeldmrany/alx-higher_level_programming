#!/usr/bin/python3
"""
That is a function to divide matrix by number
Try
Don't forget your feedback
"""
def matrix_divided(matrix, div):
    """
    that is matrix_divided function
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(item/div, 2) for item in row]for row in matrix]
    return new_matrix
