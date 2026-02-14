#!/usr/bin/python3
"""we use urllib Request to send POST request"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email=email.encode('utf-8')
    data={'email':email}
    data=urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
