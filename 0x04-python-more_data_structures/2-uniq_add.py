#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    results = 0
    for i in s:
        results += i
    return results

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
