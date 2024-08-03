#!/usr/bin/python3
"""
not empty class
"""


class Rectangle:
    """
    not empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            str_ch = str(self.print_symbol)
            for i in range(self.__height):
                for j in range(self.__width):
                    strr += str_ch
                if i < (self.__height - 1):
                    strr += "\n"
        return strr

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        area_1 = rect_1.__width * rect_1.__height
        area_2 = rect_2.__width * rect_2.__height
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (area_2 > area_1):
            return rect_2
        else:
            return rect_1
