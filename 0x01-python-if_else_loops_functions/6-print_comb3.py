#!/usr/bin/python3

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print("{:02}".format(first_digit), end="")
        print("{:02}".format(second_digit), end='')
print()
