#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# convert the number into a string
str_num = str(number)

# get the last digit of the stringed number
lastdigit = str_num[-1]
lastdigit = int(lastdigit)

#get my conditions to output
if lastdigit > 5:
    print(f"Last digit of {number:d} is {lastdigit} and is greater than 5\n")
elif (lastdigit < 6) and (lastdigit != 0):
    print(f"Last digit of {number:d} is {lastdigit} and is less than 6 and not 0\n")
elif lastdigit == 0:
    print(f"Last digit of {number:d} is {lastdigit} and is 0\n")