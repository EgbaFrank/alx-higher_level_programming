#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
of the repository `rails` by the user `rails`
"""
import sys
import requests


if __name__ == "__main__":
    OWNER = sys.argv[1]
    REPO = sys.argv[2]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"

    try:
        response = requests.get(url, params={'per_page': 10})
        commits = response.json()

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')

            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error handling request: {e}")
