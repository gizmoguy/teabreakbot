#!/usr/bin/env python

import tweepy
import json
import os.path

import teabreakbotconfig

def fetch_tweets(max_id = None, min_id=None):
	#Waikato CompSci Tea - 197261726
	user_id = 197261726
	tweetset = api.user_timeline(user_id, count=100, max_id=min_id, since_id=max_id)
	data = []
	for i in tweetset:
		print "%s" % i.text
		data.append((i.id, i.text))
	return data

cachefile_path = os.path.expanduser('teabreaks.json')

config = teabreakbotconfig.read_config()

consumer_key= config.get('twitter','consumer_key')
consumer_secret= config.get('twitter','consumer_secret')

access_token= config.get('twitter','access_key')
access_token_secret= config.get('twitter','access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

if os.path.exists(cachefile_path):
	try:
		cachefile = open(cachefile_path,'r')
		tweets = json.load(cachefile)
		tweets = sorted(tweets, key=lambda tweet: tweet[0])
		print "Cachefile successfully loaded [%s]" % cachefile_path
	except:
		print "Failed to load cachefile! [%s]" % cachefile_path
		exit(1)

# check to make sure we have the oldest tweets
min_id = None
if len(tweets) != 0:
	min_id = tweets[0][0] - 1

while True:
	t = fetch_tweets(min_id=min_id)
	if len(t) == 0:
		break
	tweets.extend(t)
	
	tweets = sorted(tweets, key=lambda tweet: tweet[0])

	min_id = tweets[0][0] - 1

# check to make sure we have the newest tweets
max_id = None
if len(tweets) != 0:
	max_id = tweets[len(tweets) -1][0] + 1

while max_id:
	t = fetch_tweets(max_id=max_id)
	if len(t) == 0:
		break
	tweets.extend(t)
	
	tweets = sorted(tweets, key=lambda tweet: tweet[0])

	max_id = tweets[len(tweets) -1][0] + 1

cachefile = open(cachefile_path,'w')
json.dump(tweets, cachefile)
cachefile.close()

print "%d tweets successfully saved to cachefile [%s]" % (len(tweets), cachefile_path)
