#!/usr/bin/python3
"""
Module: 2-square
Return: Defines a square.
"""


class Square:
    """this is a class representation of a square"""
    def __init__(self, size=0):
        """Initializes an instance of a square

        Args:
            self (string): self argument
            size (int, optional): _description_. Defaults to 0.
        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
