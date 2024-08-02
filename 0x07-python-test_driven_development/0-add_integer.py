#!/usr/bin/python3
"""
it is a function to add 2 integers
it's name is "add_integer"
a and b must be integers or floats
"""


def add_integer(a, b=98):
    """
    add_integer function is a function to add integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(a)
    result = a + b
    return result
