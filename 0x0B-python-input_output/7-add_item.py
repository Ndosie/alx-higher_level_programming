#!/usr/bin/python3
"""
This is 7-add_item module, a script that reads arguments
and save them in Json file as a list.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, "add_item.json")
