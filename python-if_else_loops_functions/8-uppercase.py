#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            result += chr(char_code - 32)
        else:
            result += char
    print('{}'.format(result))
