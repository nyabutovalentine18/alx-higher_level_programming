#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            numbers = numbers + 1
        except (TypeError, ValueError):
            continue
    print("")
    return numbers
