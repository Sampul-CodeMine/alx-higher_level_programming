#!/usr/bin/python3
"""A function to say my name"""


def say_my_name(first_name: str, last_name=""):
    """This is a function that accepts the firstname and lastname
    of a user and print out the name.
    First name must not be empty and must be a string likewise the lastname
    Args:
        first_name: The first name of the user (str)
        last_name: The last name of the user (str)
    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "" or first_name is None:
        raise ValueError("first_name is required")

    print("My name is {} {}".format(first_name, last_name))
