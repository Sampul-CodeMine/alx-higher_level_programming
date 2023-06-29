#!/bin/bash
# Bash script to display all HTTP methods the server of a given URL allows
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
