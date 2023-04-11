#!/usr/bin/python3
"""Class to represent a List Object"""

class MyList(list):
    """This is a class that inherits from the list class.
    Args:
        list (list)
    Return:
        None
    """
    def print_sorted(self):
        """method to print the sorted list"""
        
        print(sorted(self))
