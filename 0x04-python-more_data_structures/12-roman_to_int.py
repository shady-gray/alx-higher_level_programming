#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) != str:
        return 0
    else:
        R_dict = {
                "M": 1000,
                "D": 500,
                "C": 100,
                "L": 50,
                "X": 10,
                "V": 5,
                "I": 1
                }
        final_int = 0
        n = list(R_dict[a] for a in roman_string)
        for i in range(0, len(n) - 1):
            if n[i] < n[i + 1]:
                n[i] = -n[i]
            else:
                continue
        for item in n:
            final_int += item

    return final_int
