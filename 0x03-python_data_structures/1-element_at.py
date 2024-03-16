#!/usr/bin/python3
def element_at(my_list, idx):
    num = len(my_list)
    if idx > num:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
