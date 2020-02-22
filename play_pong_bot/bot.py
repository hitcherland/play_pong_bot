'''Defines the class that we use to interact with twitter'''

import requests
from requests_oauthlib import OAuth1

class TwitterBot:
    '''A bot that interacts with Twitter, using oAuth2'''
    env_prefix = "TWITTER"
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.auth = OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def get_last_tweet(self, need_polls=True):
        url='https://api.twitter.com/1.1/statuses/user_timeline.json'
        resp = requests.get(url, auth=self.auth, params={
            'count': 1,
            'exclude_replies': False,
        })

        js = resp.json()
        if len(js) == 0:
            return None

        id = js[0]['id']

        params = {}
        if need_polls:
            params.update({
                'expansions': 'attachments.poll_ids',
                'poll.fields': 'id,options,voting_status'
            })

        url=f'https://api.twitter.com/labs/2/tweets/{id}'
        resp = requests.get(url, auth=self.auth, params=params)
        return resp.json()
