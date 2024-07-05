#!/usr/bin/python3
"""
Displays the response body of the specified URL
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.exceptions import HTTPError

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError:
        if response.status_code >= 400:
            print(response.status_code)
