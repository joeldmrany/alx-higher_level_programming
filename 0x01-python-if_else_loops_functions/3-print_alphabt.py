#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e':
        continue
    elif chr(i) == 'q':
        continue
    print("{}".format(chr(i)), end="")
