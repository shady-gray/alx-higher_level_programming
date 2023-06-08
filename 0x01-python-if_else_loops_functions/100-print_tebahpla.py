#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 == 0:
        step = 0
    else:
        step = 32
    print("{}".format(chr(a - step), end='')
