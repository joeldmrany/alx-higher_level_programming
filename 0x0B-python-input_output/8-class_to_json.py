#!/usr/bin/python3
""" JSON """


def class_to_json(obj):
    """ function class to json """
    dictt = {}
    if hasattr(obj, "__dict__"):
        dictt = obj.__dict__.copy()
    return dictt
