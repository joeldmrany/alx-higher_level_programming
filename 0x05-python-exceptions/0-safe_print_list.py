#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for l in range(x):
        try:
            print("{}".format(my_list[l]), end='')
            num += 1
        except IndexError:
            break
    print()
    return (num)
