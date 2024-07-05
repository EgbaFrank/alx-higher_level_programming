#!/usr/bin/python3
"""
Displays response body of a specified URL
"""


if __name__ == "__main__":
    import sys
    from urllib

    try:
        response = urllib.request.urlopen(sys.argv[1])
        print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
