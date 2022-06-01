#!/usr/bin/python3
""" Reddit api, to return subs """
import requests


def recurse(subreddit, hot_list=[], after=''):
    request = requests.get('https://reddit.com/r/{}/hot/.json?limit=100\
                  &after={}'.format(subreddit, after),
                  headers={'User-Agent': 'yourbot'}).json()
    try:
        after = request['data']['after']
    except KeyError:
        return None
    for post in request['data']['children']:
        hot_list.append(post['data']['title'])
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
