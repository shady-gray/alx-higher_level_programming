#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_listCpy = my_list[0:len(my_list)]
    if idx < 0:
        return my_listCpy
    elif idx > len(my_list) - 1:
        return my_listCpy
    else:
        my_listCpy[idx] = element
        return my_listCpy
