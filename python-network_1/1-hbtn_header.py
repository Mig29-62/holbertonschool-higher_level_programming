#!/usr/bin/python3
"""we use urllib to get request from specific links"""
import urllib.request
import sys
if __name__="__main__":
    url =sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
 
