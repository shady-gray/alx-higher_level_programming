#!/usr/bin/python3
for i in range(0, 10):
	for j in range(0, 10):
		print("{}{}, ".format(i, j), end='')
		if i == 9 and j == 9:
			print("{}{}\n".format(i, j))
