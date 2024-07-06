#!/bin/bash
# Displays only the response status code of a specified URL
curl -o /dev/null -sw '%{http_code}' "$1"
