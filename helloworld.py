import tweepy
import os
import csv

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet = 'Hello, world!'
# api.update_status(status=tweet)

# query = 'OA OR Oblivion Allstars OR Unity OR QMA OR Sparks OR Ascension Eagles OR AE OR Surrey Starlets OR Eclipse OR Royals OR Marshals OR Coventry Dynamite'
query = 'bunny OR muffin'
max_tweets = 100

results = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

# create csv file for data to go into
with open('cheer_teams.csv', 'a') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # write tweets to csv file
    for tweet in results:
        filewriter.writerow([tweet.text.encode('utf-8')])
        print(tweet)
