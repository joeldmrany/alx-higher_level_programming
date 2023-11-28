#!/usr/bin/python3
for i in range(0, 9):
    for a in range(i + 1, 10):
        if i == 8 and a == 9:
            print("89")
            break
        print("{:02d}, ".format((i * 10) + a), end="")
