#!/usr/bin/python3
""" JSON """
import json
import sys
import os


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    data = load_json(filename)
else:
    data = []

data.extend(sys.argv[1:])

save_json(data, filename)
