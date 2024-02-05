#!/usr/bin/python3
"""
this file contains the  print square function
"""


def print_square(size):
    """
    print the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
