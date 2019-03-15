import tweepy
import json
import math
from unidecode import unidecode

def authenticate_twitter_app():
    consumer_key="E6YZaaVCDbxyErKYBRjm9rdbL"
    consumer_secret="hEZAp5RNEvQRVmCBBDvjCjScKvvn1Twb0QtKhhToOkCsjpGqqt"
    access_token="222424109-IzmY6ibEyLPUUWvCc8pwQqkXQ3CVWs2V09lkZd5a"
    access_token_secret="8YGdr7jmySS8ticCDkY7WcHWF98GcnsydRnAdQeDQt8j5"

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    return api

if __name__=="__main__":
    screen_name = 'EmmaWatson'
    user = authenticate_twitter_app().get_user(screen_name)
    #data_user = json.dumps(user._json, indent=5)
    #print(data_user)
    
    column_account = [  'ID',
                        'Name',
                        'Screen Name',
                        'Followers Count',
                        'Friends Count',
                        'Statuses Count',
                        'Favourites Count']
    account = []
    account.append([    user.id, 
                        user.name, 
                        user.screen_name, 
                        user.followers_count, 
                        user.friends_count, 
                        user.statuses_count, 
                        user.favourites_count])

    for i in range(0,len(column_account)):
        print(str(column_account[i])+" : "+str(account[0][i]))

    get_status_by_id = authenticate_twitter_app().get_status(1100492162830000129)._json
    
    get_status = json.dumps(get_status_by_id, indent=5)
    print(get_status)
    #get_status_by_id = json.dumps(get_status_by_id.Status._json, indent=5)

 