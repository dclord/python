#!/usr/bin/python3
import smtplib, tweepy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tweepy import Stream
from tweepy.streaming import StreamListener

data = 0

class MyListener(StreamListener):
        def on_data(self, data):
                try:
                        email(data)
                        return True

                except BaseException as e:
                        print("Error on_data: %s" % str(e))
                        return True

def email(data):
	msg = MIMEMultipart()
	msg['From'] = '<From Addr>'
	msg['To'] = '<To Addr>'
	msg['Subject'] = '<Subject>'
	message = data 
	msg.attach(MIMEText(message))
	username = '<email username>'
	password = '<email password>'
	
	
	mailserver = smtplib.SMTP('smtp.gmail.com', 587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login(username, password)
	mailserver.sendmail('<from addr>', '<to addr>', msg.as_string())
	mailserver.quit()


consumer_key = '<consumer twitter key>'
consumer_secret = '<consumer twitter secret>'
access_token = '<twitter access token>'
access_token_secret = '<twitter access secret>'

# OAuth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create interface
api = tweepy.API(auth)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

