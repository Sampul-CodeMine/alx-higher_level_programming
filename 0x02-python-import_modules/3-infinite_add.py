#!/usr/bin/python3
def add_arg(argv):
    lent = len(argv) - 1
    total = 0
    if lent == 0:
        print("{:d}".format(lent))
        return
    else:
        for itr in range(lent):
            total += int(argv[itr + 1])
    print("{:d}".format(total))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
