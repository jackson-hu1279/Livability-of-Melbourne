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

import tweepy
import pickle
import time
import couchdb3
from shapely.geometry import Point


### definitions
def reform_tweet(raw_tweet):
    """
    Reform the tweet data into a dictionary form.
    Each tweet is a dictionary contains: tweet_id, text, author_id, create_at, geo
    """
    tweet_dict = dict()
    tweet_dict['_id'] = str(raw_tweet.id)
    tweet_dict['author_id'] = raw_tweet.author_id
    tweet_dict['text'] = raw_tweet.text
    tweet_dict['created_at'] = str(raw_tweet.created_at)
    tweet_dict['geo'] = raw_tweet.geo

    return tweet_dict


def preprocess(raw_tweet, tweet_list):
    """
    Process all tweets in one turn
    """
    for data in raw_tweet:
        tweet_list.append(reform_tweet(data))
    
    return tweet_list


def get_tweet_1(query, token, tweets_each_turn, next_page = None):
    """
    Get tweet using Twitter API 2.0. 
    Using keywords(query) as a main parameter
    Caputure tweet_id, text, geo, author_id, create_at
    """
    client = tweepy.Client(bearer_token= token)
    # each time capture 100 tweets
    tweets = client.search_recent_tweets(query=query, tweet_fields=['author_id', 'created_at', 'geo'], max_results=tweets_each_turn, next_token=next_page)

    print(tweets.meta)

    return tweets.data, tweets.meta['next_token']


def crawler(query, tokens, tweets_each_turn, turns, client, db_name, db_name2):
    """
    This crawler is used to get raw tweet(including tweets without geo)
    Main function. Use query as filter, token for authocation, and number of tweets each turn
    Turns suggest how many turns this function will run
    Get tweets from Twitter
    Refrom tweets to dictionary type
    Save tweets to CouchDB
    Automatically repeat this process.
    For one token, speed limit is 900 tweets/15min(1/sec)
    """

    time_gap = int (tweets_each_turn / len(tokens)) + 1
    
    count = 0
    next_page = None
    tweet_list = []
    while(count < turns):
        for token in tokens:
            data, next_page = get_tweet_1(query, token, tweets_each_turn, next_page)
            tweet_list = preprocess(data, tweet_list)
            time.sleep(time_gap)
        
        count = count + 1

    #add LGA tags
    tweet_list = add_lga_tags('LGA_list.pkl', tweet_list)

    save_to_couchDB(client, tweet_list, db_name, db_name2)
    
    return next_page



def save_to_couchDB(client, tweet_data, db_name, db_name2):
    """
    Save tweets to CouchDB, remove all duplicates
    Save tweets without geo info to db_name
    Save tweets with geo info to db_name2
    Used to collect all tweets(including tweets without geo)
    """
    if(client.up() == True):
        print("Connected to CouchDB")
    else:
        print("Unable to connect to CouchDB")
        return

    if( db_name not in client.all_dbs()):
        print("No database:" + db_name + ", create one first")
        client.create(db_name)

    if( db_name2 not in client.all_dbs()):
        print("No database:" + db_name2 + ", create one first")
        client.create(db_name2)
    
    db1 = client.get(db_name)
    count1 = 0

    db2 = client.get(db_name2)
    count2 = 0

    for data in tweet_data:
        if(data['geo'] == None):
            if(data['_id'] not in db1):
                db1.save(data)
                count1 += 1
        
        else:  #store tweets with geo to another database
            if(data['_id'] not in db2):
                db2.save(data)
                count2 += 1
    
    print(str(count1) + " tweets(no geo) are successfully saved to database" + db_name)
    print(str(count2) + " tweets(with geo) are successfully saved to database" + db_name2)
    return




def crawler_2(query, tokens, tweets_each_turn, turns, client, db_name):
    """
    Main function. Use query as filter, token for authocation, and number of tweets each turn
    Turns suggest how many turns this function will run
    Get tweets from Twitter
    Refrom tweets to dictionary type
    Save tweets to CouchDB
    Automatically repeat this process.
    For one token, speed limit is 900 tweets/15min(1/sec)
    """

    time_gap = int (tweets_each_turn / len(tokens)) + 1
    
    count = 0
    next_page = None
    tweet_list = []
    while(count < turns):
        for token in tokens:
            data, next_page = get_tweet_1(query, token, tweets_each_turn, next_page)
            tweet_list = preprocess(data, tweet_list)
            time.sleep(time_gap)
        
        count = count + 1

    #add LGA tags
    tweet_list = add_lga_tags('LGA_list.pkl', tweet_list)

    save_to_couchDB_2(client, tweet_list, db_name)
    
    return next_page



def save_to_couchDB_2(client, tweet_data, db_name):
    """
    Save tweets to CouchDB, remove all duplicates
    Save tweets with geo info to db_name
    Filter is based on coorinates
    Used for specific scenario
    """

    geo_filter = [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995]

    if(client.up() == True):
        print("Connected to CouchDB")
    else:
        print("Unable to connect to CouchDB")
        return

    if( db_name not in client.all_dbs()):
        print("No database:" + db_name + ", create one first")
        client.create(db_name)
    
    db1 = client.get(db_name)
    count1 = 0

    for data in tweet_data:
        if(data['geo'] != None):#only store tweets with geo to database
            if('coordinates' in data['geo'].keys()):
                if(data['_id'] not in db1):
                    latitude = data['geo']['coordinates']['coordinates'][0] 
                    longitude = data['geo']['coordinates']['coordinates'][1] 
                    if( latitude >= geo_filter[0] and latitude <= geo_filter[2]):
                        if(longitude >= geo_filter[1] and longitude <= geo_filter[3]):
                            db1.save(data)
                            count1 += 1
    
    print(str(count1) + " tweets(with geo) are successfully saved to database" + db_name)
    return



def add_lga_tags(file_name, tweet_data):
    """
    Add LGA tags to tweets which have coordinates
    file_name indicates the LGA lists stored as .pkl file
    Add 2 attributes to tweet: LAG name, LGA code
    """

    inputs = open(file_name,'rb')
    LGA_FEATURES_LIST = pickle.load(inputs)
    inputs.close()

    for tweet in tweet_data:
        if(tweet['geo'] != None):
            if('coordinates' in tweet['geo'].keys()):
                coords = tweet['geo']['coordinates']
                point = Point(coords["coordinates"])  
                for j in range(len(LGA_FEATURES_LIST)):
                    if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
                        tweet["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
                        tweet["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
                        print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
                        print(tweet["LGA_NAME"])
            
                if "LGA_NAME" not in tweet:
                    #print("not in LGA")
                    tweet["LGA_NAME"] = "NO LGA"
                    tweet["LGA_CODE"] = "NO LGA CODE"
    
    return tweet_data
