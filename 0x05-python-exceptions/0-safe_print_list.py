#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0;

    try:
        for i in range(x + 1):
            print(my_list[i], end="")
        print()
    except IndexError:
        print()
    return i + 1;
