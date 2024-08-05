#!/usr/bin/python3
"""
checker
"""


def inherits_from(obj, a_class):
    """ check of obj is inherits from a_class """
    return isinstance(obj, a_class) and type(obj) is not a_class
