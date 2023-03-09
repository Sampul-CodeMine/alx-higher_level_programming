#!/usr/bin/python3
def show_arg_len(argv):
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{:d} argument.".format(arg_len))
        return
    else:
        if arg_len == 1:
            print("{:d} argument:".format(arg_len))
        else:
            print("{:d} arguments:".format(arg_len))
        itr = 1
        while itr <= arg_len:
            print("{:d}: {:s}".format(itr, argv[i]))
            itr += 1

if __name__ == "__main__":
    import sys
    show_arg_len(sys.argv)
