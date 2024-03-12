#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if (i != 8) or (x != 9):
            if (i != x) and (i < x):
                print("{}{}".format(i, x), end=", ")
        else:
            print("{}{}".format(i, x))
