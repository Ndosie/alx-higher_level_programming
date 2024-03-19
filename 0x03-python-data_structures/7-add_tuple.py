#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            a1, a2 = 0, 0
        else:
            a1, a2 = tuple_a[0], 0
    else:
        a1, a2 = tuple_a

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            b1, b2 = 0, 0
        else:
            b1, b2 = tuple_b[0], 0
    else:
        b1, b2 = tuple_b

    return (a1 + b1, a2 + b2)
