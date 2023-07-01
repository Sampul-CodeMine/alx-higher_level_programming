#!/usr/bin/python3
"""
Python script that takes a URL sends a request to the URL and displays the
body of the response getting the HTTP status code if greater than or equal 400
"""
if __name__ == '__main__':
    from sys import argv as sarg
    import requests as req

    url = sarg[1]
    res = req.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
