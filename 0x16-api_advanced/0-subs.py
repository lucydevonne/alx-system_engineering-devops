#!/usr/bin/python3

"""
Queries the Reddit API and returns the no of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    :param subreddit: A string representing the subreddit name.
    :return: An integer representing the number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
