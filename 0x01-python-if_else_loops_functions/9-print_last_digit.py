#!/usr/bin/python3
def print_last_digit(number):
    if number is < 0:
        lastDigit = number % -10
        print(-(lastDigit), end='')
    else:
        lastDigit = number % 10
        print(lastDigit, end='')
    return abs(lastDigit)
