#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = 10 - (number % 10)
        print(f"{last}", end='')
    else:
        last = number % 10
        print(f"{last}", end='')
    return last
