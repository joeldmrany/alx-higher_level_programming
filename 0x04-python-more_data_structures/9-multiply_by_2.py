#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for key in b_dictionary:
        num = b_dictionary[key]
        b_dictionary[key] = num * 2
    return (b_dictionary)
