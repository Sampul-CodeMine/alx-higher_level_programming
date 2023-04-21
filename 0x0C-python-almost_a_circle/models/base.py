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

    @classmethod
    def create(cls, **dictionary):
        """A class method that returns a class instantied from a dictionary
        of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def load_from_file(cls):
        """A Class method that returns a list of classes instantiated from a
        file of JSON strings. It reads from `<cls.__name__>.json`.

        Returns:
            Empty list if file not found else, a list of instantiated classes.
        """
        fn = str("{}.json".format(cls.__name__))
        try:
            with open(fn, "r") as jf:
                list_dicts = Base.from_json_string(jf.read())
                return [cls.create(**dictnry) for dictnry in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that writes the CSV serialization of a list of objects
        to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fn = "{}.csv".format(cls.__name__)
        with open(fn, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvf, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A Class method that returns a list of classes instantiated from a
        CSV file. Reads from `<cls.__name__>.csv`.

        Returns:
            Empty list if file not found else, a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvf, fieldnames=fields)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
