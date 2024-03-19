#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num = len(my_list)
    if idx >= num:
        return my_list
    elif idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
