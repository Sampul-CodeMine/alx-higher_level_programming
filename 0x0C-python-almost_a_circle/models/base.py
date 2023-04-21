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
        if type(list_dictionaries) == list:
            if list_dictionaries is None:
                return "[]"
            return json.dumps(list_dictionaries)
        else:
            ...

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
