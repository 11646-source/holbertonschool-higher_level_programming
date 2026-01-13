#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5:
    desc = "and is greater than 5"
elif last == 0:
    desc = "and is 0"
else:
    desc = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {desc}")
