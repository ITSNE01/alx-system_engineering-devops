#!/usr/bin/python3
""" Returns a list of the titles of all hot articles for a given subreddit """

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ Returns a list of titles of all hot posts on a given subreddit """

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"},
                            params={"count": count, "after": after},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    full_hotlst = hot_list + [child.get("data").get("title")
                              for child in response.json()
                              .get("data")
                              .get("children")]
    page_info = response.json()
    if not page_info.get("data").get("after"):
        return full_hotlst

    return recurse(subreddit, full_hotlst, page_info.get("data").get("count"),
                   page_info.get("data").get("after"))
