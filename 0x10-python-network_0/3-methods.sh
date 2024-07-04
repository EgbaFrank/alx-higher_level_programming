#!/bin/bash
# Displays all HTTP methods the specified url server will accept
curl -X OPTIONS -s "$1"
