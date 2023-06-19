#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """_summary_  : a function that deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): dictionary to search for value key to be deleted from
        value (string): value of keys to be deleted
    """
    key_to_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_to_del.append(key)
    for key in key_to_del:
        del a_dictionary[key]
    return a_dictionary

