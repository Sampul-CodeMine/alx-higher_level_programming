#!/usr/bin/python3
"""Function that performs text indentation when the characters '.', '?',
and ':' are encountered"""


def text_indentation(text: str):
    """Function to indent text when the `.`, `?`, `:` characters are encountered.
    When these characters are encountered, it shift the text 2 new lines below
    Args:
        text: The stream of text datatype to indent (str)
    Raises:
        TypeError: when text is not of string datatype "text must be a string"
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) == 0:
        print("")

    count = 0
    str_len = len(text)

    while count < str_len and text[count] == ' ':
        count += 1

    while count < str_len:
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < str_len and text[count] == ' ':
                count += 1
            continue
        count += 1
