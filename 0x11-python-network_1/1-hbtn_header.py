#!/usr/bin/python3
"""
This is a python script that takes a URL and displays the X-Request-Id
variable in the header of the response
"""

if __name__ == '__main__':
    import sys
    import urllib.request as urlreq

    url = sys.argv[1]

    req = urlreq.Request(url)
    with urlreq.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
