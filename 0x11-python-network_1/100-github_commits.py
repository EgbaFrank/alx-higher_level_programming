#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
of the repository `rails` by the user `rails`
using github API
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} [OWNER] [REPO]")
        sys.exit(1)

    OWNER = sys.argv[1]
    REPO = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(OWNER, REPO)

    try:
        response = requests.get(url, params={'per_page': 10})
        response.raise_for_status()

        try:
            commits = response.json()

            for commit in commits:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')

                print("{}: {}".format(sha, author_name))
                
        except ValueError:
            print("Invalid JSON")

    except requests.exceptions.RequestException as e:
        print(e)
