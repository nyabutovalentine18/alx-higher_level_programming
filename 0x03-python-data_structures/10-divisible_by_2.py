#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = len(my_list)
    list_output = []
    for i in range(new_list):
        if my_list[i] % 2 == 0:
            list_output.append(True)
        else:
            list_output.append(False)
    return list_output
