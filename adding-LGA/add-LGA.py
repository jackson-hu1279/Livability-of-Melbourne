import geojson 
import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from sqlalchemy import null

def write_tweets(filename, tweets):
    with open(filename, "w", encoding="utf-8") as updated_file:
        print('{"docs": [', file=updated_file)
        i = 0
        for record in tweets:
            json.dump(record, updated_file)
            if i < len(tweets) -1:
                updated_file.write(",")
            updated_file.write('\n')
            i += 1
        print(']}', file=updated_file)

    with open(filename) as fp:
        # only to check that the format is correct
        json.load(fp)
    
# Open the geojson file 
with open("vic-lga.geojson", "r") as f:
    gj = geojson.load(f)



# Greater melbourne LGAs taken from wikipedia page
GREATER_MELBOURNE_LGA_LIST = [
    "Melbourne City", "Port Phillip City", "Stonnington City", "Yarra City",
    "Banyule City", "Bayside City", "Boroondara City", "Darebin City",
    "Glen Eira City", "Hobsons Bay City", "Kingston City", "Manningham City",
    "Maribyrnong City", "Monash City", "Moonee Valley City", "Moreland City",
    "Whitehorse City", "Brimbank City", "Cardinia Shire", "Casey City",
    "Frankston City", "Greater Dandenong City", "Hume City", "Knox City",
    "Maroondah City", "Melton City", "Mornington Peninsula Shire", "Nillumbik Shire",
    "Whittlesea City", "Wyndham City", "Yarra Ranges Shire"
    ]

# Greater melbourne LGA codes in alphabetical order (Banyule City -> Yarra Ranges Shire)
GREATER_MELBOURNE_LGA_CODES = [
    20660, 20910, 21110, 21180, 21450, 21610, 21890, 22170, 22310,
    22670, 23110, 23270, 23430, 23670, 24210, 24330, 24410, 24600,
    24650, 24970, 25060, 25250, 25340, 25710, 25900, 26350, 26980,
    27070, 27260, 27350, 27450
]

LGA_FEATURES_LIST = []
count = 0
# There are 91 LGAs in Victoria - we only want information about LGAs in Greater Melbourne (31), we store in a list object
for i in range(0,92):
    lga_features = gj["features"][i]
    lga_name = lga_features["properties"]["LGA_NAME"]
    if lga_name in GREATER_MELBOURNE_LGA_LIST:
        lga_features["properties"]["LGA_CODE"] = GREATER_MELBOURNE_LGA_CODES[count]
        count += 1
        LGA_FEATURES_LIST.append(lga_features)

# Convert all the coordinates in the LGA to Polygon type 
for i in range(len(LGA_FEATURES_LIST)):
    LGA_FEATURES_LIST[i]["geometry"]["coordinates"][0] = Polygon(LGA_FEATURES_LIST[i]["geometry"]["coordinates"][0])

# print(LGA_FEATURES_LIST)
# checking that there are 31 features 
# print(len(LGA_FEATURES_LIST))
# print(LGA_FEATURES_LIST[0]["geometry"])
# print(LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0])
# print(type(Polygon(LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0])))



# print(LGA_FEATURES_LIST[30]["geometry"]["coordinates"][0])

# ----------------------------------------------------------------------------------------------
# Step 2 - Open up all the extracted json files and see if the coordinate (convert to Point object) is in the polygon

# sample code with only the first extracted json file (extracted-1.json)
# Open the json file

# counter = 0
# chunk_size = 25000
# file_num = 0
# total_files = 1

# here for our new version of the code, we would be opening crimes.json and health.json
# crimes.json

# def attach_lga(filename):
#     with_lga = []
#     without_lga = []

#     with open ("crimes.json", "r", encoding = "utf-8") as tweets_json:
#         tweet_data = json.load(tweets_json)
#         for tweet in tweet_data['docs']:
#             coords = tweet.get('coordinates')
#             if coords:
#                 point = Point(coords["coordinates"])  
#                 for j in range(len(LGA_FEATURES_LIST)):
#                     if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
#                         tweet["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
#                         tweet["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
#                         print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
#                         print(tweet["LGA_NAME"])
#                         with_lga.append(tweet)
            
