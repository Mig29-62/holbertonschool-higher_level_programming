#!/usr/bin/python3
"""
Sends a POST request to a search API with a letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # URL to send the request to
    url = "http://0.0.0.0:5000/search_user"

    # Set q to the first argument if it exists, otherwise use an empty string
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Prepare the payload
    payload = {'q': q}

    try:
        # Send the POST request
        response = requests.post(url, data=payload)
        
        # Parse the JSON response
        user_data = response.json()

        # Check if the dictionary is empty
        if not user_data:
            print("No result")
        else:
            # Display the id and name in the format [<id>] <name>
            print("[{}] {}".format(user_data.get('id'), user_data.get('name')))

    except ValueError:
        # This handles cases where response.json() fails
        print("Not a valid JSON")
