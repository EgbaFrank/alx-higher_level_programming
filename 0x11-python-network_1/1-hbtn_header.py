#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""
import sys
import urllib


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.headers).get('X-Request-Id'))
