#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    a = len(arg)
    if len(arg) == 1:
        print("0 arguments.")
    elif len(arg) == 2:
        print("1 argument:")
    else:
        print("{} argument:".format(a - 1))
    for i in range(len(arg)):
        if i == 0:
            continue
        print("{}: {}".format(i, arg[i]))
