#!/usr/bin/python3
"""
A script that fetches a url using the urllib package
"""

if __name__ == '__main__':
    import urllib.request as urlreq

    url = 'https://alx-intranet.hbtn.io/status'
    with urlreq.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
