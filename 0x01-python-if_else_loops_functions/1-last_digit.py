#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 0:
    print("{} is positive".format(last_digit))
elif last_digit == 0:
    print("{} is zero".format(last_digit))
else:
    print("{} is negative".format(last_digit))
