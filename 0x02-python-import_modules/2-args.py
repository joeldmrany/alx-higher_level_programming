#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if (num == 1):
        print("0 arguments.")
    elif (num == 2):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments".format(num - 1))
        for i in range(1, num):
            print("{}: {}".format(i, argv[i]))
