#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return(my_list[-1])
