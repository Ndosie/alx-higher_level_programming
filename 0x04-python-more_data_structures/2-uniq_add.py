#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    results = 0
    for i in s:
        results += i
    return results
