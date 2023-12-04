#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if (len(tuple_a)) == 2 and (len(tuple_b)) == 2:
        for i in range(len(tuple_a)):
            tuple_c(i) = int(tuple_a(i)) + int(tuple_b(i))
        return tuple_c
