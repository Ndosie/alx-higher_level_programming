#!/usr/bin/python3
def safe_print_integer(value):
    r = True
    try:
        print("{:d}".format(value))
    except ValueError:
        r = False
    except TypeError:
        r = False
    return r
