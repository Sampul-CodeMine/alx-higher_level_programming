#!/usr/bin/python3
"""This Defines the `Base` Class for the Project"""


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
