#!/bin/bash
#Bash script to get the HTTP response header for a URL
curl -s "$1" | wc -c
