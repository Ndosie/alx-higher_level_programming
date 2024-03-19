#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = my_list.copy()
    if len(my_list) == 0:
        return my_list

    for i in range(len(copy)):
        if copy[i] % 2 == 0:
            copy[i] = True
        else:
            copy[i] = False
    return copy
