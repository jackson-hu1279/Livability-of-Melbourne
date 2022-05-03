import get_tweet as tw
import couchdb3
import tweepy
import pickle
from shapely.geometry import Point

def main():
    #### Set up
    BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAALWBbQEAAAAA%2FbQ0tpIE3uy14yUmYU0AiocoH6c%3DDkX3Fl2TdMFgRBCivYCSMajfqglkm8DkyylcAXkUFFceAIOBRB"]


    query = 'Melbourne OR #Melbourne lang:en'
    query2 = '#Melbourne lang:en'

    client = couchdb3.Server(
        "http://172.26.132.196:5984",
        user="admin",
        password="admin"
    )
    db_name = "raw_tweets"
    db_name2 = "geo_tweets"

    count = 0
    ### Run
    if(client.up()):
        while(True): ## infinite loop
            if(count == 0):
                next_tokens = tw.crawler(query, BEARER_TOKEN, 50, 40, client, db_name, db_name2)
                count = 1

            next_tokens = tw.crawler(query, BEARER_TOKEN, 50, 5, client, db_name, db_name2)