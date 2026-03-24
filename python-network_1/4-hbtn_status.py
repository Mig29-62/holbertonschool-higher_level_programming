#!/usr/bin/python3
"""we use this module to fetch type and content
   and we use print function to output all needed
   information accordingly"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
