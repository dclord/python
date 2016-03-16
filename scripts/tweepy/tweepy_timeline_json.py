#!/usr/bin/python
import tweepy, json


def process_or_store(status):
	print(json.dumps(status))

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create interface
api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
#	print(status.text)

# JSON
for status in tweepy.Cursor(api.home_timeline).items(10):
	process_or_store(status._json)


