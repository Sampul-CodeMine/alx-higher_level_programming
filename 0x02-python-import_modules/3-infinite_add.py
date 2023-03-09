#!/usr/bin/python3
def add_arg(argv):
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{:d}".format(arg_len))
        return
    else:
        itr = 1
        add = 0
        while itr <= n:
            add += int(argv[itr])
            itr += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
