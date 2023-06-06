#!/usr/bin/python3
'''
Module contains function that queries
the Reddit API and returns the number of subscribers
'''

import requests


def number_of_subscribers(sub):
    '''
    Function queries the Reddit API
    '''
    req = requests.get("https://www.reddit.com/r/{}/about.json".format(sub),
                       headers={"User-Agent": "ALX"})

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
