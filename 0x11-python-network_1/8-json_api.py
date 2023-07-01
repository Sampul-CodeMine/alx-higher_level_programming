#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to a given URL
with the letter as a parameter
"""
if __name__ == '__main__':
    from sys import argv as sarg
    import requests as req

    if len(sarg) == 1:
        letter = ""
    else:
        letter = sarg[1]
    param = {"q": letter}
    data = req.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        res = data.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id')
                                   res.get('name')))
    except ValueError:
        print('Not a valid JSON')
