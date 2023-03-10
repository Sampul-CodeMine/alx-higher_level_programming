# Python - Data Structure

## General

- Why Python programming is awesome
- What are `lists` and how to use them
- What are the differences and similarities between `strings` and `lists`
- What are the most common methods of `lists` and how to use them
- How to use `lists` as `stacks` and `queues`
- What are `list comprehensions` and how to use them
- What are `tuples` and how to use them
- When to use `tuples` versus `lists`
- What is a `sequence`
- What is `tuple packing`
- What is `sequence unpacking`
- What is the `del` statement and how to use it

## Data Types

Python is a dynamically typed language, which means that the Python interpreter infers the type of an object at runtime. In comparison, compiled languages like C are generally statically typed. In these cases, the type of an object has to be attached to the object before compile time.

Datatypes in Python includees:

- **Integers** - Whole numbers which could be positive or negative `a = 10; print(type(a)) # <class int>`
- **Float** - Negative or positive numbers with decimal places or fractions `b = 3.14159; print(type(b)) # <class float>`
- **Strings** - These are streams of text (aplphanumeric characters) that are placed between double quotes `""` or single quotes `''`. `name = "student"; print(type(name)) # <class str>`
- **Lists** - These are an ordered collection of items and an essential data structure in Python Programming Language. They are `mutable` i.e. their values can be modified or their structure modified as well.`animals = ["Deer", "Dog", "Duck", "Dragon"]`
- **Tuples** - These are built in data structure in python. Unlike Lists, tuples are immutable data structure. Once declared and initializzed their values cannot be changed. They are preferred over List when you want to create a data structure that should not be modified. `properties = ("age", "name", "gender", "nationality")`
- **Sets** - A set is defined as a unique collection of unique elements that do not follow a specific order. Sets are used when the existence of an object in a collection of objects is more important than the number of times it appears or the order of the objects.They are mutable and can be modified. `sets = {"first", "second", "third", ..., "item n"}`