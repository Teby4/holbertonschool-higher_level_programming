#!/usr/bin/python3
"""
    rectangle class exercises
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initialize
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """
        height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def _str_(self):
        """str function"""
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            for x in range(self.width):
                rectangle += "#"
            rectangle += "\n"
        return rectangle
    
    def _repr_(self):
        return "Rectangle({} {})".format(self.height, self.width)

    def _del_(self):
        print("Bye rectangle...")