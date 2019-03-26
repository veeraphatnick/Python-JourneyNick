from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

        consumer_key = "E6YZaaVCDbxyErKYBRjm9rdbL"
        consumer_secret = "hEZAp5RNEvQRVmCBBDvjCjScKvvn1Twb0QtKhhToOkCsjpGqqt"
        access_token = "222424109-IzmY6ibEyLPUUWvCc8pwQqkXQ3CVWs2V09lkZd5a"
        access_token_secret = "8YGdr7jmySS8ticCDkY7WcHWF98GcnsydRnAdQeDQt8j5"

        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            data = json.loads(data)
            data = json.dumps(data, indent=5)
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["NamneungBNK48"]
    fetched_tweets_filename = "test.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)