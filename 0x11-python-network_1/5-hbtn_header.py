#!/usr/bin/python3
"""
Displays response header variable X-Request-Id value
"""

if __name__ == "__main__":
    import sys
    import requests

    response = requests.head(sys.argv[1])

    print(response.headers.get('X-Request-Id'))
