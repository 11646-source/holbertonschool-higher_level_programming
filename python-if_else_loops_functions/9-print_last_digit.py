#!/usr/bin/python3
def print_last_digit(number):
    #Get the last digit using modulus
    last = abs(number) % 10
    import sys
    sys.stdout.write(str(last))
    return last
