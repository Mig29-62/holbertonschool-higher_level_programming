#!/usr/bin/python3
"""
Sends a POST request to a search API with a letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    try:
        response = requests.post(url, data=payload)
        user_data = response.json()
        if not user_data:
            print("No result")
        else:
            print("[{}] {}".format(user_data.get('id'), user_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
