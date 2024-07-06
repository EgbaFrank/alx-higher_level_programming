#!/bin/bash
# Displays only the response status code of a specified URL

if [ $# -ne 1 ]; then
	echo "Usage: '$0' [URL]"
	exit 1
fi

curl -o /dev/null -sw '%{http_code}\n' "$1"
