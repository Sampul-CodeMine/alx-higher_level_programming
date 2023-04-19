#!/usr/bin/python3

import json
import csv
"""This Defines the `Base` Class for the Project"""
"""importing the builtin JSONand csv libraries"""


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
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes a JSON string rep of a list object
        to a file.
        Args:
            list_objs (list): a list of inherited Base Instances
        """
        fn = "{}.json".format(cls.__name__)
        with open(fn, mode="w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_obj = [obj.to_dictionary() for obj in list_objs]
                jf.write(Base.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """Class Static method that returns the decoded object of JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            Empty list If json_string is None or empty - an empty list.
            else - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
