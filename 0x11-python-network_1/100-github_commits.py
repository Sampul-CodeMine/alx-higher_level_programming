#!/usr/bin/python3
"""
This is a python script that lists the 10 most recent commits from a repo
owned by a user
"""

if __name__ == '__main__':
    from sys import argv as sarg
    import requests as req

    repo = sarg[1]
    repo_ownr = sarg[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo_ownr, repo)
    res = req.get(url)
    commits = res.json()
    try:
        for commit in commits[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
    except IndexError:
        pass
        ...
