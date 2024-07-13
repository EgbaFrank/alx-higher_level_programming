#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""
import sys
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = sys.argv[1]

    request = Request(url)
    with urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
