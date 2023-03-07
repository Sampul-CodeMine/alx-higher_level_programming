# CONTROL FLOWS AND CONDITIONAL TOOLS IN PYTHON PROGRAMMING

We have looked into the basis of Python programming language and we know that we have some data types in Python.

- Numbers
  - Integers (positive or negative numbers without decimal places: e.g. 12, 4, -12, -43)
  - Floats (negative or positive numbers that have decimal places: e.g. 3.14159, -22.7)
  - Complex numbers
- Strings (values that are enclosed in quotation marks either double or singles "Dennis", 'Williams')
- Lists (Compound data type that are used to group together other values: e.g. [1, 4, 6, 7])
- Tuples 
- Dictionaries
- Sets etc.

We will be looking at how to perform conditional operations, and control flow to program logic.

## `if - Else` Statements

This is the most well-known statement type in most programming language and there is no exception to Python. The syntax is given below

```python
if condition:
        # run this code
else:
        # run this code
```

Where you have more than one condition, you can use this syntax:

```python
if first_condition:
        # run this code
elif second_condition:
        # run this code
else:
        # run this code
```

## `for` Statements

The `for` statement differs a bit from the for statements used in `C` programming language. The Python `for` statment iterates over sequences of a list or string in the order they appear.

```python
animals = ['Cat', 'Dog', 'Antelope', 'Lion', 'Tiger']
for animal in animals:
        print("Animal is ", animal)


# This will print out the following below
'''
Animal is  Cat
Animal is  Dog     
Animal is  Antelope
Animal is  Lion    
Animal is  Tiger
'''
```

Another example is thus:

```python
name = "Sampul"
for chr in name:
        print(f"Character is {chr}")


# This will print out the following below
'''
Character is S
Character is a
Character is m
Character is p
Character is u
Character is l
'''
```

You could specify a range 

```python
for num in range(1, 5):
        if num % 2 == 0:
                print(f"{num} is an even number")
        else:
                print(f"{num} is an odd number")


# This will print out the following below
'''
1 is an odd number
2 is an even number
3 is an odd number 
4 is an even number
5 is an odd number 
'''
```
