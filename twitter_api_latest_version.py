#!/usr/bin/env python
# encoding: utf-8
#Author - Hanchen Zhang, Qianqian Guo


import tweepy #https://github.com/tweepy/tweepy
import json
import re


#Twitter API credentials
consumer_key = #key1
consumer_secret = #key2
access_key = #key3
access_secret = #key4


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    

    #make initial request for most recent tweets (200 is the maximum allowed count)
    all_tweets = api.user_timeline(screen_name = screen_name,count=10, tweet_mode = 'extended')

    alltext = []
    alldate = []

    for status in all_tweets:
        tweet= status._json
        #print (tweet)
        key = 'full_text'
        text = tweet[key]
        text_clean = re.sub(r"http\S+", "", text)
        alltext.append(text_clean)
        key = 'created_at'
        date = tweet[key]
        alldate.append(date)

    wfile = open('tweet.json', 'w') 
    json.dump(alltext, wfile)
    json.dump(alldate, wfile)
    print ("Done")
    wfile.close()



if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@BU_Tweets")
