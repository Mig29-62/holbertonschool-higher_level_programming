#!/usr/bin/python3
"""
Sends a GET request to a URL and displays the 'X-Request-Id' response header.
"""
import requests
import sys

if __name__ == "__main__":
    # Ensure an argument was actually passed to avoid IndexError
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            response = requests.get(url)
            # .get() returns None if the key doesn't exist
            request_id = response.headers.get('X-Request-Id')
            
            if request_id:
                print(request_id)
        except requests.exceptions.RequestException as e:
            # Handle connection errors gracefully
            pass
