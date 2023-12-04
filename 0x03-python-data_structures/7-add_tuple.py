#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if (((len(tuple_a)) == 2 and (len(tuple_b)) == 2) or ((len(tuple_a) > 2) and (len(tuple_b) > 2))):
        a = int(tuple_a[0]) + int(tuple_b[0])
        b = int(tuple_a[1]) + int(tuple_b[1])
    elif ((len(tuple_a)) == 1) and (len(tuple_b) == 2):
        a = int(tuple_a[0]) + int(tuple_b[0])
        b = (0) + int(tuple_b[1])
    elif ((len(tuple_a)) == 2) and (len(tuple_b) == 1):
        a = int(tuple_a[0]) + int(tuple_b[0])
        b = int(tuple_a[1]) + (0)
    elif ((len(tuple_a)) == 0) and (len(tuple_b) == 2):
        a = (0) + int(tuple_b[0])
        b = (0) + int(tuple_b[1])
    elif ((len(tuple_a)) == 2) and (len(tuple_b) == 0):
        a = int(tuple_a[0]) + (0)
        b = int(tuple_a[1]) + (0)
    elif ((len(tuple_a)) == 1) and (len(tuple_b) == 0):
        a = int(tuple_a[0]) + (0)
        b = 0
    elif ((len(tuple_a)) == 0) and (len(tuple_b) == 1):
        a = (0) + int(tuple_b[0])
        b = (0)
    elif ((len(tuple_a)) == 0) and (len(tuple_b) == 0):
        a = 0
        b = 0
    tuple_c = (a, b)
    return tuple_c
