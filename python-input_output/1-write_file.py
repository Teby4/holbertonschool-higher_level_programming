#!/usr/bin/python3
"""
task 0
"""


def write_file(filename="", text=""):
    """
    read and print file
    """
    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
    return count
