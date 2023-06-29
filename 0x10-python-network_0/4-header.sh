#!/bin/bash
# Bash script that sends a GET request to a URL with a header variable displaying the body
curl -sH "X-School-User-Id: 98" "${1}"
