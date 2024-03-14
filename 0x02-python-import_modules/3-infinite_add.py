#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    summ = 0
    if (num == 1):
        print("0")
    else:
        for i in range(1, num):
            summ += int(argv[i])
        print("{}".format(summ))
