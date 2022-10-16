import socket
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys
import os

import var
search = var.search #gets search variable from var.py
f = open("kill.py", "w") #opens another file to store id of opened bash shell for killing
f.write("id = %d" %os.getpid()) #gets parent id
f.close()

#insert authorisation keys
consumer_key    = ''
consumer_secret = ''
access_token    = ''
access_secret   = ''

#Stream Listener Class
class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket


    def on_data(self, data):
        try:
            msg = json.loads(data) #loads in all tweet data as json file
            #filter to get cleaner text output
            if ('retweeted_status' in msg):
                if ('extended_tweet' in msg['retweeted_status']):
                    print(msg['retweeted_status']['extended_tweet']['full_text'])
                    self.client_socket.send((str(msg['retweeted_status']['extended_tweet']['full_text']) + "\n").encode('utf-8'))
            elif ('extended_status' in msg):
                print(msg['extended_status']['full_text'])
                self.client_socket.send((str(msg['extended_status']['full_text']) + "\n").encode('utf-8'))
            else:
                print(msg['text'])
                self.client_socket.send((str(msg['text']) + "\n").encode('utf-8'))
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

def send_tweets(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetsListener(c_socket), tweet_mode="extended_tweet")
    twitter_stream.filter(track=search, languages=['en'])


if __name__ == "__main__":
    new_skt = socket.socket()         # initiate a socket object
    host = "127.0.0.1"     # local machine address
    port = 5555                 # specific port for your service.
    new_skt.bind((host, port))        # Binding host and port

    print("Now listening on port: %s" % str(port))

    new_skt.listen(5)                 #  waiting for client connection.
    c, addr = new_skt.accept()        # Establish connection with client. it returns first a socket object,c, and the address bound to the socket

    print("Received request from: " + str(addr))
    # and after accepting the connection, we aill sent the tweets through the socket
    send_tweets(c)
