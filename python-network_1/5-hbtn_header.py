#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a GET request,
and displays the 'X-Request-Id' value from the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
