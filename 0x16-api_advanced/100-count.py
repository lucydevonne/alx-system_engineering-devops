#!/usr/bin/python3
"""
Count Words
"""

import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.
    """
    # Initialize count_dict if it is not provided
    if count_dict is None:
        count_dict = {}
    
    # Build URL for API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Set user-agent header to avoid 429 error
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Send API request
    response = requests.get(url, headers=headers, params={"after": after})
    if response.status_code == 404:  # Invalid subreddit
        return
    
    # Extract data from API response
    data = response.json().get("data")
    if data is None:  # No more articles
        # Sort and print count_dict
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return
    
    # Iterate over articles and update count_dict
    articles = data.get("children", [])
    for article in articles:
        title = article.get("data", {}).get("title", "").lower()
        for word in word_list:
            # Check if word is in title
            if word.lower() in title:
                # Clean word
                word = word.lower().strip("!?.,")
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
    
    # Recursively call count_words with the next "after" value
    after = data.get("after")
    count_words(subreddit, word_list, count_dict, after)
