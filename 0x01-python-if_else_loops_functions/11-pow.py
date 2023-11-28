#!/usr/bin/python3
def pow(a, b):
    d = a
    if b == 0:
        return 1
    elif b > 0:
        for i in range(1, b):
            if a < 0:
                if (b % 2) == 0:
                    c = d * a
                    d = c
                else:
                    c = d * a
                    d = c
            else:
                c = d * a
                d = c
        return c
    else:
        for i in range(b, -1):
            c = d * a
            d = c
        c = 1 / c
        return c
