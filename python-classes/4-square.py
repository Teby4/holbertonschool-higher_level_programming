#!/usr/bin/python3
"""
    Write a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    square class
    """
    
    def __init__(self, size=0):
        """
        init square
        """
        self.__size = size

    def size(self):
        """
        returns size of square
        """
        return self.__size
    
    def __init__(self, size=0):
        """
        initialice square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area of square
        """
        return (self.__size * self.__size)
