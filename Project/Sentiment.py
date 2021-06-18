import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import re

class Twitter:
    def __init__(self):

        consumer_key = 'XpAIQHkMgCBO8L8UYQ4FJv4q3'
        consumer_secret = 'wKTz6i17OfJHUFX0u04mC8dIbzhHtE2TithOvMAhuaD6BfmIMb'
        access_token = '165156783-DJ5R2yvppy8MwMUnQKPRIBjew3gYS2DYKr9uWfo5'
        access_token_secret = 'OMxLuGnHiqXpQEqaxn0JQxzjdq1ISMgneHCPnzg4q3dUn'

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed") 

    def cleaning(self,tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self,tweet):

        predict_sentiment = TextBlob(self.cleaning(tweet))

        if predict_sentiment.sentiment.polarity > 0:
            return 'positive'
        elif predict_sentiment.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self,query,count):

        tweets = []
        try:
            fetched_tweets = self.api.search(q = query, count = count)
            # print(fetched_tweets)
            for tweet in fetched_tweets:

                parsed_tweet = {}

				# saving text of tweet
                parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))
        


if __name__ == '__main__':

    api = Twitter()

    search_term = input("Enter the keyword: => ")
    no_of_terms = int(input("Enter how many tweets you want to fetch => "))
    res = api.get_tweets(search_term,no_of_terms)
    ptweets = []
    ntweets = []
    for tweet in res:
        if tweet['sentiment'] == 'positive':
            ptweets.append(tweet)
        elif tweet['sentiment'] == 'negative':
            ntweets.append(tweet)
    # print(ptweets,ntweets)    
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(res)))    
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(res)))
    print("Neutral tweets percentage: {} % \
		".format(100*(len(res) -(len( ntweets )+len( ptweets)))/len(res)))

    	# printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

	# printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])




