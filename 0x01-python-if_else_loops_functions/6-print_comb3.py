#!/usr/bin/python3
# Author - Dukeson Ehigboria
for number in range(10):
    for digit in range(number + 1, 10):
        if number == 8 and digit == 9:
            print("{}{}".format(number, digit))
        else:
            print("{}{}".format(number, digit), end=", ")
