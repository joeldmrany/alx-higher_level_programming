#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = 10 - (number % 10)
    print(f"Last digit of {number:d} is -{last} and is less than 6 and not 0")

else:
    last = number % 10
    if last > 5:
        print(f"Last digit of {number:d} is {last} and is greater than 5")
    elif last < 6 and last != 0:
        print(f"Last digit of {number:d} is {last}")
        print(" and is less than 6 and not 0")

    elif last == 0:
        print(f"Last digit of {number:d} is {last} and is 0")
