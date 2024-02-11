#!/usr/bin/python3
"""
task 0
"""


def read_file(filename=""):
    """
    read and print file
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
