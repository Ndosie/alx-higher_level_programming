#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0

    if roman_string is None or roman_string.isdigit():
        return 0

    while i < len(roman_string):
        if i + 1 < len(roman_string):
            if romans[roman_string[i]] < romans[roman_string[i+1]]:
                result += romans[roman_string[i + 1]] - romans[roman_string[i]]
                i += 2
                continue

        result += romans[roman_string[i]]
        i += 1

    return result
