import tweepy
import json
import math

def authenticate_twitter_app():
    consumer_key="E6YZaaVCDbxyErKYBRjm9rdbL"
    consumer_secret="hEZAp5RNEvQRVmCBBDvjCjScKvvn1Twb0QtKhhToOkCsjpGqqt"
    access_token="222424109-IzmY6ibEyLPUUWvCc8pwQqkXQ3CVWs2V09lkZd5a"
    access_token_secret="8YGdr7jmySS8ticCDkY7WcHWF98GcnsydRnAdQeDQt8j5"

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    return api

def get_user_timeline_tweets(num_tweets,screen_name,fetched_tweets_filename):
    tweets = ''
    count = 0
    for tweet in tweepy.Cursor(authenticate_twitter_app().user_timeline, id=screen_name).items(num_tweets):
        #tweets.append(tweet)
        tweets = json.dumps(tweet._json, indent=5)
        print(tweets)
        with open(fetched_tweets_filename, 'a') as tf:
            tf.write(tweets)
        count += 1
    print(count)
    return tweets    

if __name__=="__main__":
    screen_name = 'VeeraphatN'
    fetched_tweets_filename = "tweets.txt"
    data_tweet = get_user_timeline_tweets(20,screen_name,fetched_tweets_filename)
    data = json.loads(data_tweet)
