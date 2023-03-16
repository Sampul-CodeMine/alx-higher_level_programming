#!/usr/bin/python3

"""Function to convert a roman_numeral into integer equivalent

    Args:
        roman_string: the roman numeral to convert to integer equivalent

    Returns:
        Returns 0 if string is None or not a string else integer equivalent
    """


def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string is not None:
        roman_symbol = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        int_equiv = 0
        for num in range(len(roman_string)):
            if num > 0 and roman_symbol[roman_string[num]] > \
              roman_symbol[roman_string[num - 1]]:
                int_equiv += roman_symbol[roman_string[num]] - 2 * \
                        roman_symbol[roman_string[num - 1]]
            else:
                int_equiv += roman_symbol[roman_string[num]]
        return (int_equiv)

    return (0)
