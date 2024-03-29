#!/usr/bin/python3
"""
    Base
"""

import json


class Base:
    """
    base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_objs))