#!/usr/bin/python3
"""
This module contains a function that retrieves the titles of all hot articles
for a given subreddit using recursion.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that retrieves the titles of all hot articles for a given
    subreddit.

    Args:
        subreddit (str): The subreddit to retrieve the hot articles from.
        hot_list (list): The list to append the article titles to.
        after (str): The ID of the last post in the current page of results.

    Returns:
        If successful, a list containing the titles of all hot articles for the
        given subreddit. Otherwise, None.
    """
    # Base case: No subreddit provided or maximum depth reached
    if not subreddit or len(hot_list) >= 100:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    response_data = response.json()
    after = response_data['data']['after']

    for post in response_data['data']['children']:
        hot_list.append(post['data']['title'])

    # Recursive call
    return recurse(subreddit, hot_list, after=after)
