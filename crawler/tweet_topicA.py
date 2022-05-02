import get_tweet as tw
import couchdb3
import tweepy





#### Set up
BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAAF1YbQEAAAAAEOLr26RmQ1V0eVq1xDR%2FUioYOKY%3DAHtIcXsDHv5lnyzj8KAdzlEbVVaC85k3uvvUvYESyeK0h9knqM",
"AAAAAAAAAAAAAAAAAAAAACVqcAEAAAAAOBsy5JBbA1uQ1g0JoI6GZYLgNCQ%3DmxBL5JiQNv8CTVi6yCPADp8wFnbbK9es1xgO2458Q5KF0ygstO"]

query = 'incident OR (family violence) OR Incident OR drug OR robbery OR theft OR trespassing lang:en'

client = couchdb3.Server(
    "http://172.26.132.196:5984",
    user="admin",
    password="admin"
)
db_name = "topicA_tweets"


count = 0
### Run
if(client.up()):
    while(True): ## infinite loop
        if(count == 0):
            next_tokens = tw.crawler_2(query, BEARER_TOKEN, 100, 20, client, db_name)
            count = 1

        next_tokens = tw.crawler_2(query, BEARER_TOKEN, 100, 5, client, db_name)