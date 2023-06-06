#!/usr/bin/python3
'''
Module contains function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
'''

import requests


def top_ten(sub):
    '''
    Function queries and prints the titles of the first 10 hot
    posts listed in a given subreddit
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(sub)
    req = requests.get(url, headers={"User-Agent": "AL"}, params={"limit": 10})

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            print(title)
    else:
        print("None")
