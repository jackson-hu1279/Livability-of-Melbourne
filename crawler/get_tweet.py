import tweepy
import pickle
import time
import couchdb3


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
    Process all tweets in one turn, remove tweets withou geo info
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


def crawler(query, tokens, tweets_each_turn, turns, client, db_name):
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

    save_to_couchDB(client, tweet_list, db_name)
    
    return next_page



def save_to_couchDB(client, tweet_data, db_name):
    """
    Save tweets to CouchDB, remove all duplicates
    """
    if(client.up() == True):
        print("Connected to CouchDB")
    else:
        print("Unable to connect to CouchDB")
        return

    if( db_name not in client.all_dbs()):
        print("No database:" + db_name + ", create one first")
        client.create(db_name)
    
    db = client.get(db_name)
    count = 0

    for data in tweet_data:
        if(data['_id'] not in db):
            db.save(data)
            count += 1
    
    print(str(count) + " tweets is successfully saved to CouchDB")
    return


#### Set up
BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAALWBbQEAAAAA%2FbQ0tpIE3uy14yUmYU0AiocoH6c%3DDkX3Fl2TdMFgRBCivYCSMajfqglkm8DkyylcAXkUFFceAIOBRB",
"AAAAAAAAAAAAAAAAAAAAAF1YbQEAAAAAEOLr26RmQ1V0eVq1xDR%2FUioYOKY%3DAHtIcXsDHv5lnyzj8KAdzlEbVVaC85k3uvvUvYESyeK0h9knqM"]                
query1 = '#Melbourne lang:en'
query2 = 'Melbourne rape lang:en'
query3 = 'Melbourne family violence lang:en'

client = couchdb3.Server(
    "http://172.26.132.196:5984",
    user="admin",
    password="admin"
)
db_name = "renkai_tweets"


### Run
if(client.up()):
    while(True): ## infinite loop
        next_token = crawler(query1, BEARER_TOKEN, 10, 3, client, db_name)