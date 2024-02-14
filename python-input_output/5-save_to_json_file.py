#!/usr/bin/python3
"""
task 0
"""

import json


def save_to_json_file(my_obj, filename):
    """
    read and print file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
