Use tweet_couchDB.ipynb, test.ipynb, more_test.ipynb to test
get_tweet.py define all the functions used in deploy files

Deploy files are: raw_tweet.py, tweet_topicA.py, tweet_topicB.py

raw_tweet.py harvests all tweets about Melbourne(with or without geo info)
tweet_topicA.py harvests all tweets about topic A(with geo info)
tweet_topicB.py harvests all tweets about topic B(with geo info)

LGA_list.pkl is used for attatching LAG tags to tweets

5 tokens in total, 1 for raw_tweet.py, 2 for tweet_topicA.py, 2 for tweet_topicB.py

Do NOT use other files.

docker files are copied from previous project. Not very sure about its function.