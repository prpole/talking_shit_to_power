#!/usr/bin/python

import sys

import tweepy,sys,time,random
from nltk.tokenize import RegexpTokenizer

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET_KEY'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'YOUR_ACCESS_KEY'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'YOUR_ACCESS_SECRET_KEY'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

nowtime = str(time.time())

api.update_status(status='@readDonaldTrump Go fuck yourself. #TalkingShitToPower \n \n \n \n \n #'+nowtime)
