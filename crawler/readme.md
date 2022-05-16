Use tweet_couchDB.ipynb, test.ipynb, more_test.ipynb to test
get_tweet.py define all the functions used in deploy files

Deploy files are: raw_tweet.py, tweet_topicA.py, tweet_topicB.py

raw_tweet.py harvests all tweets about Melbourne(with or without geo info)
tweet_topicA.py harvests all tweets about topic A(with geo info)
tweet_topicB.py harvests all tweets about topic B(with geo info)

To run a tweet harvester instance, use raw_tweet.py as a template.
Make sure all files are under crawler folder

Information you should provide:
BEAR_TOAKNS = []   Put the Twitter API2.0 beartokens here.
couchDB server information, including server IP address, username and password.
Search query: provide a serach query to define what kind of tweets you want. Examples are in raw_tweet.py, tweet_topicA.py, tweet_topicB.py
couchDB database name:  please make sure the name only contains lowercase English characters. 
The harvester will create such database if it doesn't exist.
If you use crawler1(), you must provide 2 database name, crawler2() only need 1.
crawler2() is designed for the project scenarios, for more general purpose, please use crawler1()


To run the tweet harvester instance(s) in the cloud, please check the Ansible module and demo video.

To run a tweet harvester locally, simply use the command line and run the instance file. You must install Python3.9,
and 3rd party library: tweepy, couchdb3, shapely. Make sure you have an available couchDB server. 

LGA_list.pkl is used for attatching LAG tags to tweets

5 tokens in total, 1 for raw_tweet.py, 2 for tweet_topicA.py, 2 for tweet_topicB.py

Do NOT use other files.

