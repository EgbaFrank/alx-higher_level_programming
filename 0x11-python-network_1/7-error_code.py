#!/usr/bin/python3
"""
Displays the response body of the specified URL
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(response.status_code)
