#!/usr/bin/python3
"""
that is print square function
Remember
Don't forget your feedback
"""


def print_square(size):
    """
    function to print square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            print("#", end="")
            j += 1
        print()
        i += 1
