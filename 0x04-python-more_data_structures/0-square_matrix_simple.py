#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [list(map((lambda x: x**2), index)) for index in matrix]
    return square_matrix
