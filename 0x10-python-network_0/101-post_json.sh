#!/bin/bash
# Bash script that sends a JSON POST request to a URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
