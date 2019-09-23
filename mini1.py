#!/usr/bin/env python

import json
import os
import google_api
import twitter_api

#username = input('Please enter the username: ')
username = '@BU_Tweets'

# grab tweets
twitter_api.get_tweets (username)

# read file
rfile = open('tweet.json', 'r') 
data = json.load(rfile)
rfile.close()


# use google api and store score
allscore = []
for string in data:
  score = google_api.google_sentiment(string)
  allscore.append(score)

# analyze and print result
mean = sum(allscore) / len (allscore)
print ('The average score is: {:.2f}'.format(mean) )

