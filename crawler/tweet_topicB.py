import get_tweet as tw
import couchdb3
import tweepy
import pickle
from shapely.geometry import Point
import time

def main():
    #### Set up
    BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAABTzbAEAAAAAdojtSeSLrMbP1332MUDWvDH%2BizY%3DMTbgi5FKJHNnLwwO5acTPNP3uWRPrUAtoxnckAzXiDq3BwU4Bo",
    "AAAAAAAAAAAAAAAAAAAAAN%2FIbQEAAAAAsOzq2imuYFShxFO1EnN4EcOEA6c%3DMgCTYsVUpitvOTzwJFpMDCOvSPb2K5PNOjE1kLxnaTGXSPw462"]

    query1 = 'anxiety OR craziness OR delusion OR depression OR (disturbed mind) OR dying OR (emotional disorder) OR (emotional instability) OR exhausted lang:en'
    query2 = 'hallucination OR insanity OR (mental disorder) OR (mental disease) OR (mental sickness) OR (mental health) OR (nervous disorder) OR neurosis lang:en'
    query3 = '(neurotic disorder) OR (personality disorder) OR schizophrenia OR self-harm OR (self harm) OR suicide lang:en'

    client = couchdb3.Server(
        "http://172.26.132.196:5984",
        user="admin",
        password="admin"
    )
    db_name = "mental_tweets"


    ### Run
    if(client.up()):
        while(True): ## infinite loop
            try:
                next_tokens = tw.crawler_2(query1, BEARER_TOKEN, 100, 5, client, db_name)
                next_tokens = tw.crawler_2(query2, BEARER_TOKEN, 100, 5, client, db_name)
                next_tokens = tw.crawler_2(query3, BEARER_TOKEN, 100, 5, client, db_name)
            except Exception as ee:
                print('exception occur:'+ str(ee))
                time.sleep(900)