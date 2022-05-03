import get_tweet as tw
import couchdb3
import tweepy
import pickle
from shapely.geometry import Point

def main():
    #### Set up
    BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAAF1YbQEAAAAAEOLr26RmQ1V0eVq1xDR%2FUioYOKY%3DAHtIcXsDHv5lnyzj8KAdzlEbVVaC85k3uvvUvYESyeK0h9knqM",
    "AAAAAAAAAAAAAAAAAAAAACVqcAEAAAAAOBsy5JBbA1uQ1g0JoI6GZYLgNCQ%3DmxBL5JiQNv8CTVi6yCPADp8wFnbbK9es1xgO2458Q5KF0ygstO"]

    query1 = 'abduction OR abuse OR accident OR arson OR assassination OR assault OR bigamy OR blackmail OR bombing OR bribery OR corruption OR crime OR transgression OR violation lang:en'
    query2 = 'cybercrime OR (domestic violence) OR drug OR embezzlement OR espionage OR (family violence) OR felony OR forgery OR fraud OR gang OR genocide OR vandalism lang:en'
    query3 = 'hijacking OR (hit run) OR homicide OR hooliganism OR (identity theft) OR incident OR infraction OR kidnapping OR looting OR lynching OR trespassing OR voyeurism lang:en'
    query4 = 'manslaughter OR mugging OR murder OR pickpocketing OR pilfering OR poaching OR rape OR riot OR robbery OR shoplifting OR slander OR smuggling OR terrorism OR theft OR trafficking lang:en'

    client = couchdb3.Server(
        "http://172.26.132.196:5984",
        user="admin",
        password="admin"
    )
    db_name = "crime_tweets"



    ### Run
    if(client.up()):
        while(True): ## infinite loop
            next_tokens = tw.crawler_2(query1, BEARER_TOKEN, 100, 5, client, db_name)
            next_tokens = tw.crawler_2(query2, BEARER_TOKEN, 100, 5, client, db_name)
            next_tokens = tw.crawler_2(query3, BEARER_TOKEN, 100, 5, client, db_name)
            next_tokens = tw.crawler_2(query4, BEARER_TOKEN, 100, 5, client, db_name)