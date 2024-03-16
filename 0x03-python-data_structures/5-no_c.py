#!/usr/bin/python3
def no_c(my_string):
    strings = ''
    for char in my_string:
        if (char != 'c') and (char != 'C'):
            strings += char
    return strings
