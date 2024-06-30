#!/usr/bin/python3
""" define Square class """


class Square:
    """ that is empty class which is named by Square """
    def __init__(self, size=0):
        """ it takes arg size """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
