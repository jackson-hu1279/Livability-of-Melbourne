import json

# TODO: try to filter out all the keys except "doc" first
# TODO: then we try and filter out all the keys in "doc" except _id, _rev, author_id, text, created_at, coordinates, geo
# TODO: then filter through the tweet["docs"]["doc"]["text"] and search for the keywords 
keywords_crime = ["incident", "family violence", "drug", "robbery", "theft", "trespas"]
keywords_health =["suicide", "depression", "anxiety", "dying", "death", "hallucination", "self harm", "personality disorder"]


allowed_keys = ["coordinates", "text", "lang"]

# i = 0
# trying with a smaller json file first - i want to do this with the massive json file though 
with open('twitter-melb.json', 'r', encoding='utf-8') as unfiltered_file:
    # skip the first line 
    
    line = next(unfiltered_file)
    health = []
    crimes = []

    for line in unfiltered_file:
        # if i == 10000:
        #     break
        # i += 1
        line = line.lower()
        newline = {}
        for key in keywords_crime:
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
                            d = {}
                            for key in allowed_keys:
                                d[key] = js['doc'][key]

                            crimes.append(json.dumps(d))
                          
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
                            health.append(json.dumps(js['doc']))
                            
                            break
                if found:
                    break       

with open("health.json", "w", encoding = 'utf-8') as test_file:
    print('{"docs": [', file=test_file)
    print(",\n".join(health), file=test_file)
    print("]}\n", file=test_file)


with open("crimes.json", "w", encoding = 'utf-8') as test_file:
    print('{ "doc" : [', file=test_file)
    print(",\n".join(crimes), file=test_file)
    print("]}\n", file=test_file)
