# -*- coding=utf8 -*-
__author__ = 'Esther'

import tweepy
import random
import bildconfig

def login():
    # for info on the tweepy module, see http://tweepy.readthedocs.org/en/

    # OAuth2 Authentication is taken from bildconfig.py
    consumer_key = bildconfig.consumer_key
    consumer_secret = bildconfig.consumer_secret
    access_token = bildconfig.access_token
    access_token_secret = bildconfig.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def make_compound(first_path, second_path):
    """
    Open data files, select random elements, return generated word
    """
    firsts = [line.strip() for line in open(first_path, "r", encoding="utf8").readlines()]
    seconds= [line.strip() for line in open(second_path, "r", encoding="utf8").readlines()]
    start = random.sample(firsts, 1)[0]
    end = random.sample(seconds, 1)[0]
    return start + "-" + end

def tweet_something(debug):
    """
    Generate word and send to Twitter
    """
    api = login()
    output = make_compound("./bild_data/1.txt", "./bild_data/2.txt")
    if debug:
        print(output)
    else:
        api.update_status(status=output)
        print(output)

tweeted = False
while not tweeted:
    try:
        tweet_something(False)
        tweeted = True
    except:
        pass

