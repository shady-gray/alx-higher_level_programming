#!/usr/bin/python3
def no_c(my_string):
    str_list = [*my_string]
    new_list = []
    for a in str_list:
        if a == 'c' or a == 'C':
            continue
        else:
            new_list.append(a)
    new_str = ''.join(new_list)
    return new_str
