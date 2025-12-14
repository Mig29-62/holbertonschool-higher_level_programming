#!/usr/bin/python3
"""we define module"""
save=__import__('5-save_to_json_file').save_to_json_file
load=__import__('6-load_from_json_file').load_from_json_file
import sys
l=list(sys.argv)
with open("add_item.json",'w') as f:
    save(l,f)