#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""

import sys
import urllib

if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers().get('X-Request-Id'))
