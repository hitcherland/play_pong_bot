'''Defines the class that we use to interact with twitter'''

import tweepy
from tweepy.binder import bind_api
import logging

tweepy.binder.log.setLevel(logging.DEBUG)

class API(tweepy.API):
    def get_status_with_card(self, id, *args, **kwargs):
        return bind_api(
            api=self,
            path=f'/statuses/show/{id}.json',
            payload_type='status',
        )(*args, include_my_retweet=True, cards_platform="iPhone-13", include_cards=True,
            headers={
                "Accept": "*/*",
                "User-Agent": "Twitter-iPhone/6.45 iOS/9.0.2 (Apple;iPhone8:2;;;;;1)",
                "X-Twitter-Client": "Twitter-iPhone",
                "X-Twitter-API-Version": "5",
                "X-Twitter-Client-Language": "en",
                "X-Twitter-Client-Version": "6.45",
            },
        )

import requests

class TwitterBot:
    '''A bot that interacts with Twitter, using oAuth2'''
    env_prefix = "TWITTER"
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(token_key, token_secret)

        url='https://api.twitter.com/labs/2/tweets/1230264909612691456'
        params={
            'expansions': 'attachments.poll_ids',
            'poll.fields': 'id,options,voting_status'
        }
        headers={
            "Accept": "*/*",
            "User-Agent": "Twitter-iPhone/6.45 iOS/9.0.2 (Apple;iPhone8:2;;;;;1)",
            "X-Twitter-Client": "Twitter-iPhone",
            "X-Twitter-API-Version": "5",
            "X-Twitter-Client-Language": "en",
            "X-Twitter-Client-Version": "6.45",
        }
        req = requests.Request('get', url, auth=auth.apply_auth(), params=params) #, headers=headers)
        prep = req.prepare()
        resp = requests.Session().send(prep)
        js = resp.json()

        print(js)
        exit(1)
        self.api = API(auth)

    def get_last_tweet(self):
        '''Returns the last tweet the supplied account made'''
        tweets = self.api.user_timeline(
            tweet_mode="extended",
            count=1,
            include_cards=True,
            cards_platform="iPhone-13",
            include_my_retweet=True,
            include_entities=True,
            include_card_uri=True,
            trim_user=True,
            headers={
                "Accept": "*/*",
                "User-Agent": "Twitter-iPhone/6.45 iOS/9.0.2 (Apple;iPhone8:2;;;;;1)",
                "X-Twitter-Client": "Twitter-iPhone",
                "X-Twitter-API-Version": "5",
                "X-Twitter-Client-Language": "en",
                "X-Twitter-Client-Version": "6.45",
            })

        if len(tweets) == 0:
            return None

        tweet = tweets[0]
        print([c for c in dir(tweet) if 'card' in c])

        tweet2 = self.api.get_status(id=tweet.id,
                                     include_cards=True,
                                     cards_platform="Android-12")
        print([c for c in dir(tweet2) if 'card' in c])

        #tweet = self.api.get_status_with_card(truncated_tweet.id)
        return tweet

    def read_poll(self):
        '''We try to read some poll information using cards'''
        self.api
