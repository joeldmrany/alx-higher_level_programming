#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    a = len(arg)
    print("{} argument:".format(a - 1))
    for i in range(len(arg)):
        if i == 0:
            continue
        print("{}: {}".format(i, arg[i]))
