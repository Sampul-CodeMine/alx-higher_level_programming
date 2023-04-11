# 0x0A. Python - Inheritance


## General

- Why Python programming is awesome
- What is a `superclass`, `baseclass` or `parentclass`
- What is a `subclass`
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be `executable`
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (`extension: .txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Inheritance in Python

One of the core concepts in OOP languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.

### Benefits of inheritance are: 

- It represents real-world relationships well.
- It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
- Inheritance offers a simple, understandable model structure. 
- Less development and maintenance expenses result from an inheritance. 

```python
# Base or Parent Class
class Animal(object):
    """Iniitialize the Animal class object"""
	def __init__(self, name, age):
	    self.name = name
		self.age = age
		
	def __str__(self):
	    return (f"<{self.__name}, {self.__age}>")
	
	def display(self):
	    print(f"Name: {self.__name}\nAge: {self.__age}")
		
		
		
# Child or SubClass
class Dog(Animal):
    """Iniitialize the Dog class object and inheriting from the Animal Class"""
	Animal.__init__(self)
	# this inherits in constructor or initializer of the Base or Parent class
		
	def __str__(self):
	    return (f"<{self.__name}, {self.__age}>")
	
	def print(self):
	    print(f"Name: {self.__name}\nAge: {self.__age}")
```

### Different types of Inheritance:

- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
- Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 