#!/usr/bin/env python3
'''Commandline interface for the play_pong_bot class'''

import os
from play_pong_bot.bot import TwitterBot

ENV_PREFIX = 'PLAY_PONG_BOT'

def main():
    '''The main function, this should run once per update'''
    consumer_key = os.environ.get(f'{ENV_PREFIX}_CONSUMER_KEY')
    consumer_secret = os.environ.get(f'{ENV_PREFIX}_CONSUMER_SECRET')
    token_key = os.environ.get(f'{ENV_PREFIX}_TOKEN_KEY')
    token_secret = os.environ.get(f'{ENV_PREFIX}_TOKEN_SECRET')

    bot = TwitterBot(consumer_key, consumer_secret, token_key, token_secret)

    tweet = bot.get_last_tweet(need_polls=True)
    print(tweet)

if __name__ == '__main__':
    main()
