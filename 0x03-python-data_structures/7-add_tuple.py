#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    int a = []
    for i in range(2):
        if (not tuple_a[i]):
            tuple_a[i] = 0
        elif (not tuple_b[i]):
            tuple_b[i] = 0
        a[i] = int(tuple_a[i]) + int(tuple_b[i])
    tuple_c = (a[0], a[1])
    return tuple_c
