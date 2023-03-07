#!/usr/bin/python3
# Program to print numbers from 00 to 99

for num in range(100):
	if (num == 99):
		print("{}".format(num))
	else:
		print("{:02}".format(num), end=", ")
