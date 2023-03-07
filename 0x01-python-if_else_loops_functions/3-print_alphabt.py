#!/usr/bin/python3

# program to print all alphabets in lower case
# from a - z

for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print("{}".format(chr(i)), end="")
