# 0x06. Python - Classes and Objects

OOP is a totally new concept for all of us [especially those who think they know about it :)].

## General

- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## More Info

Documentation is now mandatory! Each module, class, and method must contain docstring as comments.

## Object Oriented Programming

In all the programs we wrote till now, we have designed our program around functions i.e. blocks of statements which manipulate data. This is called the procedure-oriented way of programming. There is another way of organizing your program which is to combine data and functionality and wrap it inside something called an object. This is called the object oriented programming paradigm. Most of the time you can use procedural programming, but when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. 

Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.

A class is created using the class keyword. The fields and methods of the class are listed in an indented block.

We will learn to know the four major principles of object-orientation and the way Python deals with them in the next section of this tutorial on object-oriented programming:

- Encapsulation
- Data Abstraction
- Polymorphism
- Inheritance

