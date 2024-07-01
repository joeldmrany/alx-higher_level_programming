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
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not position[0] or not position[1]):
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
            for s in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for s in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def area(self):
        """ function to calculate area of square """
        return (self.__size * self.__size)
