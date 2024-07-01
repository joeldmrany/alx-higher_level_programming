#!/usr/bin/python3
""" define Square class """


class Square:
    """ that is empty class which is named by Square """
    def __init__(self, size=0, position=(0, 0)):
        """ it takes arg size """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """ Retrives the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets square size """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for n in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        """ function to calculate area of square """
        return (self.__size * self.__size)
