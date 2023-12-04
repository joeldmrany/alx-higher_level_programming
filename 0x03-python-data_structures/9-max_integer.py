#!/usr/bin/python3
def max_integer(my_list=[]):
    b = my_list[0]
    for i in range(len(my_list) - 1):
        if (not my_list):
            return None
        else:
            if b <= my_list[i]:
                b = my_list[i]
    return b
