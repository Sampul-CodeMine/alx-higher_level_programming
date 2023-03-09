#!/usr/bin/python3

# function to get the length of the arguments passed
def get_arg_length(arg):
    num = len(arg) - 1
    if num == 0:
        print("0 argument")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    return (num)


if __name__ == "__main__":
    import sys

    counts = get_arg_length(sys.argv)
    for n in range(counts):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
