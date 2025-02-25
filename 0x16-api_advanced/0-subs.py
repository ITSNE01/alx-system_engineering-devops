#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers on a given subreddit """
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"})
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
