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
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------


import json

# list of greater melbourne lga code
greater_melbourne_lga_code = [24600, 25900, 26350, 27350, 20660, 20910, 21110, 21890, 22310, 23110, 23430, 24210, 24330,
                              24970, 25060, 25250, 26980, 21180, 21450, 21610, 22170, 22670, 23270, 23670, 24410,
                              24650, 25340, 25710, 27070, 27260, 27450]
greater_melbourne_lga_name = ["Melbourne City", "Port Phillip City", "Stonnington City", "Yarra City", "Banyule City", "Bayside City", "Boroondara City", "Darebin City", "Glen Eira City",
                              "Hobsons Bay City", "Kingston City", "Manningham City", "Maribyrnong City", "Monash City", "Moonee Valley City",
                              "Moreland City", "Whitehorse City", "Brimbank City", "Cardinia Shire", "Casey City", "Frankston City", "Greater Dandenong City",
                              "Hume City", "Knox City", "Maroondah City", "Melton City", "Mornington Peninsula Shire", "Nillumbik Shire", "Whittlesea City", "Wyndham City", "Yarra Ranges Shire"]

file_name1 = "results-crime.json"
file_name2 = "results-vic-lga.geojson"


def makeDict(code, name):
    lga_dict = {}
    for i in range(0, len(code)):
        lga_dict[name[i]] = code[i]
    return lga_dict


with open(file_name1) as f:
    dataset = json.load(f)
    lga_drug = {}
    lga_violence = {}
    for data in dataset["greater_melbourne"]:
        lga_code = data["lga_code"]
        drug_use_per_1000 = data["drug_use_per_1000"]
        family_violence_incidents_per_1000 = data["family_violence_incidents_per_1000"]
        lga_drug[lga_code] = drug_use_per_1000
        lga_violence[lga_code] = family_violence_incidents_per_1000


with open(file_name2) as f:
    dataset = json.load(f)
    results_list = []
    data_dict = makeDict(greater_melbourne_lga_code,
                         greater_melbourne_lga_name)
    for data in dataset["features"]:
        lga_name = data["properties"]["lga_name"]
        if lga_name in greater_melbourne_lga_name:
            lga_code = data_dict[lga_name]
            data["properties"] = {
                "lga_code": lga_code, "lga_name": lga_name, "drug_use_per_1000": lga_drug[lga_code],
                "family_violence_incidents_per_1000": lga_violence[lga_code]}
            results_list.append(data)


result = {"type": "FeatureCollection", "features": []}
result["features"] = results_list

# create JSON file to store process data
final_results = result
output_file = "geojson-" + file_name1
with open(output_file, "w") as f:
    json.dump(final_results, f)
