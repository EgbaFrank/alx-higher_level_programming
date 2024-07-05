#!/usr/bin/python3
"""
Displays response body of a specified URL
"""
import sys
import urllib


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
