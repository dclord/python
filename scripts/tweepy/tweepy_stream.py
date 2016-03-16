#!/usr/bin/python
import tweepy, json

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
			return True

	def on_error(self, status):
		print(status)
		return True

#def process_or_store(status):
#	print(json.dumps(status))

#keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create interface
api = tweepy.API(auth)

# JSON
#for status in tweepy.Cursor(api.home_timeline).items(10):
#	process_or_store(status._json)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
