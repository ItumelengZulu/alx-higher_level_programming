#!/usr/bin/python3
from sys import argv

# Get the length of the argv list
num_arguments = len(argv) - 1  # Subtract 1 to exclude the script name

# Print the number of arguments
if num_arguments == 0:
    print("0.")
else:
    print("{} argument{}:".format(
        num_arguments, 's' if num_arguments != 1 else ''))

    # Print each argument with its position
    for i, arg in enumerate(argv[1:], start=1):
        print("    {}: {}".format(i, arg))
    print()
