#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev_value = 0

    for char in roman_string:
        current_value = romandict[char]

        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

        prev_value = current_value

    return result
