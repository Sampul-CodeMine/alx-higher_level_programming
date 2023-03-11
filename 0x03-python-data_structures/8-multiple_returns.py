#!/usr/bin/python3

def multiple_returns(sentence):
    """Function to returns a tuple with the length of a string and
    its first character

    Args:
        sentence: string passed to check its length and first letter

    Returns:
        Returns tuple with length and first char of sentence
    """
    sentence_temp_tup = ()
    if len(sentence) == 0:
        sentence_temp_tup = 0, "None"
    else:
        sentence_temp_tup = len(sentence), sentence[0]
    return sentence_temp_tup
