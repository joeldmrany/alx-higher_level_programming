#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num = len(my_list)
    if idx >= num:
        return None
    elif idx < 0:
        return None
    else:
        my_list[idx] = element
        return(my_list)
