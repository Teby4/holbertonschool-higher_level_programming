#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """ square class """

    def __init__(self, size=0):
        """ init square """
        self.__size = size

    @property
    def size(self):
        """ returns size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ set square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area of square """
        return (self.__size * self.__size)

    def my_print(self):
        """ print square in # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
