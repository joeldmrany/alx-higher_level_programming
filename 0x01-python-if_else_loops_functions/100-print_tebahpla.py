#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        letter = chr(i)
    else:
        letter = chr(i-32)
    print("{}".format(letter), end='')
