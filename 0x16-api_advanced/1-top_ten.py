#!/usr/bin/python3

"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to search for.

    Returns:
        None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 '
               'Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)
