#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print(
            f"Body response:\n"
            f"\t- type: {type(response.text)}\n"
            f"\t- content: {response.text}"
            )
