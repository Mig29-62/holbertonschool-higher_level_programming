#!/usr/bin/python3
"""we use urllib to get request from specific links"""
import urllib.request
import sys
url = "https://intranet.hbtn.io"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.info().get('X-Request-Id'))
