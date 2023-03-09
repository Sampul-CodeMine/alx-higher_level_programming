#!/usr/bin/python3
def add_arg(argv):
    summ = 0
    for itr in range(len(sys.argv) - 1):
        summ += int(argv[itr + 1])
    print("{}".format(summ))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
