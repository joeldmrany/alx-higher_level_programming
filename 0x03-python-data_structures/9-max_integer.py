#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        maxx = my_list[0]
        for i in range(len(my_list)):
            if maxx < my_list[i]:
                maxx = my_list[i]
            else:
                pass
        return maxx
