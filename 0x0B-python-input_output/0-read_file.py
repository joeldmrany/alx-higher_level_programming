#!/usr/bin/python3
"""
function to read file content
"""


def read_file(filename=""):
    """ that is the function """
    with open(filename, "r", encoding="UTF-8") as f:
        print (f.read(), end="")
