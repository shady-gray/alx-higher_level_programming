#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for a in my_list:
        if a == search:
            my_list[my_list.index(a)] = replace
