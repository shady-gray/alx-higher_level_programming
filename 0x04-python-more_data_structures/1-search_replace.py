#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list.copy()
    for a in range(0, len(list_copy)):
        if list_copy[a] == search:
            list_copy[a] = replace
        else:
            continue
    return list_copy
