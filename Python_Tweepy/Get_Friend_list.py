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
   
def get_friend_list(num_friends,screen_name):
        friend_list = ''
        count = 0
        for friend in tweepy.Cursor(authenticate_twitter_app().friends, id=screen_name).items(num_friends):
            #friend_list.append(friend)
            #friends = json.dumps(friend._json, indent=5)
            # Name User Followers
            print(friend.name)
            count += 1
        print(count)
        return friend_list

if __name__=="__main__":
    screen_name = 'VeeraphatN'
    fetched_tweets_filename = "tweets.txt"
    data_tweet = get_friend_list(50,screen_name)
    #data = json.loads(data_tweet)
