#!/bin/bash
# displays the size of the body of a specified url
curl -s -I "$1" | sed -n '/Content-Length/p' | cut -d ":" -f 2 | cut -c 2-
