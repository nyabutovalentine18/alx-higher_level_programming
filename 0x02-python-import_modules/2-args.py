#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 1:
        print("{}".format(number), "arguments.")
    elif number == 2:
        print("{}".format(number), "argument:")
    else:
        print("{}".format(number), "arguments:")

    for j in range(number):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
