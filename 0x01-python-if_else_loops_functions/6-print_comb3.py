#!/usr/bin/python3

for first_number in range(1, 10):
    for second_number in range(first_number + 1, 10):
        print("{:02}, {:02}".format(first_number, second_number), end=" ")
print()
