#!/usr/bin/python3
for i in range(100):
    if i == 0:
        continue
    elif i // 10 == i % 10:
        continue
    print("{:02d}, ".format(i), end="")
