#!/bin/bash
# Bash scripts that sends a POST request to a URL and displays the body.
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
