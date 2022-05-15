# ----------------------------------------------
# --------
#
# Cluster and Cloud Computing Assignment 2 - Team 53
# 
# Authors: 
# - Chi Yin Wong (Student ID: 836872)
# - Kaiquan Lin (Student ID: 1147233)
# - Renkai Liao (Student ID: 1141584)
# - Renwei Hu (Student ID: 1067974)
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Author of this file:
# - Renkai Liao (Student ID: 1141584)
#
# Location:
# - China
#
# --------
# ----------------------------------------------


import get_tweet as tw
import couchdb3
import tweepy
import pickle
import time
from shapely.geometry import Point

def main():
    """
    This function is used as a template to run a tweet harvester instance
    To run a tweet harvester instance, simply modify information in this file, do not change other files.
    You can reate as many instances as you want from this template if you have enough toekns.
    """
    #### Set up
    BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAALWBbQEAAAAA%2FbQ0tpIE3uy14yUmYU0AiocoH6c%3DDkX3Fl2TdMFgRBCivYCSMajfqglkm8DkyylcAXkUFFceAIOBRB"]


    query = 'Melbourne OR #Melbourne lang:en'  # put your serach query here
    query2 = '#Melbourne lang:en'

    client = couchdb3.Server(            # put the couchDB server information here
        "http://172.26.132.196:5984",
        user="admin",
        password="admin"
    )
    db_name = "raw_tweets"   #couchDB database name
    db_name2 = "geo_tweets"

    count = 0
    ### Run
    if(client.up()):
        while(True): ## infinite loop
            try:
                next_tokens = tw.crawler(query, BEARER_TOKEN, 50, 5, client, db_name, db_name2)
            except Exception as ee:
                print('exception occur:'+ str(ee))
                time.sleep(900)
