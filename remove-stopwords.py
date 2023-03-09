import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

'''This code reads each stop word text file and adds the words to a set of stopwords.
The update() method is used to add the words to the set.'''

import os
stopwords_dir = 'GIVEN-DATA\StopWords'
stopwords = set()

for filename in os.listdir(stopwords_dir):
    with open(os.path.join(stopwords_dir, filename), 'r') as f:
        words = f.read().splitlines()
        stopwords.update(words)

#This code reads each text file and adds the text to a list of texts.

text_dir = 'data'
texts = []

for filename in os.listdir(text_dir):
    
    with open(os.path.join(text_dir, filename),'r',encoding="utf8") as f:
        text = f.read()
        texts.append(text)

'''word_tokenize():- it then removes the stop words from the words using a list comprehension and the set of stopwords. '''

from nltk.tokenize import word_tokenize
for i in range(len(texts)):
    words = word_tokenize(texts[i])
    filtered_words = [word for word in words if word.lower() not in stopwords]
    texts[i] = ' '.join(filtered_words)
print(texts)


## Perform sentiment analysis: using textblob liabrary
#pip install textblob
print('sentiments of each text file')
from textblob import TextBlob

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(sentiment)
