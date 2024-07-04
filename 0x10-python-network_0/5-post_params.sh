#!/bin/bash
# Sends a POST request to the specified URL, and displays the body of the response
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
