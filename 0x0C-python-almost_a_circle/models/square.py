#!/usr/bin/python3
"""This Defines the `Square` Class for the Project
The `Square` class is a subclass to the `Rectangle` class which
inturn is a Subclass to the `Base` class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class that represents a Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a new Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size (width and height) of the Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """A class module overwriting the class __magic method __str__"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """This is a public class method that updates all class attributes
        of the Square object
        Args:
            *args (int): list of new attributes to update the class attribs.
            **kwargs (dict): dictionary containing key/value for class attrib.
        """
        if args and len(args) != 0:
            count = 0
            for a in args:
                if count == 0:
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif count == 1:
                    self.size = a
                elif count == 2:
                    self.x = a
                elif count == 3:
                    self.y = a
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                else:
                    self.__setattr__(key, val)
