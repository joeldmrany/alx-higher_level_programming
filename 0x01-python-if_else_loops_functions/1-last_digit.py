#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = -(10 - last)
print(f"Last digit of {number} is ", end="")
if last > 5:
    print(f"{last} and is greater than 5")
elif last == 0:
    print(f"{last} and is 0")
else:
    print(f"{last} and is less than 6 and not 0")
