#!/usr/bin/python3
def get_arg_len(argv):
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{:d} argument.".format(arg_len))
    elif arg_len == 1:
        print("{:d} argument:".format(arg_len))
    else:
        print("{:d} arguments:".format(arg_len))
    return (arg_len)

if __name__ == "__main__":
    import sys
    length = get_arg_len(sys.argv)
    for num in range(1, length + 1):
        print("{}: {}".format(num, sys.argv[num]))
