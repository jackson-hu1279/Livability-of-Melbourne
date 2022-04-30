import geojson 

# Open the geojson file 
with open("vic-lga.geojson", "r") as f:
    gj = geojson.load(f)

# access the third row (second object) in the geojson file
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

LGA_FEATURES_LIST = []

# There are 91 LGAs in Victoria - we only want information about LGAs in Greater Melbourne (31), we store in a list object
for i in range(0,92):
    lga_features = gj["features"][i]
    lga_name = gj["features"][i]["properties"]["LGA_NAME"]
    if lga_name in GREATER_MELBOURNE_LGA_LIST:
        LGA_FEATURES_LIST.append(lga_features)

# print(LGA_FEATURES_LIST)
# checking that there are 31 features 
print(len(LGA_FEATURES_LIST))
# print(LGA_FEATURES_LIST[0]["geometry"])

# Finding the bounding box for the first area for centroid calculation
# we take the first coordinate as the initial values 
x_low = LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0][0][0]
y_low = LGA_FEATURES_LIST[0]["geometry"]["coordinates"][0][0][1]
x_high = x_low
y_high = y_low


for j in range(0, len(LGA_FEATURES_LIST[0]["geometry"]["coordinates"])):
    for coord in LGA_FEATURES_LIST[0]["geometry"]["coordinates"][j]:
        if coord[0] < x_low:
            x_low = coord[0]
        if coord[1] < y_low:
            y_low = coord[1]
        if coord[0] > x_high:
            x_high = coord[0]
        if coord[1] > y_high:
            y_high = coord[1]

print(x_low,y_low,x_high,y_high)

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




