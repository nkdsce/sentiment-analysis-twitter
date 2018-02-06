#ComPilED by AdiTya MoHaN

import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key= 'xxxxxx'
consumer_secret= 'xxxxxxxx'

access_token = 'xxxxxx'
access_token_secret = 'xxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('india')


#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

csvfile = open('twitter_sentiment.csv', 'wb') #open file for operation
writer = csv.writer(csvfile)   



for tweet in public_tweets:
    foo = tweet.text.encode('utf-8').strip()  #this encoding formatting was required to make file writing of tweets  troublefree, as some   characters in the tweets faced format problems

    analysis = TextBlob(tweet.text).sentiment
    emotion = analysis.polarity
    if emotion > 0:
       writer.writerow([foo,"positive",analysis]) 
    else : 
       writer.writerow([foo,"negative",analysis])         
    
csvfile.close()
print("ENtire process completed successfully ! Open your CSV file and look at the results.")
