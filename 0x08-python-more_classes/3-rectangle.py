#!/usr/bin/python3
"""
Module:3-rectangle
empty class that defines a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle by its width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.
        Args:
            width (int): the width of a rectangle.
            height (int): the height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method fof width attribute.
        Returns:
            int: width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        Args:
            value (int): the width value to set.
        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is negative or zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle represented as a string of '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
