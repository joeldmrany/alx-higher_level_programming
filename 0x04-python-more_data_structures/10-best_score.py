#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return (None)
    k = None
    v = float('-inf')
    for key, value in a_dictionary.items():
        if (value > v):
            v = value
            k = key
    return (k)
