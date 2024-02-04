#!/usr/bin/python3
""" this file contains the  add_integrer function """


def add_integer(a, b=98):
    """ add the addition of two integrers """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
