#!/usr/bin/python3
"""
Uses GitHub API to display the user id of a given profile.
"""
import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        pass
