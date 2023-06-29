#!/usr/bin/python3
""" Module: 3-square
class square that defines a square.
"""


class Square:
    """This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size(int): the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns area of the square.

        Returns:
            int: the area of the square.
        """
        return (self.__size ** 2)
