#!/usr/bin/pyrhon3

intval = 122
while intval >= 97:
    flag = 0
    if intval % 2 != 0:
        intval -= 32
        flag = 1
    print("{:s}".format(chr(intval)), end="")
    if flag == 1:
        intval += 32
    intval -= 1
