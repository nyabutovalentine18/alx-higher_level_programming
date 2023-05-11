#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = int(len(sys.argv))
    total = 0
    for j in range(1, number):
        print("{} + {} = {}".format(number, total, number + total))
