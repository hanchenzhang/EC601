#!/usr/bin/env python

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= file_path

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def google_sentiment(text):
    
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Analyze the sentiment of the text 
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # Print the result 
    print('Text: {}'.format(text))
    print('Sentiment: {:.2f}, {:.2f}'.format(sentiment.score, sentiment.magnitude))
    
    # Return the score
    return sentiment.score
 


if __name__ == '__main__':
    pass
