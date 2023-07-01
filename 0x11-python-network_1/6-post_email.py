#!/usr/bin/python3
"""
Python script that takes in a URL and an email address and sends a POST
request with the email as a parameter and then displays the response.
"""

if __name__ == "__main__":
    import sys
    import requests as req

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    print(req.post(url, data=email).text)
