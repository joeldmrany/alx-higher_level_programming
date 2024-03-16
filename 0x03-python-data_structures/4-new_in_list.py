#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    num = len(my_list)
    if idx >= num:
        return new_list
    elif idx < 0:
        return new_list
    else:
        new_list[idx] = element
        return new_list
