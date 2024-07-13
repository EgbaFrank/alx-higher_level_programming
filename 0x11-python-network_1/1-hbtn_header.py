#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
