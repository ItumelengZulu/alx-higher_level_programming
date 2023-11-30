#!/usr/bin/python3
import sys


def add_arguments(args):
    # Convert each argument to an integer and sum them up
    result = sum(int(arg) for arg in args)
    return result


if __name__ == "__main__":
    # Extract command line arguments excluding the script name
    arguments = sys.argv[1:]

    # Call the function and print the result
    result = add_arguments(arguments)
    print(result)
