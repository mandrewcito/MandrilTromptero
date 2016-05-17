import ctes
from tweepy.streaming import StreamListener
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream
import json
class StdOutListener(StreamListener):
  """ A listener handles tweets are the received from the stream.
 This is a basic listener that just prints received tweets to stdout.
  """
  def on_data(self, data):
    data=json.loads(data)
    print data["user"]["name"]+" -> "+data["text"]
    #print data
    return True
  def on_error(self, status):
    print status
if __name__ == '__main__':
  l = StdOutListener()
  auth = OAuthHandler(ctes.consumer_key, ctes.consumer_secret)
  auth.set_access_token(ctes.access_token, ctes.access_token_secret)
  stream = Stream(auth, l)
  stream.filter(track=['rajoy'])
