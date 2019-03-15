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
    reply_count, retweeted_count, original_tweets_count = 0,0,0
    for tweet in tweepy.Cursor(authenticate_twitter_app().user_timeline, id=screen_name).items(num_tweets):
        #tweets.append(tweet)
        tweets = json.dumps(tweet._json, indent=5)
        if(tweet.in_reply_to_status_id != None):
            #print("Reply to Status :",tweet.in_reply_to_status_id)
            reply_count += 1
        elif(tweet.text.startswith("RT @") == True):
            #print("Retweeted Status :",tweet.id)
            retweeted_count += 1
        else:
            print("Original Tweets :",tweet.id)
            original_tweets_count += 1
        #with open(fetched_tweets_filename, 'a') as tf:
        #    tf.write(tweets)
    print(reply_count)
    print(retweeted_count)
    print(original_tweets_count)
    return tweets    

if __name__=="__main__":
    screen_name = 'VeeraphatN'
    fetched_tweets_filename = "tweets.txt"
    fetched_tweets_filename = "retweets.txt"
    fetched_tweets_filename = "reply.txt"
    data_tweet = get_user_timeline_tweets(20,screen_name,fetched_tweets_filename)
    data = json.loads(data_tweet)
