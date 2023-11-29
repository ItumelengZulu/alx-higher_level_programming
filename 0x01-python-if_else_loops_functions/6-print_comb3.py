#!/usr/bin/python3

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print(
            "{:01d}{:01d}".format(first_digit, second_digit),
            end=', ' if second_digit < 9 else '\n'
            )
