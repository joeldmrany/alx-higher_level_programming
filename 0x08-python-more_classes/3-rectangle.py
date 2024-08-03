#!/usr/bin/python3
"""
not empty class
"""


class Rectangle:
    """
    not empty class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            result = 0
        else:
            result = 2 * (self.__width + self.__height)
        return result

    def __str__(self):
        strr = ""
        if self.__width == 0 or self.__height == 0:
            pass
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    strr += "#"
                if i < (self.__height - 1):
                    strr += "\n"
        return strr
