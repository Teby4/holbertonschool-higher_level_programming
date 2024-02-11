#!/usr/bin/python3
"""
task 3
"""


def is_same_class(obj, a_class):
    """
    check for obj instanse of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
