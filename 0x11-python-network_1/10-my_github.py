#!/usr/bin/python3
"""
Displays your GitHub id via the GitHub API
"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    token = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    header = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=header)

        user_data = response.json()

        print(user_data.get('id'))

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except requests.exceptions.HTTPError as HTTPErr:
        print(f"HTTP Error{HTTPErr}")
