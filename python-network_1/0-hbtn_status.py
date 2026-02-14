#!/usr/bin/python3
"""we use urllib to get request from specific links"""
import urllib.request
url="https://intranet.hbtn.io/"
with urllib.request.urlopen(url) as response:
	data=response.read()
	content=data.decode('utf-8')
	print(content)
