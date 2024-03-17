#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]
    if not (a[0]):
        a.append(0)
    if not (a[1]):
        a[1] = 0
    if not (b[0]):
        b[0] = 0
    if not (b[1]):
        b.append(0)
    tuple_c = (a[0] + b[0]), (a[1] + b[1])
    return tuple_c
