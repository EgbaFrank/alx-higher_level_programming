#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""


if __name__ == "__main__":
    import sys
    from urllib.request import urlopen

    url = sys.argv[1]

    with urlopen(url) as response:
        http = response.info()
        print(http.get('X-Request-Id'))
