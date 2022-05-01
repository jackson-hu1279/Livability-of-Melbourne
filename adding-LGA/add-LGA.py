import geojson 
import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Open the geojson file 
with open("vic-lga.geojson", "r") as f:
    gj = geojson.load(f)

# aside:  access the third row (second object) in the geojson file
# features = gj["features"][2]

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

print(LGA_FEATURES_LIST[2]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[2]["properties"]["LGA_CODE"])
        

# print(LGA_FEATURES_LIST)
# checking that there are 31 features 
print(len(LGA_FEATURES_LIST))
# print(LGA_FEATURES_LIST[0]["geometry"])
# print(LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0])
# print(type(Polygon(LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0])))

# Convert all the coordinates to Polygon type 
for i in range(len(LGA_FEATURES_LIST)):
    LGA_FEATURES_LIST[i]["geometry"]["coordinates"][0] = Polygon(LGA_FEATURES_LIST[i]["geometry"]["coordinates"][0])

# print(LGA_FEATURES_LIST[30]["geometry"]["coordinates"][0])

# ----------------------------------------------------------------------------------------------
# Step 2 - Open up all the extracted json files and see if the coordinate (convert to Point object) is in the polygon

# sample code with only the first extracted json file (extracted-1.json)
# Open the json file
with open ("extracted-1.json", "r", encoding = "utf-8") as tweets_json:
    tweet_data = json.load(tweets_json)

# some tests
print(tweet_data["docs"][0]["doc"]["coordinates"]["coordinates"])
point = Point(tweet_data["docs"][0]["doc"]["coordinates"]["coordinates"])
print(point)
print(tweet_data["docs"][0]["doc"]["geo"]["coordinates"])

print(len(tweet_data["docs"]))

# for i in range(0,10):
#     point = Point(tweet_data["docs"][i]["doc"]["coordinates"]["coordinates"])
#     print(point)

# testing for only the first tweet
for i in range(0,1):
    point = Point(tweet_data["docs"][i]["doc"]["coordinates"]["coordinates"]) #TODO: list index out of range error here when using len(tweet_data["docs"])
    for j in range(len(LGA_FEATURES_LIST)):
        if LGA_FEATURES_LIST[j]["geometry"]["coordinates"][0].contains(point): # if true, add the LGA name and code to the tweet as a new key
            tweet_data["docs"][j]["LGA_NAME"] = LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"]
            tweet_data["docs"][j]["LGA_CODE"] = LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"]
            print("in LGA", LGA_FEATURES_LIST[j]["properties"]["LGA_NAME"], LGA_FEATURES_LIST[j]["properties"]["LGA_CODE"])
            print(tweet_data["docs"][j]["LGA_NAME"])
        # else: # remove the tweet if it doesn't belong in any of the LGA (TODO: Check if LGA_NAME key is empty, if it is, remove)
        #     print("not in LGA")
        #     tweet_data["docs"].pop(j) 

# TODO: Logic error? There is no LGA_NAME key eventhough it prints fine above
print(tweet_data["docs"][0])


# Step 3 - write to new json file

# with open("updated-1.json", "w", encoding="utf-8") as updated_file:
#     json.dump(tweet_data, updated_file)
    























# might not be super useful ---------------------
# Finding the bounding box for the first area for centroid calculation
# we take the first coordinate as the initial values 
# x_low = LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0][0][0]
# y_low = LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0][0][1]
# x_high = x_low
# y_high = y_low


# for j in range(0, len(LGA_FEATURES_LIST[0]["geometry"]["coordinates"])):
#     for coord in LGA_FEATURES_LIST[0]["geometry"]["coordinates"][j]:
#         if coord[0] < x_low:
#             x_low = coord[0]
#         if coord[1] < y_low:
#             y_low = coord[1]
#         if coord[0] > x_high:
#             x_high = coord[0]
#         if coord[1] > y_high:
#             y_high = coord[1]

# print(x_low,y_low,x_high,y_high)

# use the following equation to find the center coordinates - do we need to? 
# TODO: figure out if we need the center of the bounding box for anything
# center_x = x_low + ((x_high - x_low)/2)
# center_y = y_low + ((y_high - y_low)/2)



# note for this code: the geojson returned is missing the "type":"Feature"
# field before "geometry", not sure why it is missing.
# note also missing the "type":"Polygon" inside the geometry dictionary

# with open("greater-melbourne-lga.geojson", "w") as greater_melbourne_file:
#     print('{"type":"FeatureCollection, "features":[', file=greater_melbourne_file)
#     for item in LGA_FEATURES_LIST:
#         # this doesn't work, there is a key error because each item is a dictionary not a string
#         # convert to string? 
#         # print(item[0] + '"type":"Feature",' + item[1:], file=greater_melbourne_file)
#         print(item, file=greater_melbourne_file)
#     print("]}", file=greater_melbourne_file)



# property_0 = gj["features"][0]["properties"]
# property_0_LGA_NAME = gj["features"][91]["properties"]["LGA_NAME"]
# print(property_0)
# print(property_0_LGA_NAME)




