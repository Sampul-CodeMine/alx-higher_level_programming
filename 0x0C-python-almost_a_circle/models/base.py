#!/usr/bin/python3
import json
import csv
import turtle
"""This Defines the `Base` Class for the Project"""
"""importing the builtin JSON, csv, and turtle libraries"""


class Base:
    """This is a Class that represents the Base Class (Parent Class)
    Private Class attribute:
        __nb_objects (int): manages the id of the Subclasses in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Object initialization for a new Base object
        Args:
            id (int): New Base class object identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A class static method to stringify a list of dictionary into JSON
        Args:
            list_dictionaries (list): a list of dictionaries
        Return:
            A JSON string of python list object
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
