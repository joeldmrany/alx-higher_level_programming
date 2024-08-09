#!/usr/bin/python3
"""
function to append to a file
"""


def append_write(filename="", text=""):
    """ the function """
    with open(filename, 'a', encoding="UTF-8") as f:
        f.write(text)
        return (len(text))
