#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for j in range(1, len(sys.argv)):
        print("{} + {} = {}".format(number, total, int(len(sys.argv[j])) + total))
