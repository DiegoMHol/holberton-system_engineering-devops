#!/usr/bin/python3
""" Reddit api, to return subs """
import requests


def top_ten(subreddit):
    urlr = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    request = requests.get(urlr, headers={'User-agent': 'yourbot'},
            allow_redirects=False, params={"limit": 10})
    if request.status_code == 200:
        first = request.json().get("data").get("children")
        for item in first:
            print(item.get("data").get("title"))
    else:
        print(None)
