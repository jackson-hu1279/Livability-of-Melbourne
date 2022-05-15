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
# - Chi Yin Wong (Student ID: 836872)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------

import json

keywords_crime = [
    "abduct", "abuse", "abusive", "arson", "assassin", "assault", "bigamy", "blackmail", "bombing", "bribe", "burglar", 
    "corrupt", "crime", "cybercrime", "cyber crime", "domestic violence", "drug", "embezzle", "espionage", "family violence", 
    "felony", "forgery", "fraud", "gang", "genocide", "hijack", "hit and run", "homicide", "homicidal", "hooliganism", 
    "identity theft", "incident", "infract", "kidnap", "looting", "lynch", "manslaughter", "mugging", "mugged", "murder",
    "pickpocket", "pilfering", "poaching", "rape", "rapist", "riot", "robbery", "robbed", "shoplift", "slander", "smuggle", 
    "smuggling", "terrorism", "theft", "traffick", "transgression", "trespass", "vandalism", "vandalize", "vandalise",
    "voyeurism", "violate", "violation"
    ]

keywords_health =[
    "anxiety", "anxious", "craziness", "delusion", "delude", "depress", "disturbed mind", "dying", "death",
    "emotional disorder", "emotional instability", "exhaust", "hallucinate", "hallucinating", "hallucination",
    "insanity", "mental disorder", "mental disease", "mental health", "mental sickness", "nervous disorder",
    "neurosis", "neurotic disorder", "personality disorder", "schizophrenia", "self harm", "self-harm", "suicide",
    "suicidal", "suiciding"
    ]

allowed_keys = ["_id", "text", "created_at", "coordinates", "geo"]

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
