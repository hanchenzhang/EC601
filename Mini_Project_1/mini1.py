#!/usr/bin/env python

import json
import os
import google_api
import twitter_api

# enter username
username = input('Please enter the username: ')
#username = '@BU_Tweets'

# grab tweets
twitter_api.get_tweets (username)

# read file
rfile = open('tweet.json', 'r') 
data = json.load(rfile)
rfile.close()


# use google api and store sentiment score
allscore = []
allmag = []
text = data[0]
date = data[1]
for string in text:
  score, mag = google_api.google_sentiment(string)
  print ('')
  allscore.append(score)
  allmag.append(mag)

# anaylze sentiment
meanscore = sum(allscore) / len (allscore)
meanmag = sum(allmag) / len (allmag)

if meanscore >= 0.25 :
  emo = 'positive emotions'
elif meanscore < 0.25 and meanscore > 0.1 :
  emo = 'slightly positive emotions'
elif meanscore < -0.1 and meanscore > -0.25 :
  emo = 'slightly negative emotions'
elif meanscore <= -0.25 :
  emo = 'negative emotions'
else :
  if meanmag >= 0.2 :
    emo = 'neutral emotions'
  else : 
    emo = 'mixted emotions'

# print results 
print ('Sentiment Analysis Results: ')
print ('From {} to {}'.format(date[-1], date[0]))
print ('The average score is: {:.2f}'.format(meanscore) )
print ('The average magnitude is: {:.2f}'.format(meanmag) )
print ('The user {} reflects {}.'.format(username,emo))




