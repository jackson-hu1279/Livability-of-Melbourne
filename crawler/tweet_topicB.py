import get_tweet as tw
import couchdb3
import tweepy

def main():
    print("Executing harvester - Mental Health")

    #### Set up
    BEARER_TOKEN = ["AAAAAAAAAAAAAAAAAAAAABTzbAEAAAAAdojtSeSLrMbP1332MUDWvDH%2BizY%3DMTbgi5FKJHNnLwwO5acTPNP3uWRPrUAtoxnckAzXiDq3BwU4Bo",
    "AAAAAAAAAAAAAAAAAAAAAN%2FIbQEAAAAAsOzq2imuYFShxFO1EnN4EcOEA6c%3DMgCTYsVUpitvOTzwJFpMDCOvSPb2K5PNOjE1kLxnaTGXSPw462"]

    query = 'suiside OR depression OR anxiety OR dying OR hallucination OR (self harm) OR (personality disorder) lang:en'

    client = couchdb3.Server(
        "http://172.26.132.196:5984",
        user="admin",
        password="admin"
    )
    db_name = "mental_tweets"

    count = 0
    ### Run
    if(client.up()):
        while(True): ## infinite loop
            if(count == 0):
                next_tokens = tw.crawler_2(query, BEARER_TOKEN, 100, 20, client, db_name)
                count = 1

            next_tokens = tw.crawler_2(query, BEARER_TOKEN, 100, 10, client, db_name)