#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"The number is: {number}")
if number > 0:
    print("It's positive!")
elif number < 0:
    print("It's negative!")
else:
    print("It's zero!")
