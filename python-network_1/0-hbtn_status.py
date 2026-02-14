#!/usr/bin/python3
"""we use urllib to get request from specific links"""
import urllib.request
url="https://intranet.hbtn.io/status"
req=urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
	body=response.read()
	content=body.decode('utf-8')
	print("Body response:")
	print("\t- type: {}".format(type(body)))
	print("\t- content: {}".format(body))
	print("\t- utf8-content: {}".format(content))
