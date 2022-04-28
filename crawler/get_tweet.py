import tweepy
import pickle
import time



def reform_tweet(raw_tweet):
    """
    Reform the tweet data into a dictionary form.
    Each tweet is a dictionary contains: tweet_id, text, author_id, create_at, geo
    """
    tweet_dict = dict()
    tweet_dict['tweet_id'] = raw_tweet.id
    tweet_dict['author_id'] = raw_tweet.author_id
    tweet_dict['text'] = raw_tweet.text
    tweet_dict['created_at'] = raw_tweet.created_at
    tweet_dict['geo'] = raw_tweet.geo

    return tweet_dict


def preprocess(raw_tweet, id_set, tweet_list):
    """
    Process all tweets in one turn, remove tweets withou geo info
    """
    for data in raw_tweet:
        if(data.geo != None): # Only keep tweets with geo information
            if(data.id not in id_set):  #remove duplicate
                id_set.add(data.id)
                tweet_list.append(reform_tweet(data))
    
    return tweet_list, id_set


def get_tweet_1(query, token):
    """
    Get tweet using Twitter API 2.0. 
    Using keywords(query) as a main parameter
    Caputure tweet_id, text, geo, author_id, create_at
    """
    client = tweepy.Client(bearer_token= token)
    # each time capture 100 tweets
    tweets = client.search_recent_tweets(query=query, tweet_fields=['author_id', 'created_at', 'geo'], max_results=100)

    return tweets.data


def crawler(query, tokens, tweets_each_turn, turns):
    """
    Main function. Use query as filter, token for authocation, and number of tweets each turn
    Turns suggest how many turns this function will run
    Get tweets from Twitter
    Remove tweets without geo
    Refrom tweets to dictionary type
    Save tweets as pickle file
    Automatically repeat this process.
    For one token, speed limit is 900 tweets/15min(1/sec)
    """

    time_gap = int (tweets_each_turn / len(tokens)) + 1
    count = 0
    tweet_list = []
    id_set = set()
    while(count < turns):
        for token in tokens:
            data = get_tweet_1(query, token)
            tweet_list, id_set = preprocess(data, id_set, tweet_list)
            time.sleep(time_gap)
        
        count = count + 1
    
    return tweet_list
        


#Set up
BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAALWBbQEAAAAA%2FbQ0tpIE3uy14yUmYU0AiocoH6c%3DDkX3Fl2TdMFgRBCivYCSMajfqglkm8DkyylcAXkUFFceAIOBRB",
"AAAAAAAAAAAAAAAAAAAAAF1YbQEAAAAAEOLr26RmQ1V0eVq1xDR%2FUioYOKY%3DAHtIcXsDHv5lnyzj8KAdzlEbVVaC85k3uvvUvYESyeK0h9knqM"]

query = 'from:suhemparack -is:retweet'