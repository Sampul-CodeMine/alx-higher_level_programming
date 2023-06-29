#!/bin/bash
# Bash script to display only the status code from a URL
curl -sLw "%{http_code}" -o /dev/null "$1"
