#!/usr/bin/env python3
# Author ID: mhamilton-edwards

def add(number1, number2):
    """
    Add two numbers together, return the result.
    If an error occurs, return 'error: could not add numbers'.
    """
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """
    Read a file and return a list of all lines.
    If an error occurs, return 'error: could not read file'.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
