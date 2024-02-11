#!/usr/bin/python3
"""
task 0
"""


def append_write(filename="", text=""):
    """
    read and print file
    """
    with open(filename, "a", encoding="utf-8") as file:
        count = file.write(text)
    return count
