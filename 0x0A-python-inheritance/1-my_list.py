#!/usr/bin/python3
"""
classes
"""


class MyList(list):
    """ print sorted list """
    def print_sorted(self):
        print(sorted(self))
