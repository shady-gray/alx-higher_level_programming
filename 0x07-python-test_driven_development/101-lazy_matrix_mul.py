#!/usr/bin/python3

"""This module contains a function that multiplies two matrices"""

import numpy as nump


def lazy_matrix_mul(matrix_1, matrix_2):
    """Return the multiplication of two matrices.
    Args:
        matrix_1 (list of lists of ints/floats): The first matrix.
        matrix_2
    
 (list of lists of ints/floats): The second matrix.
    """

    return (nump.matmul(matrix_1, matrix_2
))
