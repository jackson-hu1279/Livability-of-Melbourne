import os

scenario = os.environ['SCENARIO']

if scenario == "Crime":
    print("Execute scenario of Crime")
    exec(open("tweet_topicA.py").read())
elif scenario == "Mental":
    print("Execute scenario of Mental Health")
    exec(open("tweet_topicB.py").read())
else:
    print("Collect raw tweets")
    exec(open("raw_tweet.py").read())
