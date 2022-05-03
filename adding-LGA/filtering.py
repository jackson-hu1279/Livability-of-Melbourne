import json

# TODO: try to filter out all the keys except "doc" first
# TODO: then we try and filter out all the keys in "doc" except _id, _rev, author_id, text, created_at, coordinates, geo
# TODO: then filter through the tweet["docs"]["doc"]["text"] and search for the keywords 
keywords_crime = [
    "incident", "incidences", "family violence", "drug", "drugged", "drugging", "robbery", "robbed","theft", "theif", 
    "trespass", "trespassing", "trespasser", "murder", "murdered"
    ]
keywords_health =[
    "suicide", "depressed", "depression", "anxiety", "anxious", "dying", "death", "hallucination", "hallucinate",
    "hallucinating", "self harm", "personality disorder"
    ]


allowed_keys = ["_id", "_rev", "text", "created_at", "coordinates", "geo"]

# i = 0
with open('twitter-melb.json', 'r', encoding='utf-8') as unfiltered_file:
    # skip the first line 
    
    line = next(unfiltered_file)
    health = []
    crimes = []
    # i = 0
    for line in unfiltered_file:
        # if i == 10000:
        #      break
        # i += 1
        # make the entire tweet lower case 
        line = line.lower()
        # newline = {}
        for key in keywords_crime:
            found = False
            if key in line:
                # potential match, load the string into memory without the comma at the end
                js = json.loads(line[:-2])
                # confirm by cechking the exact text
                text = js['doc']['text']

                if key in text:
                    for word in text.split():
                        if word.startswith(key):
                            found = True
                            d_crimes = {}
                            for key in allowed_keys:
                                d_crimes[key] = js['doc'][key]
                            d_crimes['author_id'] = js['doc']['user']['id']
                            crimes.append(json.dumps(d_crimes))
                          
                            break
                
                if found:
                    break

        for key in keywords_health:
            found = False
            if key in line:
                # potential match
                js = json.loads(line[:-2])
                # confirm by cechking the exact text
                text = js['doc']['text']
                if key in text:
                    for word in text.split():
                        if word.startswith(key):
                            found = True
                            d_health = {}
                            for key in allowed_keys:
                                d_health[key] = js['doc'][key]
                            d_crimes['author_id'] = js['doc']['user']['id']
                            health.append(json.dumps(d_health))
                            
                            break
                if found:
                    break       

with open("health.json", "w", encoding = 'utf-8') as test_file:
    print('{"docs": [', file=test_file)
    print(",\n".join(health), file=test_file)
    print("]}\n", file=test_file)


with open("crimes.json", "w", encoding = 'utf-8') as test_file:
    print('{"docs": [', file=test_file)
    print(",\n".join(crimes), file=test_file)
    print("]}\n", file=test_file)
