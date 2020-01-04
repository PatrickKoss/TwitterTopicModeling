try:
    import json
except ImportError:
    import simplejson as json

import tweepy
import os
import time
import pandas as pd

# set the consumer key and access token from the local windows environment
consumer_key = os.environ.get('tweepy_consumer_key')
consumer_key_secret = os.environ.get('tweepy_consumer_key_secret')
access_token = os.environ.get('tweepy_access_token')
access_token_secret = os.environ.get('tweepy_access_token_secret')

# create the auth for tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

# set the api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# when running the first create an empty dataframe for the tweets
# df = pd.DataFrame(columns=['tweet'])
# export_csv = df.to_csv(r'tweets.csv', index=None, header=True)

# read in the tweets from before
df = pd.read_csv("tweets.csv", encoding="utf-8", error_bad_lines=False)

for tweet in tweepy.Cursor(api.search, q='*', count=20, lang='en', since='2017-06-20', tweet_mode='extended').items():
    print(tweet._json)
    # if the tweet is a retweet then add the original tweet to the dataset otherwise add the tweet
    if "retweeted_status" in tweet._json:
        df = df.append({'tweet': tweet._json['retweeted_status']['full_text']}, ignore_index=True)
    else:
        df = df.append({'tweet': tweet._json['full_text']}, ignore_index=True)

    # save the tweet to the dataset since this for loop will run forever
    export_csv = df.to_csv(r'tweets.csv', index=None, header=True)
    # wait two seconds to avoid time out errors from the api
    time.sleep(2)
