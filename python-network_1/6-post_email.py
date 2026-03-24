#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # URL is the first argument, email is the second
    url = sys.argv[1]
    email_address = sys.argv[2]

    # The payload dictionary uses 'email' as the key
    payload = {'email': email_address}

    # Sending the POST request
    response = requests.post(url, data=payload)

    # Displaying the body of the response
    print(response.text)