#             if "LGA_NAME" not in tweet:
#                 print("not in LGA")
#                 tweet["LGA_NAME"] = "NO LGA"
#                 tweet["LGA_CODE"] = "NO LGA CODE"
#                 without_lga.append(tweet)
    
#     return(tweet_data, with_lga, without_lga)

# Crimes

with_lga = []
without_lga = []

with open ("crimes.json", "r", encoding = "utf-8") as tweets_json:
    tweet_data = json.load(tweets_json)
    for tweet in tweet_data['docs']:
        coords = tweet.get('coordinates')
        if coords:
            point = Point(coords["coordinates"])  
            for j in range(len(LGA_FEATURES_LIST)):
                if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
                    tweet["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
                    tweet["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
                    print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
                    print(tweet["LGA_NAME"])
                    with_lga.append(tweet)
        
        if "LGA_NAME" not in tweet:
            print("not in LGA")
            tweet["LGA_NAME"] = "NO LGA"
            tweet["LGA_CODE"] = "NO LGA CODE"
            without_lga.append(tweet)

    write_tweets('crimes-updated.json', tweet_data['docs'])
    write_tweets('crimes-updated-lga.json', with_lga)
    write_tweets('crimes-updated-without-lga.json', without_lga)

# Health 

with_lga = []
without_lga = []

with open ("health.json", "r", encoding = "utf-8") as tweets_json:
    tweet_data = json.load(tweets_json)
    for tweet in tweet_data['docs']:
        coords = tweet.get('coordinates')
        if coords:
            point = Point(coords["coordinates"])  
            for j in range(len(LGA_FEATURES_LIST)):
                if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
                    tweet["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
                    tweet["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
                    print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
                    print(tweet["LGA_NAME"])
                    with_lga.append(tweet)
        
        if "LGA_NAME" not in tweet:
            print("not in LGA")
            tweet["LGA_NAME"] = "NO LGA"
            tweet["LGA_CODE"] = "NO LGA CODE"
            without_lga.append(tweet)

    write_tweets('health-updated.json', tweet_data['docs'])
    write_tweets('health-updated-lga.json', with_lga)
    write_tweets('health-updated-without-lga.json', without_lga)
    

# while file_num < total_files:
#     file_num += 1
#     with open ("extracted-{0}.json".format(file_num), "r", encoding = "utf-8") as tweets_json:
#         tweet_data = json.load(tweets_json)

# # some tests
# # print(tweet_data["docs"][0]["doc"]["coordinates"]["coordinates"])
# # point = Point(tweet_data["docs"][0]["doc"]["coordinates"]["coordinates"])
# # print(point)
# # print(tweet_data["docs"][0]["doc"]["geo"]["coordinates"])

# # print(len(tweet_data["docs"]))


#     for i in range(len(tweet_data["docs"])):
#         if type(tweet_data["docs"][i]["doc"]["coordinates"]["coordinates"]) != None: # TODO: none type object not subscriptable error
#             point = Point(tweet_data["docs"][i]["doc"]["coordinates"]["coordinates"])  
#             for j in range(len(LGA_FEATURES_LIST)):
#                 if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
#                     tweet_data["docs"][i]["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
#                     tweet_data["docs"][i]["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
#                     print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
#                     print(tweet_data["docs"][i]["LGA_NAME"])
#             if "LGA_NAME" not in tweet_data["docs"][i]:
#                 print("not in LGA")
#                 tweet_data["docs"][i]["LGA_NAME"] = "NO LGA"
#                 tweet_data["docs"][i]["LGA_CODE"] = "NO LGA CODE"


# # Step 3 - write to new json file
#     counter = 0
#     chunk_size = 1000

#     with open("updated-{0}.json".format(file_num), "w", encoding="utf-8") as updated_file:
#         print('{"docs": [', file=updated_file)
#         for record in tweet_data["docs"]:
#             counter += 1
#             if counter == chunk_size:
#                 json.dump(record, updated_file)
#                 updated_file.write('\n')
#             else: 
#                 json.dump(record, updated_file)
#                 updated_file.write(",")
#                 updated_file.write('\n')
#         print(']}', file=updated_file)