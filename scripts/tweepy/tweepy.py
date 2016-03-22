#!/usr/bin/python3
import tweepy

from tweepy.auth import OAuthHandler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create interface
api = tweepy.API(auth)

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

