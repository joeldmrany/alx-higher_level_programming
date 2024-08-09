#!/usr/bin/python3
"""
function to write in file
"""


def write_file(filename="", text=""):
    """ the function """
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
        return (len(text))
