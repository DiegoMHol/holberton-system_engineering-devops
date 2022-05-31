#!/usr/bin/python3
""" Reddit api, to return subs """
import requests


def number_of_subscribers(subreddit):
    urlr = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(urlr, headers={'User-agent': 'yourbot'},
                           allow_redirects=False)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
