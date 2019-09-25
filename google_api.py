#!/usr/bin/env python

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=#file_path

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def google_sentiment(text):
    
    # instantiates a client
    client = language.LanguageServiceClient()

    # text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # analyze the sentiment of the text 
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # print the result 
    print('Text: {}'.format(text))
    print('Sentiment score: {:.2f}, magnitude: {:.2f}'.format(sentiment.score, sentiment.magnitude))
    
    # return the scores
    return sentiment.score, sentiment.magnitude
 

if __name__ == '__main__':
    pass
