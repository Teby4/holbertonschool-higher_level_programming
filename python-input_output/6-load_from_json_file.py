#!/usr/bin/python3
"""
task 0
"""

import json


def load_from_json_file(filename):
    """
    read and print file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
