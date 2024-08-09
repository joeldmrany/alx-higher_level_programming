#!/usr/bin/python3
""" JSON """
import json


def save_to_json_file(my_obj, filename):
    """ function """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
