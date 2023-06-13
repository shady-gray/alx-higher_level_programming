#!/usr/bin/env python3
def no_c(my_string):
    str_list = [*my_string]
    newstring_list = []
    for a in str_list:
        if a == 'c' or a == 'C':
            continue
        else:
            newstring_list.append(a)
    new_str = ''.join(newstring_list)
    return new_str
