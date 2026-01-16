#!/bin/usr/python3
def print_last_digit(number):
    #Get the last digit using modulus
    last = abs(number) % 10
    print(last)
    return last
