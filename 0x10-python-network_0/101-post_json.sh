#!/bin/bash
# Sends a JSON POST request to the specified URL

if [ $# -ne 2 ]; then
	echo "Usage: '$0' [URL] [File]"
	exit 1
fi

curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"
