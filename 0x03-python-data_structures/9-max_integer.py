#!/usr/bin/python3
def max_integer(my_list=[]):
    maxx = my_list[0]
    if not my_list:
        return None
    else:
        for i in range(len(my_list)):
            if maxx < my_list[i]:
                maxx = my_list[i]
            else:
                pass
        return maxx
