import json

# list of greater melbourne lga code
greater_melbourne_lga_code = [24600, 25900, 26350, 27350, 20660, 20910, 21110, 21890, 22310, 23110, 23430, 24210, 24330,
                              24970, 25060, 25250, 26980, 21180, 21450, 21610, 22170, 22670, 23270, 23670, 24410,
                              24650, 25340, 25710, 27070, 27260, 27450]

with open("dataset.json") as f:
    files = json.load(f)
    file_name = files["data"]
    meta_data = files["meta-data"]

# read distress data from aurin
with open(file_name) as f:
    dataset = json.load(f)
    results_list = []
    for data in dataset["features"]:
        lga_code = data["properties"]["lga_code"]
        if lga_code in greater_melbourne_lga_code:
            lga_name = data["properties"]["lga_name"]
            drug_use_per_1000 = data["properties"]["drug_usage_and_possession_offences_per_1000_pop"]
            family_violence_incidents_per_1000 = data["properties"]["family_violence_incidents_per_1000_pop"]
            result = {"lga_code": lga_code, "lga_name": lga_name,
                      "drug_use_per_1000": drug_use_per_1000,
                      "family_violence_incidents_per_1000": family_violence_incidents_per_1000, }
            results_list.append(result)


# create JSON file to store process data
final_results = {"greater_melbourne": results_list}
output_file = "results-" + file_name
with open(output_file, "w") as f:
    json.dump(final_results, f, indent = 4)

# check output
# with open(output_file) as f:
#     data = json.load(f)
#     for line in data["greater_melbourne"]:
#         print(line)
