#!/bin/bash
# Displays all HTTP methods the specified url server will accept
curl -X OPTIONS -sI "$1" | sed -n '/Allow/p'
