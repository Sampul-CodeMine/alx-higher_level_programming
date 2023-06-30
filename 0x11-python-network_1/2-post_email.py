#!/usr/bin/python3
"""
This is a python script that takes a URL, send a POST request adding an email
as a parameter and displays the response decoded in utf-8
"""

if __name__ == '__main__':
    import sys
    import urllib.parse as urlprs
    import urllib.request as urlreq

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlprs.urlencode(value).encode("ascii")

    req = urlreq.Request(url, data)
    with urlreq.urlopen(req) as response:
        print(response.read().decode("utf-8"))
