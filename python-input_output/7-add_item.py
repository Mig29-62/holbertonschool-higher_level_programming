#!/usr/bin/python3
"""we define module"""
save=__import__('5-save_to_json_file').save_to_json_file
load=__import__('6-load_from_json_file').load_from_json_file
import sys
if 'add_item.json':
    l=list(load('add_item.json'))
else:
    pass
l.append(list(sys.argv[1:]))
save(l,'add_item.json')