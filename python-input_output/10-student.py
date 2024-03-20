#!/usr/bin/python3
"""
task 8.
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        my_dict = {}

        if isinstance(attrs, list):
            for x in attrs:
                if not isinstance(x, str):
                    break
            else:
                for i in attrs:
                    my_dict[i] = getattr(self, i)
        else:
            my_dict = self.__dict__

        return my_dict
