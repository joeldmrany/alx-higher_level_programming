#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]
    for i in range(2):
        if not a[i]:
            a[i] = 0
        if not b[i]:
            b[i] = 0
    tuple_c = (a[0] + b[0], a[1] + b[1])
    return tuple_c
