#!/usr/bin/python3
"""
task 8
"""


class BaseGeometry():
    """
    BaseGeometry Class
    """
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integrer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class rectangle
    """

    def __init__(self, width, height):
        """
        Init
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
