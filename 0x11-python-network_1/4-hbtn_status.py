#!/usr/bin/python3
"""
This is a script that fetches the URL
(https://alx-intranet.hbtn.io/status)"""

if __name__ == '__main__':
    import requests as req

    rqt = req.get('https://alx-intranet.hbtn.io/status')
    txt = rqt.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
