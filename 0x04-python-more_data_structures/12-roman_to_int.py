#!/usr/bin/python3
'''
    Goal
    - a function that converts Roman Numerals to an integer
    
    Algorithm
    - Create a Dictionary of the core roman numeral figures and link {R_dict}
      their keys (Roman numeral) to values (the corresponding integer)
    - split input string into single characters
    - store individual characters in a list [chr_list]
    - create a variable for the storing the result integer(final_int)
    - loop tru the list, assigning a as index for R_dict (R_dict[a]) and incrementing final_int 
    - return final_int
'''
from functools import reduce
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
            if final_int < R_dict[chr]:
                final_int = final_int + R_dict[chr]
            else:
                final_int -= R_dict[chr]

    return final_int
