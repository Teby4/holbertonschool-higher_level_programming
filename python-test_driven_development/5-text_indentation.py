#!/usr/bin/python3
"""
this file contains the  add_integrer function
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':' characters.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev_char = ""
    for char in text:
        if char in ['.', '?', ':']:
            print(char, end='\n\n')
            prev_char = char
        elif prev_char in ['.', '?', ':'] and char == ' ':
            continue
        else:
            print(char, end='')
            prev_char = char

    if prev_char in ['.', '?', ':']:
        print()