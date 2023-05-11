#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    if number == 1:
        print("{}".format(number - 1),"arguments.")
    elif number == 2:
        print("{}".format(number - 1), "argument:")
    else:
        print("{}".format(number - 1), "arguments:")

    for j in range(1, number):
        print("{}: {}".format(j, sys.argv[j]))
