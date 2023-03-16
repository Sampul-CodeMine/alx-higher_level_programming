#!/usr/bin/python3

"""Function to return a key with the biggest value

    Args:
        a_dictionary: the specified dictionary

    Returns:
        Returns a key with the biggest value
    """


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    max_data = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v is max_data:
            return k
