#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# My code
print('The number is: ', number)

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero.")
else:
    print("Negative.")
