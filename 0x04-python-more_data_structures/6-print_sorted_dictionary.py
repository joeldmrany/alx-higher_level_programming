#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortes = dict(sorted(a_dictionary.items()))
    for key, value in sortes.items():
        print(f"{key}: {value}")
