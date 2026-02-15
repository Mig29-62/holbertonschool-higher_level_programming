#!/usr/bin/python3
"""we use  try and except to manage errors,also using .code method to  print status code"""
import urllib.request
import sys
url=sys.argv[1]
try:
    req=urllib.request.Request()
    with urrlib.request.openurl() as response:
        content=response.read()
        content=content.decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
     print("Error code: {}".format(e.code))
