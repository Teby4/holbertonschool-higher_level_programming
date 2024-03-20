#!/usr/bin/python3
"""
task 8.
"""

import json


def class_to_json(obj):
    """return obj in dict form"""
    return obj.__dict__
