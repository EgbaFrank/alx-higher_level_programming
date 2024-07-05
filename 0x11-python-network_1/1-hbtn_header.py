#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
from a specified URL
"""


if __name__ == "__main__":
    import sys
    from urllib

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        http = response.info()
        print(http.get('X-Request-Id'))
