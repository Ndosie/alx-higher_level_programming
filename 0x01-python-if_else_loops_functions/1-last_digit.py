#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 0:
    print("is positive")
elif last_digit == 0:
    print("is zero")
else:
    print("is negative")
