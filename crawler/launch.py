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
# - Renwei Hu (Student ID: 1067974)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------

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
