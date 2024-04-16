#!/usr/bin/python3
"""
This module contains JSON functionalities
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

new = load_from_json_file(filename)

new.extend(sys.argv[1:])

save_to_json_file(new, filename)
