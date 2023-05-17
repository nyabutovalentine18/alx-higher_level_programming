#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_multidic = {}
    for k in a_dictionary:
        a_multidic[k] = a_dictionary[k] * 2
    return a_multidic
