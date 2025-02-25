#!/usr/bin/python3
""" Prints the titles of the first 10 hot posts listed
    for a given subreddit """
import requests


def top_ten(subreddit):
    """ Prints the titles of the 10 hottest posts on a given subreddit """
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
