#!/bin/bash
# displays the body from a get request of a specified url
[ $(curl -s -I "$1" | sed -n '/HTTP/p' | cut -d ' ' -f 2) -eq 200 ] && curl -s "$1"
