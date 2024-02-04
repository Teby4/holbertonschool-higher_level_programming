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
        initialice square instance
        """
        if isinstance(size, int) and size > 0:
            self.__size = size 
        
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
