#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# check if the number is negative or positive
if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is positive")
