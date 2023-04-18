#!/usr/bin/python3

import json
"""This Defines the `Base` Class for the Project"""
"""importing the builtin JSON library"""


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
        """A class method to stringify a list of dictionary into JSON"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class methid that writes a JSON string rep of a list object
        to a file.
        Args:
            cls (obj): a class instance
            list_objs (list): a list of inherited Base Instances
        """
        output = []
        fn = "{}.json".format(cls.__name__)
        result = "[]" if list_objs is None or len(list_objs) == 0\
            else [obj.to_dictionary() for obj in list_objs]

        with open(fn, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(result))

    def from_json_string(json_string):
        """"""
        ...
