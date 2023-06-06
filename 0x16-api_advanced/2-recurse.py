#!/usr/bin/python3
'''
Module contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for
a given subreddit
'''

import requests


def recurse(sub, hot_list=[], after=""):
    """
    queries the Reddit API and returns a list containing the titles
    of all hot articles for the given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(sub)
    user_agent = {"User-Agent": "ALX"}
    req = requests.get(url, headers=user_agent, params={"after": after})

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return (hot_list)
        else:
            return recurse(sub, hot_list, after)
    else:
        return ("None")
