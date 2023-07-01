#!/usr/bin/python3
"""
Python script that takes credentials from a GitHub account and uses GitHub API
to display the ID
"""
if __name__ == '__main__':
    from sys import argv as sarg
    import requests as req
    from requests.auth import HTTPBasicAuth as b_auth

    u_name = sarg[1]
    u_pwd = sarg[2]
    url = 'https://api.github.com/users/{}'.format(u_name)
    data = req.get(url, auth=b_auth(u_name, u_pwd))
    print(data.json().get('id'))
