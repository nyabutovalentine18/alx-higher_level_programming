#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    if number == 0:
        print("{}".format(number), "arguments.")
    elif number == 1:
        print("{}".format(number), "argument:")
    else:
        print("{}".format(number - 1), "arguments:")

    for j in range(1, number):
        print("{:d}: {:s}".format(j, sys.argv[j]))
