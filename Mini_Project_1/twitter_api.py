#!/usr/bin/env python

import tweepy 
import json
import re

#Twitter API credentials
consumer_key = #key1
consumer_secret = #key2
access_key = #key3
access_secret = #key4

def get_tweets(username):
    
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    

    # make initial request for most recent tweets (200 is the maximum allowed count)
    all_tweets = api.user_timeline(screen_name = username,count=15, tweet_mode = 'extended')

    # store text and dates
    alltext = []
    alldate = []

    for status in all_tweets:
        tweet= status._json
        key = 'full_text'
        text = tweet[key]
        text_clean = re.sub(r"http\S+", "", text)
        alltext.append(text_clean)
        key = 'created_at'
        date = tweet[key]
        alldate.append(date)

    # write to the jason file 
    wfile = open('tweet.json', 'w') 
    json.dump([alltext,alldate], wfile)
    print ('Done writing to the file')
    print ('')
    wfile.close()



if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_tweets('@BU_Tweets')
