#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import sqlite3
import json
from textblob import TextBlob
from unidecode import unidecode

ckey= "x"
csecret= "x"
atoken= "x"
asecret= "x"
bearer_token= "x"



# In[ ]:


conn= sqlite3.connect('twitterdata.db')
c= conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()


# In[ ]:


class MyStream(Stream):
    # This function gets called when the stream is working
    def on_data(self,data):
        try:
            data= json.loads(data)
            tweet= unidecode(data['text'])
            timems= data['timestamp_ms']
            analysis= TextBlob(tweet)
            sentiment= analysis.sentiment.polarity
            print(timems, tweet, sentiment)
            c.execute("INSERT INTO sentiment(unix, tweet, sentiment) VALUES (?,?,?)", (timems, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return True
    def on_error(self, status):
        print(status) 



# In[ ]:


while True:
    try:
        twitterstream= MyStream(ckey, csecret, atoken, asecret)
        twitterstream.filter(track=['a','e','i','o','u'])
    except Exception as e:
        print(str(e))
        time.sleep(5)

