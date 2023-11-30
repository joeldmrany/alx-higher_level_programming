#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    a = 0
    if len(arg) == 1:
        print("0")
    else:
        for i in range(1, len(arg)):
            a += int(arg[i])
        print("{}".format(a))
