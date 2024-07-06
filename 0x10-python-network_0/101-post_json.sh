#!/bin/bash
# Sends a JSON POST request to the specified URL
curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"
