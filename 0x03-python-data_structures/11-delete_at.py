def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        b = my_list[idx]
        my_list.remove(b)
        return my_list
