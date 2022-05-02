import os
import tweet_topicA
import tweet_topicB
import raw_tweet

scenario = os.environ['SCENARIO']
print(scenario)

if scenario == "Crime":
    print("Execute scenario of Crime")
    tweet_topicA.main()
elif scenario == "Mental":
    print("Execute scenario of Mental Health")
    tweet_topicB.main()
else:
    print("Collect raw tweets")
    raw_tweet.main()
