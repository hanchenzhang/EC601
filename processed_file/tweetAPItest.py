#!/usr/bin/env python
# encoding: utf-8
#This is the file that print out the twitter content, which works for comparison 
#with dumped json file


import tweepy #https://github.com/tweepy/tweepy

#Twitter API credentials
consumer_key = #key1
consumer_secret = #key2
access_key = #key3
access_secret = #key4

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

user_tweets = api.user_timeline('BU_Tweets')
print(user_tweets)
for tweet in user_tweets:
    print(tweet.text)
