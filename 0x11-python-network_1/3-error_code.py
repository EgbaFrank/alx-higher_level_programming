#!/usr/bin/python3
"""
Displays response body of a specified URL
"""


if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        response = urlopen(sys.argv[1])
        print(response.read().decode('utf-8'))

    except HTTPError as e:
        print(f"Error code: {e.code}")
