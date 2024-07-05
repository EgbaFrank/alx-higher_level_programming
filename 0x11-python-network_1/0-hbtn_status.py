#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status
'''


if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print(
                f"Body response:\n"
                f"\t- type: {type(html)}\n"
                f"\t- content: {html}\n"
                f"\t- utf8 content: {html.decode('utf-8')}"
                )
