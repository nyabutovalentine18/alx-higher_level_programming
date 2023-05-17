#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary)
    for k in sort_dic:
        print("{:s}: {}".format(k, a_dictionary[k]))
