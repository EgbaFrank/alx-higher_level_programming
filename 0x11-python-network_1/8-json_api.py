#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
"""


if __name__ == "__main__":
    import sys
    import requests

    if len(argv) > 1:
        search_query = sys.argv[1]
    else:
        search_query = ""
    parameter = {'q': search_query}
    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data=parameter)

    try:
        if not response.text.strip():
            print("No result")

        else:
            info = response.json()
            print(f"[{info.get('id')}]: {info.get('name')}")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
