#!/usr/bin/python3
"""
classes
"""


class BaseGeometry:
    """ class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class inherit from another
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """ Square class that inherits from Rectangle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
