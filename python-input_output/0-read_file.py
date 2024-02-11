#!/usr/bin/python3
"""
task 0
"""
def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end="")
