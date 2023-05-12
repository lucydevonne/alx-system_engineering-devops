#!/usr/bin/python3
"""A recursive function that queries the Reddit API
and returns a list with titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API
    and returns a list with the titles of all hot articles for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if data is None:
        return None

    children = data.get('children')
    if children is None or len(children) == 0:
        return hot_list

    for child in children:
        title = child.get('data').get('title')
        if title is not None:
            hot_list.append(title)

    if len(hot_list) >= 1000:
        return hot_list

    after = data.get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
