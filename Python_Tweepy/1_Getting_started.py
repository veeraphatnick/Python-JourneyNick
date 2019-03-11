import tweepy

consumer_key = "E6YZaaVCDbxyErKYBRjm9rdbL"
consumer_secret = "hEZAp5RNEvQRVmCBBDvjCjScKvvn1Twb0QtKhhToOkCsjpGqqt"
access_token = "222424109-IzmY6ibEyLPUUWvCc8pwQqkXQ3CVWs2V09lkZd5a"
access_token_secret = "8YGdr7jmySS8ticCDkY7WcHWF98GcnsydRnAdQeDQt8j5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''
user = api.get_user('VeeraphatN')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)