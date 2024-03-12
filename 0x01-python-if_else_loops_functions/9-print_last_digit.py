#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
        print(f"{last}", end='')
    else:
        number = -number
        last = number % 10
        print(f"{last}", end='')
    return last
