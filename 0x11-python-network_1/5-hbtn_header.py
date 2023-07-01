#!/usr/bin/python3
"""
Python script that uses the requests library to display the
X-Request-Id header from a given URL
"""
if __name__ == '__main__':
    import sys
    import requests as req

    url = sys.argv[1]
    print(req.get(url).headers.get('X-Request-Id'))
