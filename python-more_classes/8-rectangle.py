#!/usr/bin/python3
"""
Module with Class Rectangle
"""


class Rectangle:
    """Initialization Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Method: Rectangle object
        Args: Width and height
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """setter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter width"""
        if not isinstance(value, int):
            raise (TypeError("width must be an integer"))
        if value < 0:
            raise (ValueError("width must be >= 0"))
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if not isinstance(value, int):
            raise (TypeError("height must be an integer"))
        if value < 0:
            raise (ValueError("height must be >= 0"))
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle
        based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise (TypeError("rect_1 must be an \
instance of Rectangle"))
        if not isinstance(rect_2, Rectangle):
            raise (TypeError("rect_2 must be an \
instance of Rectangle"))

        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1 == rect_2:
            return rect_1

    def area(self):
        """return area for a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print square fo rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        square = "\n".join(
            [str(self.print_symbol) * self.__width
             for squre in range(self.__height)])
        return square

    def __repr__(self):
        """return string representation
        of the rectangle
        """
        Cls = self.__class__.__name__
        return "{}({}, {})".format(Cls, self.width, self.height)

    def __del__(self):
        """print message where rectangle
        is delete"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
