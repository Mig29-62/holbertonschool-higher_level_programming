#!/usr/bin/python3
"""we use urllib to get request from specific links"""
import urllib.request
url = "https://intranet.hbtn.io/status"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    body = response.getheader("X-Request-Id")
    print(body)
