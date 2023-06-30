#!/usr/bin/python3
"""
This is a python script that accepts a URL, sends a request to the URL and
displays the body of the URL decoded in UTF-8
"""

if __name__ == '__main__':
    import sys
    import urllib.request as urlreq
    import urllib.error as urlerr

    try:
        url = sys.argv[1]
        with urlreq.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urlerr.HTTPError as err:
        print('Error code: {}'.format(err.code))
