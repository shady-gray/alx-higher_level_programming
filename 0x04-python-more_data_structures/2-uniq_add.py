#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    unique_list = list(set(my_list))
    for a in range(0, len(unique_list)):
        sum_list = sum_list + int(unique_list[a])
    return sum_list
