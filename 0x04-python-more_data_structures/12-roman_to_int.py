#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    elif type(roman_string) != str:
        return 0
    else:
        R_dict ={"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        final_int = 0
        chr_list = list(roman_string)
        for chr in reversed(chr_list):
            if final_int > R_dict[chr]:
                final_int -= R_dict[chr]
            else:
                final_int = final_int + R_dict[chr]

    return final_int
