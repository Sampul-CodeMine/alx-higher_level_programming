#!/usr/bin/python3
"""This Defines the `Rectangle` Class for the Project
The `Rectangle` class is a subclass to the `Base` class
"""

from models.base import Base


class Rectangle(Base):
    """This is a class that represents a Rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a new Rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def set_validation(attrib, value: int):
        """Class static method that validates a value for its data type
        and its value else raisesan exception"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attrib))
        if attrib == "x" or attrib == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attrib))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attrib))

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinates of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinates of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinates of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("y", value)
        self.__y = value

    def area(self):
        """A Class method that finds the area of the Rectangle object
        Returns:
            int: product of `width` and `height`
        """
        return self.__width * self.__height

    def display(self):
        """A class module that prints out the shape of a Rectangle object
        using the specified width, height, x and y coordinates"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for for_y in range(self.y):
            print("")
        for h_tag in range(self.height):
            [print(" ", end="") for for_x in range(self.x)]
            [print("#", end="") for w_tag in range(self.width)]
            print("")

    def __str__(self):
        """A class module overwriting the class __magic method __str__"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def _update__old(self, *args):
        """This is a public class method that updates all class attributes
        of the Rectangle object
        Args:
            *args (int): list of new attributes to update the class attribs.
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def update(self, *args, **kwargs):
        """This is a public class method that updates all class attributes
        of the Rectangle object
        Args:
            *args (int): list of new attributes to update the class attribs.
            **kwargs (dict): dictionary containing key/value for class attrib.
        """
        if args and len(args) != 0:
            count = 0
            for a in args:
                if count == 0:
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif count == 1:
                    self.width = a
                elif count == 2:
                    self.height = a
                elif count == 3:
                    self.x = a
                elif count == 4:
                    self.y = a
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                else:
                    self.__setattr__(key, val)

    def to_dictionary(self):
        """Class method to print a dictionary of all class attributes."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
