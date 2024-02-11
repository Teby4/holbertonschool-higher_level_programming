#!/usr/bin/python3
"""
task 7
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
