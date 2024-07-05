#!/usr/bin/python3
"""
sends an email via a POST request to the passed URL
"""


if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.parse import urlencode

    url = sys.argv[1]
    email = sys.argv[2]

    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data)

    with urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
