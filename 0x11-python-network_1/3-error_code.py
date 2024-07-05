#!/usr/bin/python3
"""
Displays response body of a specified URL
"""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))

    except HTTPError as e:
        print(f"Error code: {e.code}")
