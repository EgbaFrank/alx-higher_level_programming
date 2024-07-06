#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_query = sys.argv[1]
    else:
        search_query = ""
    parameter = {'q': search_query}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=parameter)
        response.raise_for_status()

        try:
            info = response.json()

            if info:
                print(f"[{info.get('id')}] {info.get('name')}")

            else:
                print("No result")

        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
